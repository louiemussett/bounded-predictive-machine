"""Local JSONL memory retrieval without embeddings or LLMs."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from bpm_runtime.records import MemoryRetrievalRecord


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
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "is",
    "it",
    "of",
    "or",
    "the",
    "to",
}


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

    query_tokens = _query_tokens(query)
    results = []
    for record in load_trace_records(trace_dir):
        if record_type and record.get("record_type") != record_type:
            continue
        if loop_id and record.get("loop_id") != loop_id:
            continue

        matched_fields = _matched_fields(record, query_tokens)
        if query_tokens and not matched_fields:
            continue
        if query and not query_tokens:
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


def create_memory_retrieval_record(
    query: str | None,
    results: list[dict[str, Any]],
    loop_id: str | None = None,
) -> MemoryRetrievalRecord:
    """Create a record that summarizes local memory retrieval results."""

    matched_record_ids = [
        result["source_record_id"]
        for result in results
        if result.get("source_record_id")
    ]
    uncertainty = []
    if not results:
        uncertainty.append("no prior memory matches found")

    return MemoryRetrievalRecord(
        created_by="bpm_runtime.retrieval",
        loop_id=loop_id,
        source_refs=matched_record_ids,
        query=query,
        match_count=len(results),
        matched_record_ids=matched_record_ids,
        uncertainty=uncertainty,
    )


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def _query_tokens(query: str | None) -> list[str]:
    tokens = []
    for token in re.findall(r"[A-Za-z0-9]+", (query or "").lower()):
        if len(token) <= 2:
            continue
        if token in STOPWORDS:
            continue
        tokens.append(token)
    return list(dict.fromkeys(tokens))


def _matched_fields(record: dict[str, Any], query_tokens: list[str]) -> list[str]:
    if not query_tokens:
        return []

    matches = []
    for field_name in SEARCH_FIELDS:
        value = record.get(field_name)
        if isinstance(value, str) and _field_matches(value, query_tokens):
            matches.append(field_name)
    return matches


def _field_matches(value: str, query_tokens: list[str]) -> bool:
    field_text = value.lower()
    return any(token in field_text for token in query_tokens)
