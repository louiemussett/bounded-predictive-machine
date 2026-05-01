"""Deterministic prediction creation for the first-build runtime."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import PredictionRecord


def create_prediction(
    prior_belief: Any,
    target: str | None,
    expected: str | None,
    loop_id: str | None = None,
) -> PredictionRecord:
    """Create a prediction before any signal is read or interpreted."""

    source_refs = []
    if hasattr(prior_belief, "id"):
        source_refs.append(prior_belief.id)

    uncertainty: list[str] = []
    if not target:
        uncertainty.append("prediction target is missing")
    if not expected:
        uncertainty.append("expected signal, state, or outcome is missing")

    return PredictionRecord(
        created_by="bpm_runtime.prediction",
        loop_id=loop_id,
        source_refs=source_refs,
        target=target,
        expected=expected,
        match_conditions=_match_conditions(target, expected),
        uncertainty=uncertainty,
    )


def _match_conditions(target: str | None, expected: str | None) -> list[str]:
    if not target or not expected:
        return []

    return [f"{target} matches expected value: {expected}"]
