from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    SignalRecord,
)
from bpm_runtime.signals import create_manual_text_signal


def test_creating_signal_record_from_manual_text() -> None:
    signal = create_manual_text_signal("operator provided a manual signal")

    assert isinstance(signal, SignalRecord)
    assert signal.source == "manual_text"
    assert signal.admissibility_status == "admissible_for_signal_capture"


def test_preserving_manual_text_or_safe_payload_summary() -> None:
    text = "create the next first-build runtime step"

    signal = create_manual_text_signal(text)

    assert signal.payload == text
    assert signal.payload_summary == text


def test_setting_record_type_correctly() -> None:
    signal = create_manual_text_signal("hello")

    assert signal.record_type == "SignalRecord"


def test_setting_loop_id_when_provided() -> None:
    signal = create_manual_text_signal("hello", loop_id="loop-1")

    assert signal.loop_id == "loop-1"


def test_not_creating_belief_or_action_records() -> None:
    signal = create_manual_text_signal("hello")

    assert isinstance(signal, SignalRecord)
    assert not isinstance(signal, BeliefStateRecord)
    assert not isinstance(signal, ActionCandidateRecord)
    assert signal.to_dict()["record_type"] == "SignalRecord"


def test_adding_uncertainty_for_empty_text() -> None:
    signal = create_manual_text_signal("   ")

    assert signal.payload == "   "
    assert signal.payload_summary == ""
    assert signal.uncertainty == ["manual text signal is empty"]
