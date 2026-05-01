"""Loop record linking and one deterministic manual loop."""

from __future__ import annotations

from typing import Any, Iterable
from uuid import uuid4

from bpm_runtime.actions import create_action_candidate, create_no_action
from bpm_runtime.belief import apply_belief_update
from bpm_runtime.evidence import assess_evidence_quality
from bpm_runtime.interpretation import interpret_signal
from bpm_runtime.memory import create_memory_trace
from bpm_runtime.outcome import create_outcome
from bpm_runtime.prediction import create_prediction
from bpm_runtime.records import LoopRecord
from bpm_runtime.safety import evaluate_action_safety
from bpm_runtime.signals import create_manual_text_signal


def create_loop_record(
    records: Iterable[Any],
    loop_id: str | None = None,
    status: str = "completed",
) -> LoopRecord:
    """Create a linker record for an existing loop chain."""

    record_list = list(records)
    ordered_record_ids = _record_ids(record_list)

    return LoopRecord(
        created_by="bpm_runtime.loop",
        loop_id=loop_id or _first_loop_id(record_list),
        status=status,
        source_refs=ordered_record_ids,
        ordered_record_ids=ordered_record_ids,
        record_types=_record_types(record_list),
        uncertainty=_carried_uncertainty(record_list),
    )


def run_manual_text_loop(
    manual_text: str,
    prior_belief: Any,
    boundary_config: dict[str, Any] | None = None,
    loop_id: str | None = None,
) -> dict[str, Any]:
    """Run one deterministic manual-text loop without persistence or execution."""

    active_loop_id = loop_id or f"loop-{uuid4()}"
    boundary = boundary_config or _default_boundary_config()

    prediction = create_prediction(
        prior_belief,
        target="manual_text_signal",
        expected="manual text signal may contain feedback, clarification, or an update-relevant observation",
        loop_id=active_loop_id,
    )
    signal = create_manual_text_signal(manual_text, loop_id=active_loop_id)
    interpretation = interpret_signal(signal, prediction, loop_id=active_loop_id)
    evidence = assess_evidence_quality(
        signal,
        interpretation,
        prediction,
        loop_id=active_loop_id,
    )
    belief_result = apply_belief_update(
        prior_belief,
        evidence,
        interpretation,
        loop_id=active_loop_id,
    )

    safety_check = None
    if _should_create_action_candidate(manual_text, evidence, belief_result):
        action_result = create_action_candidate(
            belief_result,
            action_name="write_file",
            expected_effect="propose writing current belief state",
            target_path="state/current.json",
            loop_id=active_loop_id,
        )
        safety_check = evaluate_action_safety(action_result, boundary)
        outcome = create_outcome(
            action_result,
            observed_effect=_action_outcome_text(safety_check.status),
            success=safety_check.status == "allowed",
            loop_id=active_loop_id,
        )
    else:
        action_result = create_no_action(
            _no_action_reason(manual_text, evidence),
            belief_result,
            loop_id=active_loop_id,
        )
        outcome = create_outcome(
            action_result,
            observed_effect="no action selected; no external action performed",
            success=True,
            loop_id=active_loop_id,
        )

    memory_inputs = [
        prediction,
        signal,
        interpretation,
        evidence,
        belief_result,
        action_result,
    ]
    if safety_check is not None:
        memory_inputs.append(safety_check)
    memory_inputs.append(outcome)

    memory_trace = create_memory_trace(
        memory_inputs,
        loop_id=active_loop_id,
        summary="manual text loop reconstructed from linked records",
    )

    loop_chain = [*memory_inputs, memory_trace]
    loop_record = create_loop_record(
        loop_chain,
        loop_id=active_loop_id,
        status="completed",
    )

    return {
        "prediction": prediction,
        "signal": signal,
        "interpretation": interpretation,
        "evidence": evidence,
        "belief_result": belief_result,
        "action_result": action_result,
        "safety_check": safety_check,
        "outcome": outcome,
        "memory_trace": memory_trace,
        "loop_record": loop_record,
    }


def _record_ids(records: list[Any]) -> list[str]:
    ids = []
    for record in records:
        record_id = getattr(record, "id", None)
        if record_id:
            ids.append(record_id)
    return ids


def _record_types(records: list[Any]) -> list[str]:
    return [getattr(record, "record_type", record.__class__.__name__) for record in records]


def _carried_uncertainty(records: list[Any]) -> list[str]:
    uncertainty: list[str] = []
    for record in records:
        uncertainty.extend(getattr(record, "uncertainty", []) or [])
    return list(dict.fromkeys(uncertainty))


def _first_loop_id(records: list[Any]) -> str | None:
    for record in records:
        loop_id = getattr(record, "loop_id", None)
        if loop_id:
            return loop_id
    return None


def _default_boundary_config() -> dict[str, Any]:
    return {
        "project_root": ".",
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }


def _should_create_action_candidate(
    manual_text: str,
    evidence: Any,
    belief_result: Any,
) -> bool:
    if not manual_text.strip():
        return False
    if getattr(evidence, "quality_label", None) in {"low", "inconclusive"}:
        return False
    return getattr(belief_result, "record_type", None) == "BeliefUpdateRecord"


def _no_action_reason(manual_text: str, evidence: Any) -> str:
    if not manual_text.strip():
        return "manual text is empty"

    quality_label = getattr(evidence, "quality_label", None)
    if quality_label in {"low", "inconclusive"}:
        return f"evidence quality is {quality_label}"

    return "no safe action candidate was selected"


def _action_outcome_text(safety_status: str) -> str:
    if safety_status == "allowed":
        return "action candidate passed safety; no external action executed"

    return "action candidate blocked by safety; no external action executed"
