import json

from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefStateRecord,
    BeliefUpdateRecord,
    BlockedActionRecord,
    BodyStateRecord,
    EvidenceQualityRecord,
    InterpretationRecord,
    LoopRecord,
    MemoryTraceRecord,
    NoActionRecord,
    NoUpdateRecord,
    OutcomeRecord,
    PredictionRecord,
    SafetyCheckRecord,
    SelectedActionRecord,
    SignalRecord,
    UncertaintyRecord,
    ViabilityRecord,
)


RECORD_CLASSES = [
    BodyStateRecord,
    ViabilityRecord,
    BeliefStateRecord,
    PredictionRecord,
    SignalRecord,
    InterpretationRecord,
    EvidenceQualityRecord,
    BeliefUpdateRecord,
    NoUpdateRecord,
    ActionCandidateRecord,
    SafetyCheckRecord,
    SelectedActionRecord,
    NoActionRecord,
    BlockedActionRecord,
    OutcomeRecord,
    MemoryTraceRecord,
    UncertaintyRecord,
    LoopRecord,
]


def test_record_creation() -> None:
    record = BodyStateRecord(created_by="test", loop_id="loop-1")

    assert record.id
    assert record.created_at
    assert record.created_by == "test"
    assert record.loop_id == "loop-1"
    assert record.status == "created"


def test_record_type_correctness() -> None:
    for record_class in RECORD_CLASSES:
        record = record_class()

        assert record.record_type == record_class.__name__


def test_serialization_to_dict() -> None:
    record = PredictionRecord(
        id="prediction-1",
        created_at="2026-05-01T00:00:00+00:00",
        created_by="test",
        loop_id="loop-1",
        status="created",
        source_refs=["belief-1"],
        uncertainty=["manual signal not yet observed"],
    )

    assert record.to_dict() == {
        "id": "prediction-1",
        "record_type": "PredictionRecord",
        "created_at": "2026-05-01T00:00:00+00:00",
        "created_by": "test",
        "loop_id": "loop-1",
        "status": "created",
        "source_refs": ["belief-1"],
        "uncertainty": ["manual signal not yet observed"],
    }


def test_serialization_to_json() -> None:
    record = SignalRecord(id="signal-1", created_at="2026-05-01T00:00:00+00:00")

    assert json.loads(record.to_json()) == record.to_dict()


def test_source_refs_default_safely() -> None:
    first = InterpretationRecord()
    second = InterpretationRecord()

    first.source_refs.append("signal-1")

    assert first.source_refs == ["signal-1"]
    assert second.source_refs == []


def test_uncertainty_defaults_safely() -> None:
    first = EvidenceQualityRecord()
    second = EvidenceQualityRecord()

    first.uncertainty.append("source reliability unresolved")

    assert first.uncertainty == ["source reliability unresolved"]
    assert second.uncertainty == []
