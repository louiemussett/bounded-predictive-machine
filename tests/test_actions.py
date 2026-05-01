from bpm_runtime.actions import create_action_candidate, create_no_action
from bpm_runtime.records import (
    ActionCandidateRecord,
    BeliefUpdateRecord,
    NoActionRecord,
    NoUpdateRecord,
)


def test_creating_action_candidate_record() -> None:
    belief_result = BeliefUpdateRecord(id="belief-update-1")

    candidate = create_action_candidate(
        belief_result,
        action_name="write_file",
        expected_effect="write runtime state",
    )

    assert isinstance(candidate, ActionCandidateRecord)


def test_record_type_correctness() -> None:
    candidate = create_action_candidate(None, "write_file", "write runtime state")

    assert candidate.record_type == "ActionCandidateRecord"


def test_referencing_belief_result() -> None:
    belief_result = BeliefUpdateRecord(id="belief-update-1")

    candidate = create_action_candidate(belief_result, "write_file", "write runtime state")

    assert candidate.source_refs == ["belief-update-1"]


def test_preserving_action_name_expected_effect_and_target_path(tmp_path) -> None:
    target_path = tmp_path / "state" / "current.json"

    candidate = create_action_candidate(
        None,
        action_name="write_file",
        expected_effect="write runtime state",
        target_path=str(target_path),
    )

    assert candidate.action_name == "write_file"
    assert candidate.expected_effect == "write runtime state"
    assert candidate.target_path == str(target_path)


def test_adding_uncertainty_when_expected_effect_is_missing() -> None:
    candidate = create_action_candidate(None, "write_file", expected_effect=None)

    assert candidate.uncertainty == ["expected effect is missing"]


def test_creating_no_action_record() -> None:
    belief_result = NoUpdateRecord(id="no-update-1")

    no_action = create_no_action("evidence is inconclusive", belief_result)

    assert isinstance(no_action, NoActionRecord)
    assert no_action.record_type == "NoActionRecord"
    assert no_action.reason == "evidence is inconclusive"
    assert no_action.source_refs == ["no-update-1"]


def test_no_action_is_valid_without_expected_effect() -> None:
    no_action = create_no_action("waiting for better evidence")

    assert no_action.reason == "waiting for better evidence"
    assert no_action.uncertainty == []


def test_no_files_are_written_or_actions_executed(tmp_path) -> None:
    target_path = tmp_path / "state" / "current.json"

    create_action_candidate(
        None,
        action_name="write_file",
        expected_effect="write runtime state",
        target_path=str(target_path),
    )
    create_no_action("do nothing")

    assert not target_path.exists()
