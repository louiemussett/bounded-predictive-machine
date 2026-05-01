from bpm_runtime.belief import apply_belief_update
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    BeliefUpdateRecord,
    EvidenceQualityRecord,
    NoUpdateRecord,
)


def make_evidence(quality_label, evidence_id="evidence-1"):
    return EvidenceQualityRecord(
        id=evidence_id,
        quality_label=quality_label,
        update_targets=["manual_text_signal"],
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
    assert update.no_update_reason == "no update: evidence quality is low"


def test_inconclusive_evidence_creates_no_update_record() -> None:
    belief = BeliefStateRecord(id="belief-1")
    evidence = make_evidence("inconclusive")

    update = apply_belief_update(belief, evidence)

    assert isinstance(update, NoUpdateRecord)
    assert update.no_update_reason == "no update: evidence quality is inconclusive"


def test_missing_evidence_creates_no_update_record() -> None:
    belief = BeliefStateRecord(id="belief-1")

    update = apply_belief_update(belief, None)

    assert isinstance(update, NoUpdateRecord)
    assert update.no_update_reason == "no update: evidence quality is missing"
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
