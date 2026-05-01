"""Action candidate and no-action record creation."""

from __future__ import annotations

from typing import Any

from bpm_runtime.records import ActionCandidateRecord, NoActionRecord


def create_action_candidate(
    belief_result: Any,
    action_name: str | None,
    expected_effect: str | None,
    target_path: str | None = None,
    loop_id: str | None = None,
) -> ActionCandidateRecord:
    """Create an inert action candidate without executing it."""

    uncertainty: list[str] = []
    if not action_name:
        uncertainty.append("action name is missing")
    if not expected_effect:
        uncertainty.append("expected effect is missing")

    return ActionCandidateRecord(
        created_by="bpm_runtime.actions",
        loop_id=loop_id or getattr(belief_result, "loop_id", None),
        source_refs=_source_refs(belief_result),
        action_name=action_name,
        expected_effect=expected_effect,
        target_path=target_path,
        reason=_reason_from_belief_result(belief_result),
        uncertainty=uncertainty,
    )


def create_no_action(
    reason: str,
    belief_result: Any = None,
    loop_id: str | None = None,
) -> NoActionRecord:
    """Create an inspectable no-action decision."""

    uncertainty: list[str] = []
    if not reason:
        uncertainty.append("no-action reason is missing")

    return NoActionRecord(
        created_by="bpm_runtime.actions",
        loop_id=loop_id or getattr(belief_result, "loop_id", None),
        source_refs=_source_refs(belief_result),
        reason=reason,
        uncertainty=uncertainty,
    )


def _source_refs(record: Any) -> list[str]:
    record_id = getattr(record, "id", None)
    if record_id:
        return [record_id]
    return []


def _reason_from_belief_result(belief_result: Any) -> str | None:
    update_summary = getattr(belief_result, "update_summary", None)
    if update_summary:
        return update_summary

    no_update_reason = getattr(belief_result, "no_update_reason", None)
    if no_update_reason:
        return no_update_reason

    return None
