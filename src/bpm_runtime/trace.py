"""JSONL trace helpers for the first-build runtime."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


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


def _record_to_dict(record: Any) -> dict[str, Any]:
    if hasattr(record, "to_dict"):
        payload = record.to_dict()
    else:
        payload = record

    if not isinstance(payload, Mapping):
        raise TypeError("record must be a mapping or provide to_dict()")

    return dict(payload)
