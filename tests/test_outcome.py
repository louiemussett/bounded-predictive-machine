from bpm_runtime.actions import create_no_action
from bpm_runtime.outcome import create_outcome
from bpm_runtime.records import (
    BeliefUpdateRecord,
    MemoryTraceRecord,
    NoActionRecord,
    OutcomeRecord,
)


def test_creating_outcome_record() -> None:
    action = create_no_action("wait for clearer evidence")

    outcome = create_outcome(action, observed_effect="nothing changed", success=True)

    assert isinstance(outcome, OutcomeRecord)


def test_record_type_correctness() -> None:
    action = create_no_action("wait")

    outcome = create_outcome(action)

    assert outcome.record_type == "OutcomeRecord"


def test_referencing_action_or_no_action_record() -> None:
    action = NoActionRecord(id="no-action-1", reason="wait")

    outcome = create_outcome(action)

    assert outcome.action_ref == "no-action-1"
    assert outcome.source_refs == ["no-action-1"]


def test_preserving_observed_effect_and_success() -> None:
    action = create_no_action("wait")

    outcome = create_outcome(action, observed_effect="no file was written", success=True)

    assert outcome.observed_effect == "no file was written"
    assert outcome.success is True


def test_adding_uncertainty_when_observed_effect_is_missing() -> None:
    action = create_no_action("wait")

    outcome = create_outcome(action)

    assert outcome.uncertainty == ["observed effect is missing"]
    assert "what outcome was observed?" in outcome.unresolved_questions


def test_outcome_creation_does_not_update_belief_or_create_memory() -> None:
    action = create_no_action("wait")

    outcome = create_outcome(action, observed_effect="nothing changed", success=True)

    assert isinstance(outcome, OutcomeRecord)
    assert not isinstance(outcome, BeliefUpdateRecord)
    assert not isinstance(outcome, MemoryTraceRecord)
