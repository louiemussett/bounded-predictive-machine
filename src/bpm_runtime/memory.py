"""Memory trace reconstruction for the first-build runtime."""

from __future__ import annotations

from typing import Any, Iterable

from bpm_runtime.records import MemoryTraceRecord


def create_memory_trace(
    records: Iterable[Any],
    loop_id: str | None = None,
    summary: str | None = None,
) -> MemoryTraceRecord:
    """Create a memory trace from upstream record references."""

    record_list = list(records)
    referenced_ids = _record_ids(record_list)
    uncertainty = _carried_uncertainty(record_list)

    return MemoryTraceRecord(
        created_by="bpm_runtime.memory",
        loop_id=loop_id or _first_loop_id(record_list),
        source_refs=referenced_ids,
        referenced_record_ids=referenced_ids,
        reconstruction_summary=summary or _default_summary(record_list, referenced_ids),
        uncertainty=uncertainty,
    )


def _record_ids(records: list[Any]) -> list[str]:
    ids = []
    for record in records:
        record_id = getattr(record, "id", None)
        if record_id:
            ids.append(record_id)
    return ids


def _carried_uncertainty(records: list[Any]) -> list[str]:
    uncertainty: list[str] = []
    for record in records:
        uncertainty.extend(getattr(record, "uncertainty", []) or [])
    return list(dict.fromkeys(uncertainty))


def _first_loop_id(records: list[Any]) -> str | None:
    for record in records:
        loop_id = getattr(record, "loop_id", None)
        if loop_id:
            return loop_id
    return None


def _default_summary(records: list[Any], referenced_ids: list[str]) -> str:
    if not referenced_ids:
        return "memory trace created with no referenced records"

    record_types = [getattr(record, "record_type", record.__class__.__name__) for record in records]
    return "memory trace reconstructs records: " + ", ".join(record_types)
