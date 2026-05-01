"""Deterministic signal interpretation for the first-build runtime."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import InterpretationRecord


def interpret_signal(
    signal: Any,
    prediction: Any = None,
    loop_id: str | None = None,
) -> InterpretationRecord:
    """Interpret a signal without updating belief or creating actions."""

    signal_payload = getattr(signal, "payload", None)
    signal_summary = getattr(signal, "payload_summary", None)
    text = _text_from_signal(signal_payload, signal_summary)

    source_refs = []
    signal_id = getattr(signal, "id", None)
    if signal_id:
        source_refs.append(signal_id)

    prediction_id = getattr(prediction, "id", None)
    if prediction_id:
        source_refs.append(prediction_id)

    uncertainty: list[str] = []
    if not text:
        uncertainty.append("signal payload is empty or missing")
    elif _is_unclear(text):
        uncertainty.append("signal meaning is unclear")

    return InterpretationRecord(
        created_by="bpm_runtime.interpretation",
        loop_id=loop_id or getattr(signal, "loop_id", None),
        source_refs=source_refs,
        primary_interpretation=_primary_interpretation(text),
        alternative_interpretations=_alternative_interpretations(text),
        relevant_belief_targets=_belief_targets(prediction),
        interpretation_confidence=_confidence(text),
        uncertainty=uncertainty,
    )


def _text_from_signal(payload: Any, payload_summary: Any) -> str:
    if isinstance(payload, str) and payload.strip():
        return payload.strip()
    if isinstance(payload_summary, str) and payload_summary.strip():
        return payload_summary.strip()
    return ""


def _is_unclear(text: str) -> bool:
    unclear_values = {"?", "??", "???", "unclear", "unknown", "n/a"}
    return text.lower() in unclear_values


def _primary_interpretation(text: str) -> str | None:
    if not text:
        return None
    return f"manual text signal states: {text}"


def _alternative_interpretations(text: str) -> list[str]:
    if not text:
        return []
    if _is_unclear(text):
        return ["manual text may be incomplete", "manual text may require clarification"]
    return []


def _belief_targets(prediction: Any) -> list[str]:
    target = getattr(prediction, "target", None)
    if target:
        return [target]
    return []


def _confidence(text: str) -> str:
    if not text:
        return "none"
    if _is_unclear(text):
        return "low"
    return "medium"
