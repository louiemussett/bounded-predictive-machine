import json
import os
from pathlib import Path
import subprocess
import sys

from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import BeliefStateRecord
from bpm_runtime.retrieval import load_trace_records, search_memory_records
from bpm_runtime.trace import save_loop_result_jsonl


def test_loading_missing_trace_files_returns_empty_results(tmp_path) -> None:
    assert load_trace_records(tmp_path / "missing-traces") == []
    assert search_memory_records("anything", trace_dir=tmp_path / "missing-traces") == []


def test_saved_jsonl_records_can_be_loaded(tmp_path) -> None:
    _save_loop(tmp_path, "loop-1", "the section is vague")

    records = load_trace_records(tmp_path / "traces")

    assert records
    assert any(record["record_type"] == "SignalRecord" for record in records)
    assert any(record["record_type"] == "LoopRecord" for record in records)
    assert any(record["record_type"] == "MemoryTraceRecord" for record in records)


def test_search_by_record_type_works(tmp_path) -> None:
    _save_loop(tmp_path, "loop-1", "the section is vague")

    results = search_memory_records(
        trace_dir=tmp_path / "traces",
        record_type="MemoryTraceRecord",
    )

    assert results
    assert all(result["source_record_type"] == "MemoryTraceRecord" for result in results)


def test_keyword_search_works(tmp_path) -> None:
    _save_loop(tmp_path, "loop-1", "the section is vague")

    results = search_memory_records("vague", trace_dir=tmp_path / "traces")

    assert results
    assert any("payload" in result["matched_fields"] for result in results)


def test_multi_word_query_matches_any_meaningful_token(tmp_path) -> None:
    _save_loop(tmp_path, "loop-1", "The current section is too vague.")

    results = search_memory_records("vague section", trace_dir=tmp_path / "traces")

    assert results
    assert any("payload" in result["matched_fields"] for result in results)


def test_punctuation_only_query_returns_zero_matches(tmp_path) -> None:
    _save_loop(tmp_path, "loop-1", "The current section is too vague.")

    results = search_memory_records("???", trace_dir=tmp_path / "traces")

    assert results == []


def test_default_retrieval_returns_no_more_than_default_max_results(tmp_path) -> None:
    for index in range(6):
        _save_loop(tmp_path, f"loop-{index}", f"shared vague topic {index}")

    results = search_memory_records("vague", trace_dir=tmp_path / "traces")

    assert len(results) <= 5


def test_max_results_limits_results(tmp_path) -> None:
    for index in range(4):
        _save_loop(tmp_path, f"loop-{index}", f"shared vague topic {index}")

    results = search_memory_records("vague", trace_dir=tmp_path / "traces", max_results=2)

    assert len(results) == 2


def test_results_are_deterministically_ordered_by_token_count_then_stable_fields(tmp_path) -> None:
    _append_record(tmp_path, "record-b", "2026-05-01T00:00:02+00:00", "vague")
    _append_record(tmp_path, "record-a", "2026-05-01T00:00:01+00:00", "vague section")

    results = search_memory_records("vague section", trace_dir=tmp_path / "traces", max_results=5)

    assert [result["source_record_id"] for result in results] == ["record-a", "record-b"]
    assert results[0]["match_token_count"] == 2
    assert results[1]["match_token_count"] == 1


def test_duplicate_source_record_ids_are_not_returned(tmp_path) -> None:
    _append_record(tmp_path, "duplicate-1", "2026-05-01T00:00:01+00:00", "vague")
    _append_record(tmp_path, "duplicate-1", "2026-05-01T00:00:02+00:00", "vague")

    results = search_memory_records("vague", trace_dir=tmp_path / "traces")

    assert [result["source_record_id"] for result in results] == ["duplicate-1"]


def test_loop_id_filtering_works(tmp_path) -> None:
    _save_loop(tmp_path, "loop-a", "alpha topic")
    _save_loop(tmp_path, "loop-b", "beta topic")

    results = search_memory_records("topic", trace_dir=tmp_path / "traces", loop_id="loop-b")

    assert results
    assert all(result["loop_id"] == "loop-b" for result in results)


def test_retrieval_results_include_source_record_ids(tmp_path) -> None:
    _save_loop(tmp_path, "loop-1", "the section is vague")

    results = search_memory_records("vague", trace_dir=tmp_path / "traces")

    assert all(result["source_record_id"] for result in results)


def test_cli_memory_search_works(tmp_path) -> None:
    _run_cli("run-once", "the section is vague", "--save", cwd=tmp_path)

    result = _run_cli("memory-search", "vague", cwd=tmp_path)

    assert result.returncode == 0
    parsed = json.loads(result.stdout)
    assert parsed
    assert any(match["source_record_id"] for match in parsed)


def test_cli_memory_search_max_results_limits_results(tmp_path) -> None:
    for index in range(4):
        _run_cli("run-once", f"shared vague topic {index}", "--save", cwd=tmp_path)

    result = _run_cli("memory-search", "vague", "--max-results", "2", cwd=tmp_path)

    assert result.returncode == 0
    assert len(json.loads(result.stdout)) == 2


def test_cli_memory_search_handles_missing_traces_gracefully(tmp_path) -> None:
    result = _run_cli("memory-search", "vague", cwd=tmp_path)

    assert result.returncode == 0
    assert json.loads(result.stdout) == []


def _save_loop(tmp_path, loop_id, manual_text):
    result = run_manual_text_loop(
        manual_text,
        BeliefStateRecord(id=f"belief-{loop_id}"),
        boundary_config=_boundary_config(tmp_path),
        loop_id=loop_id,
    )
    save_loop_result_jsonl(result, trace_dir=tmp_path / "traces")


def _append_record(tmp_path, record_id, created_at, payload):
    trace_dir = tmp_path / "traces"
    trace_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "id": record_id,
        "record_type": "SignalRecord",
        "created_at": created_at,
        "created_by": "test",
        "loop_id": "loop-test",
        "status": "created",
        "source_refs": [],
        "uncertainty": [],
        "payload": payload,
    }
    with (trace_dir / "events.jsonl").open("a", encoding="utf-8") as trace_file:
        trace_file.write(json.dumps(record) + "\n")


def _boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }


def _run_cli(*args, cwd=None):
    repo_root = Path(__file__).resolve().parents[1]
    env = {
        **os.environ,
        "PYTHONPATH": str(repo_root / "src"),
    }
    return subprocess.run(
        [sys.executable, "-m", "bpm_runtime.main", *args],
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
