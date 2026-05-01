from bpm_runtime.belief import apply_belief_update
from bpm_runtime.evidence import assess_evidence_quality
from bpm_runtime.interpretation import interpret_signal
from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.prediction import create_prediction
from bpm_runtime.records import BeliefStateRecord, BeliefUpdateRecord, NoActionRecord, NoUpdateRecord
from bpm_runtime.report import loop_result_to_summary
from bpm_runtime.signals import create_manual_text_signal


def test_scored_evidence_is_deterministic() -> None:
    first = _evidence_for("bounded input", "bounded input")
    second = _evidence_for("bounded input", "bounded input")

    assert first.evidence_score == second.evidence_score
    assert first.score_components == second.score_components


def test_score_ordering_high_medium_low_inconclusive() -> None:
    high = _evidence_for("bounded input", "bounded input")
    medium = _evidence_for("different input", "bounded input")
    low = _evidence_for("???", "bounded input")
    inconclusive = _evidence_for("   ", "bounded input")

    assert high.quality_label == "high"
    assert medium.quality_label == "medium"
    assert low.quality_label == "low"
    assert inconclusive.quality_label == "inconclusive"
    assert high.evidence_score > medium.evidence_score
    assert medium.evidence_score > low.evidence_score
    assert low.evidence_score > inconclusive.evidence_score


def test_uncertainty_penalties_reduce_score() -> None:
    clear = _evidence_for("different input", "bounded input")
    unclear = _evidence_for("???", "bounded input")

    assert unclear.evidence_score < clear.evidence_score
    assert unclear.score_components["uncertainty_penalty"] > 0


def test_inconclusive_remains_below_update_threshold() -> None:
    evidence = _evidence_for("   ", "bounded input")

    assert evidence.evidence_score < evidence.update_threshold


def test_belief_update_includes_confidence_fields_when_update_happens() -> None:
    evidence = _evidence_for("bounded input", "bounded input")

    belief_result = apply_belief_update(BeliefStateRecord(id="belief-1"), evidence)

    assert isinstance(belief_result, BeliefUpdateRecord)
    assert belief_result.prior_confidence == 0.5
    assert belief_result.posterior_confidence is not None
    assert belief_result.confidence_delta is not None
    assert belief_result.confidence_delta > 0
    assert belief_result.evidence_score == evidence.evidence_score


def test_no_update_includes_score_reason_when_update_does_not_happen() -> None:
    evidence = _evidence_for("   ", "bounded input")

    belief_result = apply_belief_update(BeliefStateRecord(id="belief-1"), evidence)

    assert isinstance(belief_result, NoUpdateRecord)
    assert "score below threshold" in belief_result.no_update_reason
    assert belief_result.evidence_score == evidence.evidence_score
    assert belief_result.confidence_delta == 0.0


def test_abstention_still_blocks_action_for_low_or_inconclusive_evidence(tmp_path) -> None:
    low_result = run_manual_text_loop(
        "???",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-low",
    )
    inconclusive_result = run_manual_text_loop(
        "   ",
        BeliefStateRecord(id="belief-2"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-inconclusive",
    )

    assert low_result["uncertainty_gate"].decision == "abstain"
    assert isinstance(low_result["action_result"], NoActionRecord)
    assert inconclusive_result["uncertainty_gate"].decision == "abstain"
    assert isinstance(inconclusive_result["action_result"], NoActionRecord)


def test_report_summary_includes_scores(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    summary = loop_result_to_summary(result)

    assert "Evidence score:" in summary
    assert "(threshold: 0.6)" in summary


def _evidence_for(signal_text, expected):
    prediction = create_prediction(
        BeliefStateRecord(id="belief-1"),
        "manual_text_signal",
        expected,
        loop_id="loop-1",
    )
    signal = create_manual_text_signal(signal_text, loop_id="loop-1")
    interpretation = interpret_signal(signal, prediction, loop_id="loop-1")
    return assess_evidence_quality(signal, interpretation, prediction, loop_id="loop-1")


def _boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }
