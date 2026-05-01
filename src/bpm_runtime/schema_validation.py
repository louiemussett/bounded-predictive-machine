"""Lightweight JSON Schema validation for runtime records."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from jsonschema import validate


SCHEMA_FILES = {
    "PredictionRecord": "prediction_record.schema.json",
    "SignalRecord": "signal_record.schema.json",
    "InterpretationRecord": "interpretation_record.schema.json",
    "EvidenceQualityRecord": "evidence_quality_record.schema.json",
    "BeliefUpdateRecord": "belief_update_record.schema.json",
    "NoUpdateRecord": "no_update_record.schema.json",
    "ActionCandidateRecord": "action_candidate_record.schema.json",
    "NoActionRecord": "no_action_record.schema.json",
    "UncertaintyGateRecord": "uncertainty_gate_record.schema.json",
    "AbstentionRecord": "abstention_record.schema.json",
    "ClarificationRequestRecord": "clarification_request_record.schema.json",
    "SafetyCheckRecord": "safety_check_record.schema.json",
    "OutcomeRecord": "outcome_record.schema.json",
    "MemoryTraceRecord": "memory_trace_record.schema.json",
    "LoopRecord": "loop_record.schema.json",
}


def validate_record(record: Any, schema_dir: str | Path | None = None) -> None:
    """Validate a runtime record object against its record_type schema."""

    validate_record_dict(_record_to_dict(record), schema_dir=schema_dir)


def validate_record_dict(
    record: Mapping[str, Any],
    schema_dir: str | Path | None = None,
) -> None:
    """Validate a record dictionary against its matching JSON Schema."""

    record_type = record.get("record_type")
    if not isinstance(record_type, str):
        raise ValueError("record_type is required to select a schema")

    schema_file = SCHEMA_FILES.get(record_type)
    if schema_file is None:
        raise ValueError(f"no schema registered for record_type {record_type!r}")

    validate(instance=dict(record), schema=_load_schema(schema_file, schema_dir))


def _record_to_dict(record: Any) -> dict[str, Any]:
    if hasattr(record, "to_dict"):
        return record.to_dict()
    if isinstance(record, Mapping):
        return dict(record)
    raise TypeError("record must be a mapping or provide to_dict()")


def _load_schema(schema_file: str, schema_dir: str | Path | None) -> dict[str, Any]:
    root = Path(schema_dir) if schema_dir is not None else _default_schema_dir()
    with (root / schema_file).open("r", encoding="utf-8") as schema_handle:
        return json.load(schema_handle)


def _default_schema_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "schemas"
