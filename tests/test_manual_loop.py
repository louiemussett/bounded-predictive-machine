from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    LoopRecord,
    MemoryTraceRecord,
    NoActionRecord,
)


def make_boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }


def test_running_one_complete_manual_loop(tmp_path) -> None:
    prior_belief = BeliefStateRecord(id="belief-1")

    result = run_manual_text_loop(
        "bounded input",
        prior_belief,
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    assert result["prediction"].record_type == "PredictionRecord"
    assert result["signal"].record_type == "SignalRecord"
    assert result["interpretation"].record_type == "InterpretationRecord"
    assert result["evidence"].record_type == "EvidenceQualityRecord"
    assert result["belief_result"].record_type == "BeliefUpdateRecord"
    assert isinstance(result["action_result"], ActionCandidateRecord)
    assert result["safety_check"].record_type == "SafetyCheckRecord"
    assert result["outcome"].record_type == "OutcomeRecord"
    assert isinstance(result["memory_trace"], MemoryTraceRecord)
    assert isinstance(result["loop_record"], LoopRecord)


def test_returning_expected_record_keys(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
    )

    assert set(result) == {
        "prediction",
        "signal",
        "interpretation",
        "evidence",
        "belief_result",
        "action_result",
        "safety_check",
        "outcome",
        "memory_trace",
        "loop_record",
    }


def test_preserving_same_loop_id_across_records(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    for record in result.values():
        if record is not None:
            assert record.loop_id == "loop-1"


def test_no_action_for_empty_or_unclear_text(tmp_path) -> None:
    empty_result = run_manual_text_loop(
        "   ",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-empty",
    )
    unclear_result = run_manual_text_loop(
        "???",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-unclear",
    )

    assert isinstance(empty_result["action_result"], NoActionRecord)
    assert empty_result["safety_check"] is None
    assert isinstance(unclear_result["action_result"], NoActionRecord)
    assert unclear_result["safety_check"] is None


def test_memory_trace_references_upstream_records(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    memory_trace = result["memory_trace"]

    assert result["prediction"].id in memory_trace.referenced_record_ids
    assert result["signal"].id in memory_trace.referenced_record_ids
    assert result["outcome"].id in memory_trace.referenced_record_ids


def test_loop_record_references_ordered_chain(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    ordered_ids = result["loop_record"].ordered_record_ids

    assert ordered_ids == [
        result["prediction"].id,
        result["signal"].id,
        result["interpretation"].id,
        result["evidence"].id,
        result["belief_result"].id,
        result["action_result"].id,
        result["safety_check"].id,
        result["outcome"].id,
        result["memory_trace"].id,
    ]


def test_no_files_are_written_during_orchestration(tmp_path) -> None:
    target_path = tmp_path / "state" / "current.json"

    run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    assert not target_path.exists()
