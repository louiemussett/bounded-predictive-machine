import json
import os
from pathlib import Path
import subprocess
import sys

from bpm_runtime.evidence import assess_evidence_quality
from bpm_runtime.interpretation import interpret_signal
from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import (
    AbstentionRecord,
    BeliefStateRecord,
    NoActionRecord,
    NoUpdateRecord,
    UncertaintyGateRecord,
)
from bpm_runtime.report import loop_result_to_summary
from bpm_runtime.signals import create_manual_text_signal
from bpm_runtime.uncertainty import create_abstention, evaluate_uncertainty_gate


def test_low_evidence_triggers_abstention_no_update_and_no_action(tmp_path) -> None:
    result = run_manual_text_loop(
        "???",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-low",
    )

    assert result["evidence"].quality_label == "low"
    assert isinstance(result["uncertainty_gate"], UncertaintyGateRecord)
    assert result["uncertainty_gate"].decision == "abstain"
    assert isinstance(result["abstention"], AbstentionRecord)
    assert isinstance(result["belief_result"], NoUpdateRecord)
    assert isinstance(result["action_result"], NoActionRecord)
    assert result["safety_check"] is None


def test_empty_input_triggers_abstention_result(tmp_path) -> None:
    result = run_manual_text_loop(
        "   ",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-empty",
    )

    assert result["evidence"].quality_label == "inconclusive"
    assert result["uncertainty_gate"].decision == "abstain"
    assert result["abstention"].record_type == "AbstentionRecord"
    assert result["abstention"].reason == (
        "not enough evidence: evidence quality is inconclusive"
    )
    assert isinstance(result["belief_result"], NoUpdateRecord)
    assert isinstance(result["action_result"], NoActionRecord)


def test_abstention_record_serializes_to_dict_and_json() -> None:
    signal = create_manual_text_signal("???", loop_id="loop-1")
    interpretation = interpret_signal(signal, loop_id="loop-1")
    evidence = assess_evidence_quality(signal, interpretation, loop_id="loop-1")
    gate = evaluate_uncertainty_gate(evidence, interpretation, loop_id="loop-1")

    abstention = create_abstention("not enough evidence", gate, loop_id="loop-1")

    assert abstention.to_dict()["record_type"] == "AbstentionRecord"
    assert json.loads(abstention.to_json()) == abstention.to_dict()


def test_summary_includes_abstention_reason(tmp_path) -> None:
    result = run_manual_text_loop(
        "???",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-low",
    )

    summary = loop_result_to_summary(result)

    assert "Abstention: not enough evidence: evidence quality is low" in summary
    assert "Action/no-action: evidence quality is low" in summary


def test_cli_summary_includes_abstention_reason() -> None:
    result = _run_cli("???", "--summary")

    assert result.returncode == 0
    assert "Abstention: not enough evidence: evidence quality is low" in result.stdout


def test_no_files_are_written_without_save(tmp_path) -> None:
    result = _run_cli("???", cwd=tmp_path)

    assert result.returncode == 0
    assert not (tmp_path / "traces").exists()


def _boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }


def _run_cli(manual_text, *extra_args, cwd=None):
    repo_root = Path(__file__).resolve().parents[1]
    env = {
        **os.environ,
        "PYTHONPATH": str(repo_root / "src"),
    }
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "bpm_runtime.main",
            "run-once",
            manual_text,
            *extra_args,
        ],
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
