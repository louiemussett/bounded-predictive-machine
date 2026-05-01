"""Readable record-backed reports for manual loop runs."""

from __future__ import annotations

import json
from typing import Any


RECORD_ORDER = [
    "prediction",
    "signal",
    "interpretation",
    "evidence",
    "uncertainty_gate",
    "belief_result",
    "abstention",
    "action_result",
    "safety_check",
    "outcome",
    "memory_trace",
    "loop_record",
]


def loop_result_to_dict(loop_result: dict[str, Any]) -> dict[str, Any]:
    """Convert a loop-result mapping to deterministic plain dictionaries."""

    return {
        key: _record_to_dict(loop_result.get(key))
        for key in RECORD_ORDER
        if key in loop_result
    }


def loop_result_to_json(loop_result: dict[str, Any]) -> str:
    """Render loop records as deterministic readable JSON."""

    return json.dumps(loop_result_to_dict(loop_result), indent=2, sort_keys=True)


def loop_result_to_summary(loop_result: dict[str, Any]) -> str:
    """Render a concise human-readable report from record fields only."""

    records = loop_result_to_dict(loop_result)
    return "\n".join(
        [
            _line("Prediction", records.get("prediction"), "expected"),
            _line("Signal", records.get("signal"), "payload_summary"),
            _line("Interpretation", records.get("interpretation"), "primary_interpretation"),
            _line("Evidence quality", records.get("evidence"), "quality_label"),
            _score_line(records.get("evidence")),
            _uncertainty_gate_line(records.get("uncertainty_gate")),
            _belief_line(records.get("belief_result")),
            _abstention_line(records.get("abstention")),
            _action_line(records.get("action_result")),
            _safety_line(records.get("safety_check")),
            _line("Outcome", records.get("outcome"), "observed_effect"),
            _line("Memory trace", records.get("memory_trace"), "reconstruction_summary"),
            _uncertainty_line(records),
        ]
    )


def _record_to_dict(record: Any) -> dict[str, Any] | None:
    if record is None:
        return None
    if hasattr(record, "to_dict"):
        return record.to_dict()
    if isinstance(record, dict):
        return dict(record)
    raise TypeError("loop result values must be records, dictionaries, or None")


def _line(label: str, record: dict[str, Any] | None, field_name: str) -> str:
    if record is None:
        return f"{label}: not present"
    value = record.get(field_name)
    if value in (None, "", []):
        value = "not specified"
    return f"{label}: {value}"


def _belief_line(record: dict[str, Any] | None) -> str:
    if record is None:
        return "Belief result: not present"
    value = record.get("update_summary") or record.get("no_update_reason") or "not specified"
    return f"Belief result: {value}"


def _score_line(record: dict[str, Any] | None) -> str:
    if record is None:
        return "Evidence score: not present"
    score = record.get("evidence_score")
    threshold = record.get("update_threshold")
    if score is None:
        return "Evidence score: not present"
    return f"Evidence score: {score} (threshold: {threshold})"


def _uncertainty_gate_line(record: dict[str, Any] | None) -> str:
    if record is None:
        return "Uncertainty gate: not present"
    value = record.get("reason") or record.get("decision") or "not specified"
    return f"Uncertainty gate: {value}"


def _abstention_line(record: dict[str, Any] | None) -> str:
    if record is None:
        return "Abstention: not present"
    value = record.get("reason") or record.get("request") or "not specified"
    return f"Abstention: {value}"


def _action_line(record: dict[str, Any] | None) -> str:
    if record is None:
        return "Action/no-action: not present"
    value = record.get("action_name") or record.get("reason") or "not specified"
    return f"Action/no-action: {value}"


def _safety_line(record: dict[str, Any] | None) -> str:
    if record is None:
        return "Safety result: not present"
    return f"Safety result: {record.get('status', 'not specified')}"


def _uncertainty_line(records: dict[str, dict[str, Any] | None]) -> str:
    uncertainty: list[str] = []
    for record in records.values():
        if record is not None:
            uncertainty.extend(record.get("uncertainty", []) or [])

    if not uncertainty:
        return "Remaining uncertainty: none recorded"

    return "Remaining uncertainty: " + "; ".join(dict.fromkeys(uncertainty))
