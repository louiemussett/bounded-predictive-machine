"""Scoped belief update decisions for the first-build runtime."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import BeliefUpdateRecord, NoUpdateRecord
from bpm_runtime.scoring import confidence_update


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
    evidence_score = getattr(evidence_quality, "evidence_score", None)
    update_threshold = getattr(evidence_quality, "update_threshold", None)
    score_allows_update = _score_allows_update(evidence_score, update_threshold)
    confidence = confidence_update(
        getattr(prior_belief, "posterior_confidence", None),
        evidence_score,
        update_threshold,
        quality_label in {"high", "medium"} and score_allows_update,
    )

    if quality_label in {"high", "medium"} and score_allows_update:
        return BeliefUpdateRecord(
            created_by="bpm_runtime.belief",
            loop_id=loop_id or getattr(evidence_quality, "loop_id", None),
            source_refs=source_refs,
            update_target=update_target,
            update_summary=_update_summary(
                update_target,
                quality_label,
                evidence_score,
                update_threshold,
                interpretation,
            ),
            evidence_quality_used=quality_label,
            evidence_score=evidence_score,
            prior_confidence=confidence["prior_confidence"],
            posterior_confidence=confidence["posterior_confidence"],
            confidence_delta=confidence["confidence_delta"],
            update_threshold=update_threshold,
            score_components=getattr(evidence_quality, "score_components", {}) or {},
            uncertainty=uncertainty,
        )

    return NoUpdateRecord(
        created_by="bpm_runtime.belief",
        loop_id=loop_id or getattr(evidence_quality, "loop_id", None),
        source_refs=source_refs,
        update_target=update_target,
        no_update_reason=_no_update_reason(quality_label, evidence_score, update_threshold),
        evidence_quality_used=quality_label,
        evidence_score=evidence_score,
        prior_confidence=confidence["prior_confidence"],
        posterior_confidence=confidence["posterior_confidence"],
        confidence_delta=confidence["confidence_delta"],
        update_threshold=update_threshold,
        score_components=getattr(evidence_quality, "score_components", {}) or {},
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
    evidence_score: float | None,
    update_threshold: float | None,
    interpretation: Any,
) -> str:
    target = update_target or "unspecified target"
    interpretation_text = getattr(interpretation, "primary_interpretation", None)
    score_text = _score_text(evidence_score, update_threshold)
    if interpretation_text:
        return f"{target} updated using {quality_label} evidence ({score_text}): {interpretation_text}"
    return f"{target} updated using {quality_label} evidence ({score_text})"


def _no_update_reason(
    quality_label: str | None,
    evidence_score: float | None,
    update_threshold: float | None,
) -> str:
    score_text = _score_text(evidence_score, update_threshold)
    if quality_label is None:
        return f"no update: evidence quality is missing ({score_text})"
    if not _score_allows_update(evidence_score, update_threshold):
        return f"no update: evidence quality is {quality_label}; score below threshold ({score_text})"
    return f"no update: evidence quality is {quality_label} ({score_text})"


def _score_allows_update(
    evidence_score: float | None,
    update_threshold: float | None,
) -> bool:
    if evidence_score is None or update_threshold is None:
        return False
    return evidence_score >= update_threshold


def _score_text(evidence_score: float | None, update_threshold: float | None) -> str:
    return f"score={evidence_score}, threshold={update_threshold}"
