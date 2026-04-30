"""Minimal action safety checks for the first-build runtime."""

from __future__ import annotations

from typing import Any, Mapping

from bpm_runtime.paths import is_path_allowed
from bpm_runtime.records import SafetyCheckRecord


WRITE_ACTIONS = {"write", "write_file", "append_jsonl_record", "update_state"}


def evaluate_action_safety(
    action_candidate: Mapping[str, Any] | Any,
    boundary_config: dict[str, Any],
    viability_state: str = "safe",
) -> SafetyCheckRecord:
    """Evaluate a simple action candidate without executing it."""

    candidate = _candidate_to_dict(action_candidate)
    source_refs = _source_refs(candidate)
    uncertainty: list[str] = []

    action_name = candidate.get("action_name") or candidate.get("action")
    expected_effect = candidate.get("expected_effect")

    if not action_name:
        uncertainty.append("blocked: action name is missing")

    if not expected_effect:
        uncertainty.append("blocked: expected effect is missing")

    if _is_write_action(candidate):
        target_path = candidate.get("target_path") or candidate.get("target")

        if viability_state != "safe":
            uncertainty.append(f"blocked: viability state is {viability_state!r}, not 'safe'")

        if not target_path:
            uncertainty.append("blocked: write action has no target path")
        elif not is_path_allowed(target_path, boundary_config, "write"):
            uncertainty.append(f"blocked: write target is outside allowed boundary: {target_path}")

    status = "allowed" if not uncertainty else "blocked"
    if status == "allowed":
        uncertainty.append("allowed: minimal safety checks passed")

    return SafetyCheckRecord(
        created_by="bpm_runtime.safety",
        loop_id=candidate.get("loop_id"),
        status=status,
        source_refs=source_refs,
        uncertainty=uncertainty,
    )


def _candidate_to_dict(action_candidate: Mapping[str, Any] | Any) -> dict[str, Any]:
    if hasattr(action_candidate, "to_dict"):
        payload = action_candidate.to_dict()
    else:
        payload = action_candidate

    if not isinstance(payload, Mapping):
        raise TypeError("action_candidate must be a mapping or provide to_dict()")

    return dict(payload)


def _source_refs(candidate: dict[str, Any]) -> list[str]:
    source_refs = candidate.get("source_refs", [])
    if source_refs is None:
        source_refs = []
    refs = list(source_refs)

    candidate_id = candidate.get("id")
    if candidate_id and candidate_id not in refs:
        refs.append(candidate_id)

    return refs


def _is_write_action(candidate: dict[str, Any]) -> bool:
    access_type = candidate.get("access_type")
    if access_type == "write":
        return True

    action_name = candidate.get("action_name") or candidate.get("action")
    if action_name in WRITE_ACTIONS:
        return True

    return bool(candidate.get("writes"))
