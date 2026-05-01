import json
import os
from pathlib import Path
import subprocess
import sys

from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import BeliefStateRecord, NoActionRecord
from bpm_runtime.report import loop_result_to_summary
from bpm_runtime.trace import save_loop_result_jsonl


def test_run_once_without_use_memory_does_not_retrieve_memory(tmp_path) -> None:
    _save_prior_loop(tmp_path, "the section is vague")

    result = run_manual_text_loop(
        "vague",
        BeliefStateRecord(id="belief-2"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-2",
        trace_dir=str(tmp_path / "traces"),
    )

    assert result["memory_retrieval"] is None
    assert "MemoryRetrievalRecord" not in result["loop_record"].record_types


def test_run_once_with_use_memory_includes_retrieval_result(tmp_path) -> None:
    _save_prior_loop(tmp_path, "the section is vague")

    result = run_manual_text_loop(
        "vague",
        BeliefStateRecord(id="belief-2"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-2",
        use_memory=True,
        trace_dir=str(tmp_path / "traces"),
    )

    assert result["memory_retrieval"].record_type == "MemoryRetrievalRecord"
    assert result["memory_retrieval"].match_count > 0
    assert result["memory_retrieval"].matched_record_ids


def test_loop_record_includes_memory_retrieval_when_used(tmp_path) -> None:
    _save_prior_loop(tmp_path, "the section is vague")

    result = run_manual_text_loop(
        "vague",
        BeliefStateRecord(id="belief-2"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-2",
        use_memory=True,
        trace_dir=str(tmp_path / "traces"),
    )

    assert "MemoryRetrievalRecord" in result["loop_record"].record_types
    assert result["memory_retrieval"].id in result["loop_record"].ordered_record_ids


def test_summary_mentions_retrieved_memory_count_or_no_matches(tmp_path) -> None:
    result = run_manual_text_loop(
        "vague",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
        use_memory=True,
        trace_dir=str(tmp_path / "missing-traces"),
    )

    summary = loop_result_to_summary(result)

    assert "Memory retrieval: 0 match(es)" in summary


def test_missing_traces_with_use_memory_does_not_crash(tmp_path) -> None:
    result = run_manual_text_loop(
        "vague",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
        use_memory=True,
        trace_dir=str(tmp_path / "missing-traces"),
    )

    assert result["memory_retrieval"].match_count == 0
    assert result["memory_retrieval"].uncertainty == ["no prior memory matches found"]


def test_retrieved_memory_does_not_force_belief_update_or_action(tmp_path) -> None:
    _save_prior_loop(tmp_path, "the section is unclear")

    result = run_manual_text_loop(
        "unclear",
        BeliefStateRecord(id="belief-2"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-2",
        use_memory=True,
        trace_dir=str(tmp_path / "traces"),
    )

    assert result["memory_retrieval"].match_count > 0
    assert result["belief_result"].record_type == "NoUpdateRecord"
    assert isinstance(result["action_result"], NoActionRecord)


def test_cli_run_once_use_memory_works(tmp_path) -> None:
    _run_cli("run-once", "the section is vague", "--save", cwd=tmp_path)

    result = _run_cli("run-once", "vague", "--use-memory", "--summary", cwd=tmp_path)

    assert result.returncode == 0
    assert "Memory retrieval:" in result.stdout


def test_cli_run_once_use_memory_json_includes_retrieval(tmp_path) -> None:
    _run_cli("run-once", "the section is vague", "--save", cwd=tmp_path)

    result = _run_cli("run-once", "vague", "--use-memory", cwd=tmp_path)

    parsed = json.loads(result.stdout)
    assert parsed["memory_retrieval"]["record_type"] == "MemoryRetrievalRecord"


def test_run_once_use_memory_max_results_limits_retrieval(tmp_path) -> None:
    for index in range(4):
        _save_prior_loop(tmp_path, f"shared vague topic {index}")

    result = run_manual_text_loop(
        "vague",
        BeliefStateRecord(id="belief-2"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-2",
        use_memory=True,
        trace_dir=str(tmp_path / "traces"),
        memory_max_results=2,
    )

    assert result["memory_retrieval"].match_count == 2
    assert len(result["memory_retrieval"].matched_record_ids) == 2


def test_cli_run_once_use_memory_max_results_limits_retrieval(tmp_path) -> None:
    for index in range(4):
        _run_cli("run-once", f"shared vague topic {index}", "--save", cwd=tmp_path)

    result = _run_cli(
        "run-once",
        "vague",
        "--use-memory",
        "--memory-max-results",
        "2",
        cwd=tmp_path,
    )

    parsed = json.loads(result.stdout)
    assert parsed["memory_retrieval"]["match_count"] == 2
    assert len(parsed["memory_retrieval"]["matched_record_ids"]) == 2


def _save_prior_loop(tmp_path, manual_text):
    result = run_manual_text_loop(
        manual_text,
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
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
