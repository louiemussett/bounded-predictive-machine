from bpm_runtime.evidence import assess_evidence_quality
from bpm_runtime.interpretation import interpret_signal
from bpm_runtime.prediction import create_prediction
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    BeliefUpdateRecord,
    EvidenceQualityRecord,
)
from bpm_runtime.signals import create_manual_text_signal


def test_creating_evidence_quality_record() -> None:
    signal = create_manual_text_signal("bounded input")
    interpretation = interpret_signal(signal)

    evidence = assess_evidence_quality(signal, interpretation)

    assert isinstance(evidence, EvidenceQualityRecord)
    assert evidence.quality_label in {"high", "medium", "low", "inconclusive"}


def test_record_type_correctness() -> None:
    signal = create_manual_text_signal("bounded input")
    interpretation = interpret_signal(signal)

    evidence = assess_evidence_quality(signal, interpretation)

    assert evidence.record_type == "EvidenceQualityRecord"


def test_referencing_signal_and_interpretation() -> None:
    signal = create_manual_text_signal("bounded input")
    interpretation = interpret_signal(signal)

    evidence = assess_evidence_quality(signal, interpretation)

    assert evidence.source_refs == [signal.id, interpretation.id]


def test_referencing_prediction_when_provided() -> None:
    belief = BeliefStateRecord(id="belief-1")
    prediction = create_prediction(belief, "manual_text_signal", "bounded input")
    signal = create_manual_text_signal("bounded input")
    interpretation = interpret_signal(signal, prediction)

    evidence = assess_evidence_quality(signal, interpretation, prediction)

    assert evidence.source_refs == [signal.id, interpretation.id, prediction.id]
    assert evidence.prediction_result == "match"
    assert evidence.quality_label == "high"
    assert evidence.update_targets == ["manual_text_signal"]


def test_classifying_empty_or_unclear_signal_as_low_or_inconclusive() -> None:
    empty_signal = create_manual_text_signal("   ")
    empty_interpretation = interpret_signal(empty_signal)
    unclear_signal = create_manual_text_signal("???")
    unclear_interpretation = interpret_signal(unclear_signal)

    empty_evidence = assess_evidence_quality(empty_signal, empty_interpretation)
    unclear_evidence = assess_evidence_quality(unclear_signal, unclear_interpretation)

    assert empty_evidence.quality_label in {"low", "inconclusive"}
    assert unclear_evidence.quality_label in {"low", "inconclusive"}
    assert empty_evidence.prediction_result == "inconclusive"
    assert unclear_evidence.prediction_result == "inconclusive"


def test_not_creating_belief_or_action_records() -> None:
    signal = create_manual_text_signal("bounded input")
    interpretation = interpret_signal(signal)

    evidence = assess_evidence_quality(signal, interpretation)

    assert isinstance(evidence, EvidenceQualityRecord)
    assert not isinstance(evidence, BeliefStateRecord)
    assert not isinstance(evidence, BeliefUpdateRecord)
    assert not isinstance(evidence, ActionCandidateRecord)
