from bpm_runtime.loop import create_loop_record
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefUpdateRecord,
    InterpretationRecord,
    LoopRecord,
    MemoryTraceRecord,
    PredictionRecord,
    SignalRecord,
)


def test_creating_loop_record() -> None:
    signal = SignalRecord(id="signal-1")

    loop = create_loop_record([signal])

    assert isinstance(loop, LoopRecord)


def test_record_type_correctness() -> None:
    loop = create_loop_record([])

    assert loop.record_type == "LoopRecord"


def test_preserving_ordered_record_ids() -> None:
    prediction = PredictionRecord(id="prediction-1")
    signal = SignalRecord(id="signal-1")
    interpretation = InterpretationRecord(id="interpretation-1")

    loop = create_loop_record([prediction, signal, interpretation])

    assert loop.ordered_record_ids == ["prediction-1", "signal-1", "interpretation-1"]
    assert loop.source_refs == ["prediction-1", "signal-1", "interpretation-1"]


def test_preserving_record_types() -> None:
    prediction = PredictionRecord(id="prediction-1")
    signal = SignalRecord(id="signal-1")

    loop = create_loop_record([prediction, signal])

    assert loop.record_types == ["PredictionRecord", "SignalRecord"]


def test_carrying_forward_uncertainty() -> None:
    prediction = PredictionRecord(id="prediction-1", uncertainty=["target unresolved"])
    signal = SignalRecord(id="signal-1", uncertainty=["source unclear"])

    loop = create_loop_record([prediction, signal])

    assert loop.uncertainty == ["target unresolved", "source unclear"]


def test_not_writing_files(tmp_path) -> None:
    target_path = tmp_path / "loop.json"
    signal = SignalRecord(id="signal-1")

    create_loop_record([signal])

    assert not target_path.exists()


def test_not_creating_new_cognitive_records_besides_loop_record() -> None:
    signal = SignalRecord(id="signal-1")

    loop = create_loop_record([signal])

    assert isinstance(loop, LoopRecord)
    assert not isinstance(loop, PredictionRecord)
    assert not isinstance(loop, SignalRecord)
    assert not isinstance(loop, InterpretationRecord)
    assert not isinstance(loop, BeliefUpdateRecord)
    assert not isinstance(loop, ActionCandidateRecord)
    assert not isinstance(loop, MemoryTraceRecord)
