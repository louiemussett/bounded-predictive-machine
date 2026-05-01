import json

from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import BeliefStateRecord
from bpm_runtime.report import loop_result_to_json, loop_result_to_summary


def test_loop_result_to_json_contains_expected_record_keys(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    rendered = json.loads(loop_result_to_json(result))

    assert set(rendered) == {
        "prediction",
        "signal",
        "memory_retrieval",
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


def test_summary_uses_record_contents_and_requires_no_llm(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    summary = loop_result_to_summary(result)

    assert "Prediction: manual text signal may contain feedback" in summary
    assert "Signal: bounded input" in summary
    assert "Interpretation: manual text signal states: bounded input" in summary
    assert f"Memory trace: {result['memory_trace'].reconstruction_summary}" in summary


def test_summary_reports_remaining_uncertainty(tmp_path) -> None:
    result = run_manual_text_loop(
        "???",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    summary = loop_result_to_summary(result)

    assert "Remaining uncertainty:" in summary
    assert "signal meaning is unclear" in summary


def _boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }
