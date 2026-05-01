"""Loop record linking for already-created record chains."""

from __future__ import annotations

from typing import Any, Iterable

from bpm_runtime.records import LoopRecord


def create_loop_record(
    records: Iterable[Any],
    loop_id: str | None = None,
    status: str = "completed",
) -> LoopRecord:
    """Create a linker record for an existing loop chain."""

    record_list = list(records)
    ordered_record_ids = _record_ids(record_list)

    return LoopRecord(
        created_by="bpm_runtime.loop",
        loop_id=loop_id or _first_loop_id(record_list),
        status=status,
        source_refs=ordered_record_ids,
        ordered_record_ids=ordered_record_ids,
        record_types=_record_types(record_list),
        uncertainty=_carried_uncertainty(record_list),
    )


def _record_ids(records: list[Any]) -> list[str]:
    ids = []
    for record in records:
        record_id = getattr(record, "id", None)
        if record_id:
            ids.append(record_id)
    return ids


def _record_types(records: list[Any]) -> list[str]:
    return [getattr(record, "record_type", record.__class__.__name__) for record in records]


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
