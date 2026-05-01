"""Scoped belief update decisions for the first-build runtime."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import BeliefUpdateRecord, NoUpdateRecord


def apply_belief_update(
    prior_belief: Any,
    evidence_quality: Any,
    interpretation: Any = None,
    loop_id: str | None = None,
) -> BeliefUpdateRecord | NoUpdateRecord:
    """Return a scoped belief-update record or a no-update record."""

    source_refs = _source_refs(prior_belief, evidence_quality, interpretation)
    quality_label = getattr(evidence_quality, "quality_label", None)
    update_target = _update_target(evidence_quality, interpretation)
    uncertainty = _uncertainty(evidence_quality)

    if quality_label in {"high", "medium"}:
        return BeliefUpdateRecord(
            created_by="bpm_runtime.belief",
            loop_id=loop_id or getattr(evidence_quality, "loop_id", None),
            source_refs=source_refs,
            update_target=update_target,
            update_summary=_update_summary(update_target, quality_label, interpretation),
            evidence_quality_used=quality_label,
            uncertainty=uncertainty,
        )

    return NoUpdateRecord(
        created_by="bpm_runtime.belief",
        loop_id=loop_id or getattr(evidence_quality, "loop_id", None),
        source_refs=source_refs,
        update_target=update_target,
        no_update_reason=_no_update_reason(quality_label),
        evidence_quality_used=quality_label,
        uncertainty=uncertainty,
    )


def _source_refs(
    prior_belief: Any,
    evidence_quality: Any,
    interpretation: Any,
) -> list[str]:
    refs = []
    for record in (prior_belief, evidence_quality, interpretation):
        record_id = getattr(record, "id", None)
        if record_id:
            refs.append(record_id)
    return refs


def _update_target(evidence_quality: Any, interpretation: Any) -> str | None:
    update_targets = getattr(evidence_quality, "update_targets", None) or []
    if update_targets:
        return update_targets[0]

    interpretation_targets = getattr(interpretation, "relevant_belief_targets", None) or []
    if interpretation_targets:
        return interpretation_targets[0]

    return None


def _uncertainty(evidence_quality: Any) -> list[str]:
    if evidence_quality is None:
        return ["evidence quality is missing"]

    return list(getattr(evidence_quality, "uncertainty", []) or [])


def _update_summary(
    update_target: str | None,
    quality_label: str,
    interpretation: Any,
) -> str:
    target = update_target or "unspecified target"
    interpretation_text = getattr(interpretation, "primary_interpretation", None)
    if interpretation_text:
        return f"{target} updated using {quality_label} evidence: {interpretation_text}"
    return f"{target} updated using {quality_label} evidence"


def _no_update_reason(quality_label: str | None) -> str:
    if quality_label is None:
        return "no update: evidence quality is missing"
    return f"no update: evidence quality is {quality_label}"
