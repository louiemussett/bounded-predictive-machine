from bpm_runtime.prediction import create_prediction
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    BeliefUpdateRecord,
    InterpretationRecord,
    PredictionRecord,
    SignalRecord,
)


def test_creating_prediction_record() -> None:
    prediction = create_prediction(
        prior_belief=None,
        target="manual_text_signal",
        expected="operator provides bounded input",
    )

    assert isinstance(prediction, PredictionRecord)


def test_record_type_correctness() -> None:
    prediction = create_prediction(None, "manual_text_signal", "bounded input")

    assert prediction.record_type == "PredictionRecord"


def test_referencing_prior_belief_when_provided() -> None:
    prior_belief = BeliefStateRecord(id="belief-1")

    prediction = create_prediction(
        prior_belief,
        target="manual_text_signal",
        expected="bounded input",
    )

    assert prediction.source_refs == ["belief-1"]


def test_preserving_target_and_expected_fields() -> None:
    prediction = create_prediction(
        None,
        target="manual_text_signal",
        expected="bounded input",
        loop_id="loop-1",
    )

    assert prediction.target == "manual_text_signal"
    assert prediction.expected == "bounded input"
    assert prediction.loop_id == "loop-1"
    assert prediction.match_conditions == [
        "manual_text_signal matches expected value: bounded input"
    ]


def test_adding_uncertainty_when_target_or_expected_is_missing() -> None:
    prediction = create_prediction(None, target=None, expected=None)

    assert prediction.uncertainty == [
        "prediction target is missing",
        "expected signal, state, or outcome is missing",
    ]
    assert prediction.match_conditions == []


def test_prediction_creation_does_not_require_a_signal() -> None:
    prediction = create_prediction(None, "manual_text_signal", "bounded input")

    assert isinstance(prediction, PredictionRecord)
    assert not isinstance(prediction, SignalRecord)
    assert not isinstance(prediction, InterpretationRecord)
    assert not isinstance(prediction, BeliefUpdateRecord)
    assert not isinstance(prediction, ActionCandidateRecord)
