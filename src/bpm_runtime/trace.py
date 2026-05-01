"""JSONL trace helpers for the first-build runtime."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


LOOP_RECORD_TYPE = "LoopRecord"
MEMORY_TRACE_RECORD_TYPE = "MemoryTraceRecord"


def append_jsonl_record(path: str | Path, record: Any) -> None:
    """Append one record to a JSONL trace file.

    The first build accepts either runtime records with ``to_dict()`` or plain
    dictionaries. Each call writes exactly one JSON object followed by a
    newline.
    """

    trace_path = Path(path)
    trace_path.parent.mkdir(parents=True, exist_ok=True)

    payload = _record_to_dict(record)
    with trace_path.open("a", encoding="utf-8") as trace_file:
        json.dump(payload, trace_file, sort_keys=True)
        trace_file.write("\n")


def save_loop_result_jsonl(
    loop_result: Mapping[str, Any],
    trace_dir: str | Path = "traces",
) -> dict[str, Path]:
    """Persist one loop result to simple JSONL trace files."""

    trace_root = Path(trace_dir)
    paths = {
        "events": trace_root / "events.jsonl",
        "loops": trace_root / "loops.jsonl",
        "memory": trace_root / "memory.jsonl",
    }

    for record in loop_result.values():
        if record is None:
            continue

        record_type = _record_type(record)
        if record_type == LOOP_RECORD_TYPE:
            append_jsonl_record(paths["loops"], record)
        elif record_type == MEMORY_TRACE_RECORD_TYPE:
            append_jsonl_record(paths["memory"], record)
        else:
            append_jsonl_record(paths["events"], record)

    return paths


def _record_to_dict(record: Any) -> dict[str, Any]:
    if hasattr(record, "to_dict"):
        payload = record.to_dict()
    else:
        payload = record

    if not isinstance(payload, Mapping):
        raise TypeError("record must be a mapping or provide to_dict()")

    return dict(payload)


def _record_type(record: Any) -> str | None:
    if hasattr(record, "record_type"):
        return record.record_type
    if isinstance(record, Mapping):
        return record.get("record_type")
    return None
