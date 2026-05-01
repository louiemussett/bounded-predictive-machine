import json
import os
from pathlib import Path
import subprocess
import sys


def test_cli_run_once_exits_successfully() -> None:
    result = _run_cli("bounded input")

    assert result.returncode == 0


def test_cli_output_is_valid_json_by_default() -> None:
    result = _run_cli("bounded input")

    parsed = json.loads(result.stdout)

    assert parsed["prediction"]["record_type"] == "PredictionRecord"
    assert parsed["signal"]["record_type"] == "SignalRecord"


def test_cli_output_includes_expected_record_keys() -> None:
    result = _run_cli("bounded input")

    parsed = json.loads(result.stdout)

    assert set(parsed) == {
        "prediction",
        "signal",
        "interpretation",
        "evidence",
        "uncertainty_gate",
        "belief_result",
        "abstention",
        "action_result",
        "safety_check",
        "outcome",
        "memory_trace",
        "loop_record",
    }


def test_cli_does_not_write_files(tmp_path) -> None:
    target_path = tmp_path / "state" / "current.json"

    result = _run_cli("bounded input", cwd=tmp_path)

    assert result.returncode == 0
    assert not target_path.exists()
    assert not (tmp_path / "traces" / "events.jsonl").exists()
    assert not (tmp_path / "traces" / "loops.jsonl").exists()
    assert not (tmp_path / "traces" / "memory.jsonl").exists()


def test_cli_save_writes_jsonl_trace_files(tmp_path) -> None:
    result = _run_cli("bounded input", "--save", cwd=tmp_path)

    assert result.returncode == 0
    assert (tmp_path / "traces" / "events.jsonl").exists()
    assert (tmp_path / "traces" / "loops.jsonl").exists()
    assert (tmp_path / "traces" / "memory.jsonl").exists()


def test_cli_saved_jsonl_lines_are_valid_json(tmp_path) -> None:
    result = _run_cli("bounded input", "--save", cwd=tmp_path)

    assert result.returncode == 0
    for trace_file in [
        tmp_path / "traces" / "events.jsonl",
        tmp_path / "traces" / "loops.jsonl",
        tmp_path / "traces" / "memory.jsonl",
    ]:
        for line in trace_file.read_text(encoding="utf-8").splitlines():
            assert isinstance(json.loads(line), dict)


def test_cli_save_routes_records_by_type(tmp_path) -> None:
    result = _run_cli("bounded input", "--save", cwd=tmp_path)

    assert result.returncode == 0
    event_records = _read_jsonl(tmp_path / "traces" / "events.jsonl")
    loop_records = _read_jsonl(tmp_path / "traces" / "loops.jsonl")
    memory_records = _read_jsonl(tmp_path / "traces" / "memory.jsonl")

    assert all(record["record_type"] != "LoopRecord" for record in event_records)
    assert all(record["record_type"] != "MemoryTraceRecord" for record in event_records)
    assert [record["record_type"] for record in loop_records] == ["LoopRecord"]
    assert [record["record_type"] for record in memory_records] == ["MemoryTraceRecord"]


def test_cli_save_never_writes_source_documents(tmp_path) -> None:
    source_documents = tmp_path / "Source Documents"

    result = _run_cli("bounded input", "--save", cwd=tmp_path)

    assert result.returncode == 0
    assert not source_documents.exists()


def test_cli_summary_output_is_human_readable() -> None:
    result = _run_cli("bounded input", "--summary")

    assert result.returncode == 0
    assert "Prediction:" in result.stdout
    assert "Signal: bounded input" in result.stdout
    assert "Evidence quality:" in result.stdout
    assert "Memory trace:" in result.stdout


def _run_cli(manual_text, *extra_args, cwd=None):
    repo_root = Path(__file__).resolve().parents[1]
    env = {
        **os.environ,
        "PYTHONPATH": str(repo_root / "src"),
    }
    command = [
        sys.executable,
        "-m",
        "bpm_runtime.main",
        "run-once",
        manual_text,
        *extra_args,
    ]
    return subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def _read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
