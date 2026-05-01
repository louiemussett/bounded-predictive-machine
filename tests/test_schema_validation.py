import json

import pytest
from jsonschema import ValidationError

from bpm_runtime.loop import run_manual_text_loop
from bpm_runtime.records import BeliefStateRecord, PredictionRecord
from bpm_runtime.schema_validation import validate_record, validate_record_dict
from bpm_runtime.trace import save_loop_result_jsonl


def test_valid_records_pass_validation(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    for record in result.values():
        if record is not None:
            validate_record(record)


def test_missing_required_base_fields_fail_validation() -> None:
    record = PredictionRecord(id="prediction-1", loop_id="loop-1").to_dict()
    del record["id"]

    with pytest.raises(ValidationError):
        validate_record_dict(record)


def test_wrong_record_type_fails_validation() -> None:
    record = PredictionRecord(id="prediction-1", loop_id="loop-1").to_dict()
    record["record_type"] = "SignalRecord"

    with pytest.raises(ValidationError):
        validate_record_dict(record)


def test_loop_record_schema_validates_ordered_record_ids_and_record_types(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )
    loop_record = result["loop_record"].to_dict()

    validate_record_dict(loop_record)

    loop_record["ordered_record_ids"] = ["prediction-1", 42]
    with pytest.raises(ValidationError):
        validate_record_dict(loop_record)


def test_saved_jsonl_records_can_be_loaded_and_validated(tmp_path) -> None:
    result = run_manual_text_loop(
        "bounded input",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    paths = save_loop_result_jsonl(result, trace_dir=tmp_path / "traces")

    for trace_path in paths.values():
        for line in trace_path.read_text(encoding="utf-8").splitlines():
            validate_record_dict(json.loads(line))


def test_uncertainty_and_abstention_records_validate(tmp_path) -> None:
    result = run_manual_text_loop(
        "???",
        BeliefStateRecord(id="belief-1"),
        boundary_config=_boundary_config(tmp_path),
        loop_id="loop-1",
    )

    validate_record(result["uncertainty_gate"])
    validate_record(result["abstention"])


def _boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }
