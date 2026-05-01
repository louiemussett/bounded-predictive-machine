"""Transparent lightweight scoring for evidence and belief updates."""

from __future__ import annotations

from typing import Any


DEFAULT_PRIOR_CONFIDENCE = 0.5
DEFAULT_UPDATE_THRESHOLD = 0.6


QUALITY_BASE_SCORES = {
    "high": 0.9,
    "medium": 0.7,
    "low": 0.3,
    "inconclusive": 0.1,
}


def score_evidence(
    quality_label: str | None,
    prediction_result: str | None,
    uncertainty: list[str],
) -> dict[str, Any]:
    """Return deterministic evidence score components and final score."""

    base_score = QUALITY_BASE_SCORES.get(quality_label, 0.0)
    prediction_penalty = 0.05 if prediction_result == "mismatch" else 0.0
    uncertainty_penalty = min(0.3, 0.1 * len(uncertainty))
    evidence_score = max(0.0, round(base_score - prediction_penalty - uncertainty_penalty, 3))

    return {
        "evidence_score": evidence_score,
        "update_threshold": DEFAULT_UPDATE_THRESHOLD,
        "score_components": {
            "quality_label": quality_label,
            "base_score": base_score,
            "prediction_result": prediction_result,
            "prediction_penalty": prediction_penalty,
            "uncertainty_count": len(uncertainty),
            "uncertainty_penalty": uncertainty_penalty,
            "reason": (
                "score = base_score - prediction_penalty - uncertainty_penalty"
            ),
        },
    }


def confidence_update(
    prior_confidence: float | None,
    evidence_score: float | None,
    update_threshold: float | None,
    update_allowed: bool,
) -> dict[str, float]:
    """Compute simple prior/posterior confidence fields."""

    prior = DEFAULT_PRIOR_CONFIDENCE if prior_confidence is None else prior_confidence
    score = 0.0 if evidence_score is None else evidence_score
    threshold = DEFAULT_UPDATE_THRESHOLD if update_threshold is None else update_threshold

    if update_allowed and score >= threshold:
        confidence_delta = round((score - prior) * 0.5, 3)
        posterior = round(min(1.0, max(0.0, prior + confidence_delta)), 3)
    else:
        confidence_delta = 0.0
        posterior = round(prior, 3)

    return {
        "prior_confidence": round(prior, 3),
        "posterior_confidence": posterior,
        "confidence_delta": confidence_delta,
    }
