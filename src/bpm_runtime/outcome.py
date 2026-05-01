"""Outcome record creation for the first-build runtime."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import OutcomeRecord


def create_outcome(
    action_record: Any,
    observed_effect: str | None = None,
    success: bool | None = None,
    loop_id: str | None = None,
) -> OutcomeRecord:
    """Create an outcome record without updating belief or memory."""

    action_ref = getattr(action_record, "id", None)
    uncertainty: list[str] = []
    unresolved_questions: list[str] = []

    if not action_ref:
        uncertainty.append("action reference is missing")
    if not observed_effect:
        uncertainty.append("observed effect is missing")
        unresolved_questions.append("what outcome was observed?")
    if success is None:
        unresolved_questions.append("whether the outcome succeeded is unknown")

    return OutcomeRecord(
        created_by="bpm_runtime.outcome",
        loop_id=loop_id or getattr(action_record, "loop_id", None),
        source_refs=[action_ref] if action_ref else [],
        action_ref=action_ref,
        observed_effect=observed_effect,
        success=success,
        unresolved_questions=unresolved_questions,
        uncertainty=uncertainty,
    )
