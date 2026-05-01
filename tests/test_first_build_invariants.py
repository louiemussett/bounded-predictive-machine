from bpm_runtime.actions import create_action_candidate
from bpm_runtime.belief import apply_belief_update
from bpm_runtime.evidence import assess_evidence_quality
from bpm_runtime.interpretation import interpret_signal
from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.memory import create_memory_trace
from bpm_runtime.outcome import create_outcome
from bpm_runtime.prediction import create_prediction
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    BeliefUpdateRecord,
    LoopRecord,
    MemoryTraceRecord,
    NoActionRecord,
    NoUpdateRecord,
    OutcomeRecord,
    SignalRecord,
)
from bpm_runtime.safety import evaluate_action_safety
from bpm_runtime.signals import create_manual_text_signal


def make_boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }


def test_manual_signal_does_not_directly_become_belief_or_action() -> None:
    signal = create_manual_text_signal("bounded input")

    assert isinstance(signal, SignalRecord)
    assert not isinstance(signal, BeliefStateRecord)
    assert not isinstance(signal, BeliefUpdateRecord)
    assert not isinstance(signal, ActionCandidateRecord)


def test_manual_loop_orders_prediction_before_interpretation(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )
    ordered_ids = result["loop_record"].ordered_record_ids

    assert ordered_ids.index(result["prediction"].id) < ordered_ids.index(
        result["interpretation"].id
    )


def test_manual_loop_orders_evidence_before_belief_result(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )
    ordered_ids = result["loop_record"].ordered_record_ids

    assert ordered_ids.index(result["evidence"].id) < ordered_ids.index(
        result["belief_result"].id
    )


def test_low_or_inconclusive_evidence_produces_no_update_and_no_action(tmp_path) -> None:
    low_result = run_manual_text_loop(
        "???",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-low",
    )
    inconclusive_result = run_manual_text_loop(
        "   ",
        BeliefStateRecord(id="belief-2"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-inconclusive",
    )

    assert low_result["evidence"].quality_label == "low"
    assert isinstance(low_result["belief_result"], NoUpdateRecord)
    assert isinstance(low_result["action_result"], NoActionRecord)
    assert inconclusive_result["evidence"].quality_label == "inconclusive"
    assert isinstance(inconclusive_result["belief_result"], NoUpdateRecord)
    assert isinstance(inconclusive_result["action_result"], NoActionRecord)


def test_action_candidate_without_expected_effect_is_uncertain_and_blocked(tmp_path) -> None:
    candidate = create_action_candidate(
        BeliefUpdateRecord(id="belief-update-1"),
        action_name="write_file",
        expected_effect=None,
        target_path=str(tmp_path / "state" / "current.json"),
    )

    safety_check = evaluate_action_safety(candidate, make_boundary_config(tmp_path))

    assert candidate.uncertainty == ["expected effect is missing"]
    assert safety_check.status == "blocked"
    assert any("expected effect is missing" in item for item in safety_check.uncertainty)


def test_source_documents_and_unknown_write_targets_are_rejected(tmp_path) -> None:
    boundary_config = make_boundary_config(tmp_path)
    source_docs_candidate = create_action_candidate(
        BeliefUpdateRecord(id="belief-update-1"),
        action_name="write_file",
        expected_effect="write protected source material",
        target_path=str(tmp_path / "Source Documents" / "0. White Paper.md"),
    )
    unknown_candidate = create_action_candidate(
        BeliefUpdateRecord(id="belief-update-2"),
        action_name="write_file",
        expected_effect="write unknown file",
        target_path=str(tmp_path / "unknown" / "file.json"),
    )

    source_docs_check = evaluate_action_safety(source_docs_candidate, boundary_config)
    unknown_check = evaluate_action_safety(unknown_candidate, boundary_config)

    assert source_docs_check.status == "blocked"
    assert unknown_check.status == "blocked"


def test_outcome_is_separate_from_action_or_no_action_record() -> None:
    no_action = NoActionRecord(id="no-action-1", reason="wait")

    outcome = create_outcome(no_action, observed_effect="nothing changed", success=True)

    assert isinstance(outcome, OutcomeRecord)
    assert not isinstance(outcome, NoActionRecord)
    assert outcome.action_ref == "no-action-1"


def test_memory_trace_references_upstream_records_instead_of_replacing_them() -> None:
    signal = create_manual_text_signal("bounded input")
    prediction = create_prediction(None, "manual_text_signal", "bounded input")
    interpretation = interpret_signal(signal, prediction)
    evidence = assess_evidence_quality(signal, interpretation, prediction)
    belief_result = apply_belief_update(BeliefStateRecord(id="belief-1"), evidence)

    memory_trace = create_memory_trace([signal, prediction, interpretation, evidence, belief_result])

    assert isinstance(memory_trace, MemoryTraceRecord)
    assert memory_trace.referenced_record_ids == [
        signal.id,
        prediction.id,
        interpretation.id,
        evidence.id,
        belief_result.id,
    ]
    assert signal.payload == "bounded input"


def test_loop_record_links_full_ordered_chain(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=make_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    assert isinstance(result["loop_record"], LoopRecord)
    assert result["loop_record"].ordered_record_ids == [
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


def test_run_manual_text_loop_writes_no_files(tmp_path) -> None:
    boundary_config = make_boundary_config(tmp_path)

    run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=boundary_config,
        loop_id="loop-1",
    )

    assert not (tmp_path / "state" / "current.json").exists()
    assert not (tmp_path / "traces" / "loop.jsonl").exists()
