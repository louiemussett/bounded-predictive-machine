from bpm_runtime.records import SafetyCheckRecord
from bpm_runtime.safety import evaluate_action_safety


def make_boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }


def make_write_candidate(target_path):
    return {
        "id": "action-1",
        "action_name": "write_file",
        "expected_effect": "write a local runtime file",
        "target_path": str(target_path),
        "access_type": "write",
    }


def test_allowing_safe_write_action_to_allowed_path(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    candidate = make_write_candidate(tmp_path / "state" / "current.json")

    safety_check = evaluate_action_safety(candidate, config)

    assert safety_check.status == "allowed"
    assert safety_check.source_refs == ["action-1"]
    assert safety_check.uncertainty == ["allowed: minimal safety checks passed"]


def test_blocking_writes_to_source_documents(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    candidate = make_write_candidate(tmp_path / "Source Documents" / "0. White Paper.md")

    safety_check = evaluate_action_safety(candidate, config)

    assert safety_check.status == "blocked"
    assert any("outside allowed boundary" in item for item in safety_check.uncertainty)


def test_blocking_unknown_write_targets(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    candidate = make_write_candidate(tmp_path / "unknown" / "file.json")

    safety_check = evaluate_action_safety(candidate, config)

    assert safety_check.status == "blocked"
    assert any("outside allowed boundary" in item for item in safety_check.uncertainty)


def test_blocking_write_action_when_viability_state_is_not_safe(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    candidate = make_write_candidate(tmp_path / "state" / "current.json")

    safety_check = evaluate_action_safety(candidate, config, viability_state="degraded")

    assert safety_check.status == "blocked"
    assert any("viability state" in item for item in safety_check.uncertainty)


def test_blocking_action_candidates_with_no_expected_effect(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    candidate = make_write_candidate(tmp_path / "state" / "current.json")
    del candidate["expected_effect"]

    safety_check = evaluate_action_safety(candidate, config)

    assert safety_check.status == "blocked"
    assert any("expected effect is missing" in item for item in safety_check.uncertainty)


def test_returning_safety_check_record(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    candidate = make_write_candidate(tmp_path / "state" / "current.json")

    safety_check = evaluate_action_safety(candidate, config)

    assert isinstance(safety_check, SafetyCheckRecord)
    assert safety_check.record_type == "SafetyCheckRecord"
