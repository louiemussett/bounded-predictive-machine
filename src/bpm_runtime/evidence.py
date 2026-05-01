"""Categorical evidence-quality assessment for the first-build runtime."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import EvidenceQualityRecord


def assess_evidence_quality(
    signal: Any,
    interpretation: Any,
    prediction: Any = None,
    loop_id: str | None = None,
) -> EvidenceQualityRecord:
    """Assess evidence quality without updating belief or creating actions."""

    source_refs = _source_refs(signal, interpretation, prediction)
    uncertainty = _uncertainty(signal, interpretation, prediction)
    prediction_result = _prediction_result(signal, interpretation, prediction)
    quality_label = _quality_label(signal, interpretation, prediction_result, uncertainty)

    return EvidenceQualityRecord(
        created_by="bpm_runtime.evidence",
        loop_id=loop_id or getattr(signal, "loop_id", None),
        source_refs=source_refs,
        quality_label=quality_label,
        reasons=_reasons(quality_label, prediction_result, uncertainty),
        update_targets=_update_targets(interpretation, quality_label),
        prediction_result=prediction_result,
        uncertainty=uncertainty,
    )


def _source_refs(signal: Any, interpretation: Any, prediction: Any) -> list[str]:
    refs = []
    for record in (signal, interpretation, prediction):
        record_id = getattr(record, "id", None)
        if record_id:
            refs.append(record_id)
    return refs


def _uncertainty(signal: Any, interpretation: Any, prediction: Any) -> list[str]:
    uncertainty: list[str] = []

    if not getattr(signal, "payload", None) and not getattr(signal, "payload_summary", None):
        uncertainty.append("signal payload is missing")

    interpretation_text = getattr(interpretation, "primary_interpretation", None)
    if not interpretation_text:
        uncertainty.append("interpretation is missing")

    uncertainty.extend(getattr(signal, "uncertainty", []) or [])
    uncertainty.extend(getattr(interpretation, "uncertainty", []) or [])

    if prediction is None:
        uncertainty.append("prediction was not provided")

    return list(dict.fromkeys(uncertainty))


def _prediction_result(signal: Any, interpretation: Any, prediction: Any) -> str:
    if prediction is None:
        return "inconclusive"

    expected = getattr(prediction, "expected", None)
    signal_text = _signal_text(signal)
    interpretation_text = getattr(interpretation, "primary_interpretation", None) or ""

    if not expected or not signal_text or not interpretation_text:
        return "inconclusive"

    expected_text = str(expected).strip().lower()
    combined_text = f"{signal_text} {interpretation_text}".lower()

    if expected_text in combined_text:
        return "match"

    return "mismatch"


def _quality_label(
    signal: Any,
    interpretation: Any,
    prediction_result: str,
    uncertainty: list[str],
) -> str:
    interpretation_confidence = getattr(interpretation, "interpretation_confidence", None)
    signal_text = _signal_text(signal)

    if not signal_text:
        return "inconclusive"
    if uncertainty and interpretation_confidence in {"none", "low"}:
        return "low"
    if prediction_result == "match" and interpretation_confidence == "medium":
        return "high"
    if prediction_result == "mismatch":
        return "medium"
    if prediction_result == "inconclusive":
        return "low"
    return "medium"


def _reasons(
    quality_label: str,
    prediction_result: str,
    uncertainty: list[str],
) -> list[str]:
    reasons = [f"quality label is {quality_label}", f"prediction result is {prediction_result}"]
    reasons.extend(uncertainty)
    return reasons


def _update_targets(interpretation: Any, quality_label: str) -> list[str]:
    if quality_label == "inconclusive":
        return []
    return list(getattr(interpretation, "relevant_belief_targets", []) or [])


def _signal_text(signal: Any) -> str:
    payload = getattr(signal, "payload", None)
    if isinstance(payload, str) and payload.strip():
        return payload.strip()

    payload_summary = getattr(signal, "payload_summary", None)
    if isinstance(payload_summary, str) and payload_summary.strip():
        return payload_summary.strip()

    return ""
