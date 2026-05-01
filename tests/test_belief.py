from bpm_runtime.belief import apply_belief_update
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    BeliefUpdateRecord,
    EvidenceQualityRecord,
    NoUpdateRecord,
)


def make_evidence(quality_label, evidence_id="evidence-1"):
    score_by_label = {
        "high": 0.9,
        "medium": 0.65,
        "low": 0.2,
        "inconclusive": 0.0,
    }
    return EvidenceQualityRecord(
        id=evidence_id,
        quality_label=quality_label,
        update_targets=["manual_text_signal"],
        evidence_score=score_by_label.get(quality_label),
        update_threshold=0.6,
        score_components={"reason": "test score"},
        uncertainty=["target scope remains narrow"],
    )


def test_high_evidence_creates_belief_update_record() -> None:
    belief = BeliefStateRecord(id="belief-1")
    evidence = make_evidence("high")

    update = apply_belief_update(belief, evidence)

    assert isinstance(update, BeliefUpdateRecord)
    assert update.evidence_quality_used == "high"
    assert update.update_target == "manual_text_signal"


def test_medium_evidence_creates_belief_update_record() -> None:
    belief = BeliefStateRecord(id="belief-1")
    evidence = make_evidence("medium")

    update = apply_belief_update(belief, evidence)

    assert isinstance(update, BeliefUpdateRecord)
    assert update.evidence_quality_used == "medium"


def test_low_evidence_creates_no_update_record() -> None:
    belief = BeliefStateRecord(id="belief-1")
    evidence = make_evidence("low")

    update = apply_belief_update(belief, evidence)

    assert isinstance(update, NoUpdateRecord)
    assert update.no_update_reason == (
        "no update: evidence quality is low; score below threshold "
        "(score=0.2, threshold=0.6)"
    )


def test_inconclusive_evidence_creates_no_update_record() -> None:
    belief = BeliefStateRecord(id="belief-1")
    evidence = make_evidence("inconclusive")

    update = apply_belief_update(belief, evidence)

    assert isinstance(update, NoUpdateRecord)
    assert update.no_update_reason == (
        "no update: evidence quality is inconclusive; score below threshold "
        "(score=0.0, threshold=0.6)"
    )


def test_missing_evidence_creates_no_update_record() -> None:
    belief = BeliefStateRecord(id="belief-1")

    update = apply_belief_update(belief, None)

    assert isinstance(update, NoUpdateRecord)
    assert update.no_update_reason == (
        "no update: evidence quality is missing (score=None, threshold=None)"
    )
    assert update.uncertainty == ["evidence quality is missing"]


def test_returned_record_references_prior_belief_and_evidence_quality() -> None:
    belief = BeliefStateRecord(id="belief-1")
    evidence = make_evidence("high", evidence_id="evidence-1")

    update = apply_belief_update(belief, evidence)

    assert update.source_refs == ["belief-1", "evidence-1"]


def test_no_action_records_are_created() -> None:
    belief = BeliefStateRecord(id="belief-1")
    evidence = make_evidence("high")

    update = apply_belief_update(belief, evidence)

    assert isinstance(update, BeliefUpdateRecord)
    assert not isinstance(update, ActionCandidateRecord)
