from bpm_runtime.memory import create_memory_trace
from bpm_runtime.records import BeliefUpdateRecord, MemoryTraceRecord, SignalRecord


def test_creating_memory_trace_record() -> None:
    signal = SignalRecord(id="signal-1")

    memory = create_memory_trace([signal])

    assert isinstance(memory, MemoryTraceRecord)


def test_record_type_correctness() -> None:
    memory = create_memory_trace([])

    assert memory.record_type == "MemoryTraceRecord"


def test_referencing_upstream_records() -> None:
    signal = SignalRecord(id="signal-1")
    update = BeliefUpdateRecord(id="belief-update-1")

    memory = create_memory_trace([signal, update])

    assert memory.referenced_record_ids == ["signal-1", "belief-update-1"]
    assert memory.source_refs == ["signal-1", "belief-update-1"]


def test_preserving_or_carrying_forward_uncertainty() -> None:
    signal = SignalRecord(id="signal-1", uncertainty=["source clarity unresolved"])
    update = BeliefUpdateRecord(id="belief-update-1", uncertainty=["target scope narrow"])

    memory = create_memory_trace([signal, update])

    assert memory.uncertainty == ["source clarity unresolved", "target scope narrow"]


def test_using_provided_summary() -> None:
    signal = SignalRecord(id="signal-1")

    memory = create_memory_trace([signal], summary="manual signal was captured")

    assert memory.reconstruction_summary == "manual signal was captured"


def test_creating_default_summary_if_none_is_provided() -> None:
    signal = SignalRecord(id="signal-1")

    memory = create_memory_trace([signal])

    assert memory.reconstruction_summary == "memory trace reconstructs records: SignalRecord"


def test_memory_creation_does_not_update_belief_or_write_files(tmp_path) -> None:
    target_path = tmp_path / "memory.json"
    signal = SignalRecord(id="signal-1")

    memory = create_memory_trace([signal])

    assert isinstance(memory, MemoryTraceRecord)
    assert not isinstance(memory, BeliefUpdateRecord)
    assert not target_path.exists()
