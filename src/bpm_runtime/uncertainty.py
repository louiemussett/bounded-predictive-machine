"""Deterministic uncertainty gates and abstention records."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import (
    AbstentionRecord,
    ClarificationRequestRecord,
    UncertaintyGateRecord,
)


def evaluate_uncertainty_gate(
    evidence_quality: Any,
    interpretation: Any = None,
    loop_id: str | None = None,
) -> UncertaintyGateRecord:
    """Decide whether evidence is sufficient for update or action."""

    quality_label = getattr(evidence_quality, "quality_label", None)
    interpretation_confidence = getattr(interpretation, "interpretation_confidence", None)
    prediction_result = getattr(evidence_quality, "prediction_result", None)
    uncertainty = _uncertainty(evidence_quality, interpretation)
    source_refs = _source_refs(evidence_quality, interpretation)

    if quality_label in {"low", "inconclusive"}:
        decision = "abstain"
        reason = f"not enough evidence: evidence quality is {quality_label}"
        allow_belief_update = False
        allow_action = False
    elif interpretation_confidence in {"none", "low"}:
        decision = "clarify"
        reason = f"not enough evidence: interpretation confidence is {interpretation_confidence}"
        allow_belief_update = False
        allow_action = False
    elif prediction_result == "inconclusive":
        decision = "abstain"
        reason = "not enough evidence: prediction result is inconclusive"
        allow_belief_update = False
        allow_action = False
    elif uncertainty:
        decision = "abstain"
        reason = "not enough evidence: unresolved uncertainty remains"
        allow_belief_update = False
        allow_action = False
    else:
        decision = "proceed"
        reason = "evidence is sufficient for scoped update consideration"
        allow_belief_update = True
        allow_action = quality_label in {"high", "medium"}

    return UncertaintyGateRecord(
        created_by="bpm_runtime.uncertainty",
        loop_id=loop_id or getattr(evidence_quality, "loop_id", None),
        status=decision,
        source_refs=source_refs,
        decision=decision,
        reason=reason,
        allow_belief_update=allow_belief_update,
        allow_action=allow_action,
        evidence_quality=quality_label,
        interpretation_confidence=interpretation_confidence,
        prediction_result=prediction_result,
        uncertainty=uncertainty,
    )


def create_abstention(
    reason: str,
    uncertainty_gate: Any = None,
    loop_id: str | None = None,
) -> AbstentionRecord:
    """Create a record-backed abstention decision."""

    return AbstentionRecord(
        created_by="bpm_runtime.uncertainty",
        loop_id=loop_id or getattr(uncertainty_gate, "loop_id", None),
        source_refs=_source_refs(uncertainty_gate),
        reason=reason,
        gate_decision=getattr(uncertainty_gate, "decision", None),
        uncertainty=list(getattr(uncertainty_gate, "uncertainty", []) or []),
    )


def create_clarification_request(
    reason: str,
    uncertainty_gate: Any = None,
    loop_id: str | None = None,
) -> ClarificationRequestRecord:
    """Create a simple clarification request record."""

    return ClarificationRequestRecord(
        created_by="bpm_runtime.uncertainty",
        loop_id=loop_id or getattr(uncertainty_gate, "loop_id", None),
        source_refs=_source_refs(uncertainty_gate),
        request="Please provide a clearer manual text signal.",
        reason=reason,
        uncertainty=list(getattr(uncertainty_gate, "uncertainty", []) or []),
    )


def _source_refs(*records: Any) -> list[str]:
    refs = []
    for record in records:
        record_id = getattr(record, "id", None)
        if record_id:
            refs.append(record_id)
    return refs


def _uncertainty(evidence_quality: Any, interpretation: Any) -> list[str]:
    uncertainty: list[str] = []
    uncertainty.extend(getattr(evidence_quality, "uncertainty", []) or [])
    uncertainty.extend(getattr(interpretation, "uncertainty", []) or [])
    return list(dict.fromkeys(uncertainty))
