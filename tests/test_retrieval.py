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
