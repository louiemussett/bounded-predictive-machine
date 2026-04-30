import json

from bpm_runtime.records import BodyStateRecord, SignalRecord
from bpm_runtime.trace import append_jsonl_record


def read_jsonl(path):
    return path.read_text(encoding="utf-8").splitlines()


def test_writing_one_record(tmp_path) -> None:
    trace_path = tmp_path / "trace.jsonl"
    record = BodyStateRecord(id="body-1", created_at="2026-05-01T00:00:00+00:00")

    append_jsonl_record(trace_path, record)

    lines = read_jsonl(trace_path)
    assert len(lines) == 1
    assert json.loads(lines[0])["record_type"] == "BodyStateRecord"


def test_writing_multiple_records(tmp_path) -> None:
    trace_path = tmp_path / "trace.jsonl"

    append_jsonl_record(trace_path, BodyStateRecord(id="body-1"))
    append_jsonl_record(trace_path, SignalRecord(id="signal-1"))

    lines = read_jsonl(trace_path)
    assert len(lines) == 2
    assert json.loads(lines[0])["id"] == "body-1"
    assert json.loads(lines[1])["id"] == "signal-1"


def test_creating_parent_directories(tmp_path) -> None:
    trace_path = tmp_path / "nested" / "trace" / "trace.jsonl"

    append_jsonl_record(trace_path, BodyStateRecord(id="body-1"))

    assert trace_path.exists()


def test_accepting_plain_dictionaries(tmp_path) -> None:
    trace_path = tmp_path / "trace.jsonl"

    append_jsonl_record(trace_path, {"id": "plain-1", "record_type": "PlainRecord"})

    lines = read_jsonl(trace_path)
    assert json.loads(lines[0]) == {"id": "plain-1", "record_type": "PlainRecord"}


def test_each_line_is_valid_json(tmp_path) -> None:
    trace_path = tmp_path / "trace.jsonl"

    append_jsonl_record(trace_path, BodyStateRecord(id="body-1"))
    append_jsonl_record(trace_path, {"id": "plain-1", "record_type": "PlainRecord"})

    for line in read_jsonl(trace_path):
        parsed = json.loads(line)
        assert isinstance(parsed, dict)
