"""Local JSONL memory retrieval without embeddings or LLMs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


TRACE_FILES = ["events.jsonl", "loops.jsonl", "memory.jsonl"]
SEARCH_FIELDS = [
    "payload",
    "payload_summary",
    "primary_interpretation",
    "update_summary",
    "no_update_reason",
    "reconstruction_summary",
    "reason",
    "observed_effect",
]


def load_trace_records(trace_dir: str | Path = "traces") -> list[dict[str, Any]]:
    """Load known JSONL trace files, returning an empty list for missing files."""

    trace_root = Path(trace_dir)
    records: list[dict[str, Any]] = []
    for file_name in TRACE_FILES:
        trace_path = trace_root / file_name
        if not trace_path.exists():
            continue
        records.extend(_load_jsonl(trace_path))
    return records


def search_memory_records(
    query: str | None = None,
    trace_dir: str | Path = "traces",
    record_type: str | None = None,
    loop_id: str | None = None,
) -> list[dict[str, Any]]:
    """Search local trace records by type, loop id, and simple keyword."""

    query_text = (query or "").strip().lower()
    results = []
    for record in load_trace_records(trace_dir):
        if record_type and record.get("record_type") != record_type:
            continue
        if loop_id and record.get("loop_id") != loop_id:
            continue

        matched_fields = _matched_fields(record, query_text)
        if query_text and not matched_fields:
            continue

        results.append(
            {
                "source_record_id": record.get("id"),
                "source_record_type": record.get("record_type"),
                "loop_id": record.get("loop_id"),
                "matched_fields": matched_fields,
                "record": record,
            }
        )
    return results


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def _matched_fields(record: dict[str, Any], query_text: str) -> list[str]:
    if not query_text:
        return []

    matches = []
    for field_name in SEARCH_FIELDS:
        value = record.get(field_name)
        if isinstance(value, str) and query_text in value.lower():
            matches.append(field_name)
    return matches
