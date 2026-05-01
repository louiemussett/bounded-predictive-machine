from bpm_runtime.interpretation import interpret_signal
from bpm_runtime.prediction import create_prediction
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    BeliefUpdateRecord,
    InterpretationRecord,
)
from bpm_runtime.signals import create_manual_text_signal


def test_creating_interpretation_record_from_signal_record() -> None:
    signal = create_manual_text_signal("operator provided a bounded instruction")

    interpretation = interpret_signal(signal)

    assert isinstance(interpretation, InterpretationRecord)
    assert interpretation.primary_interpretation == (
        "manual text signal states: operator provided a bounded instruction"
    )


def test_record_type_correctness() -> None:
    signal = create_manual_text_signal("hello")

    interpretation = interpret_signal(signal)

    assert interpretation.record_type == "InterpretationRecord"


def test_referencing_the_signal() -> None:
    signal = create_manual_text_signal("hello")

    interpretation = interpret_signal(signal)

    assert interpretation.source_refs == [signal.id]


def test_referencing_prediction_when_provided() -> None:
    belief = BeliefStateRecord(id="belief-1")
    prediction = create_prediction(belief, "manual_text_signal", "bounded input")
    signal = create_manual_text_signal("bounded input")

    interpretation = interpret_signal(signal, prediction)

    assert interpretation.source_refs == [signal.id, prediction.id]
    assert interpretation.relevant_belief_targets == ["manual_text_signal"]


def test_not_creating_belief_or_action_records() -> None:
    signal = create_manual_text_signal("hello")

    interpretation = interpret_signal(signal)

    assert isinstance(interpretation, InterpretationRecord)
    assert not isinstance(interpretation, BeliefStateRecord)
    assert not isinstance(interpretation, BeliefUpdateRecord)
    assert not isinstance(interpretation, ActionCandidateRecord)


def test_adding_uncertainty_for_empty_or_unclear_signals() -> None:
    empty_signal = create_manual_text_signal("   ")
    unclear_signal = create_manual_text_signal("???")

    empty_interpretation = interpret_signal(empty_signal)
    unclear_interpretation = interpret_signal(unclear_signal)

    assert empty_interpretation.uncertainty == ["signal payload is empty or missing"]
    assert unclear_interpretation.uncertainty == ["signal meaning is unclear"]
    assert unclear_interpretation.alternative_interpretations == [
        "manual text may be incomplete",
        "manual text may require clarification",
    ]
