import json

from bpm_runtime.paths import is_path_allowed, load_boundary_config


def make_boundary_config(project_root):
    return {
        "project_root": str(project_root),
        "allowed_read_paths": ["Source Documents"],
        "allowed_write_paths": ["state", "traces"],
        "read_only_paths": ["Source Documents"],
        "forbidden_paths": [".env", "secrets"],
    }


def test_loading_boundary_config(tmp_path) -> None:
    config_path = tmp_path / "boundary.json"
    config = make_boundary_config(tmp_path)
    config_path.write_text(json.dumps(config), encoding="utf-8")

    loaded_config = load_boundary_config(config_path)

    assert loaded_config == config


def test_allowing_reads_from_source_documents(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    target = tmp_path / "Source Documents" / "0. White Paper.md"

    assert is_path_allowed(target, config, "read")


def test_rejecting_writes_to_source_documents(tmp_path) -> None:
    config = make_boundary_config(tmp_path)
    target = tmp_path / "Source Documents" / "0. White Paper.md"

    assert not is_path_allowed(target, config, "write")


def test_allowing_writes_to_configured_state_and_traces_paths(tmp_path) -> None:
    config = make_boundary_config(tmp_path)

    assert is_path_allowed(tmp_path / "state" / "current.json", config, "write")
    assert is_path_allowed(tmp_path / "traces" / "loop.jsonl", config, "write")


def test_rejecting_unknown_write_targets(tmp_path) -> None:
    config = make_boundary_config(tmp_path)

    assert not is_path_allowed(tmp_path / "README.md", config, "write")


def test_rejecting_forbidden_paths(tmp_path) -> None:
    config = make_boundary_config(tmp_path)

    assert not is_path_allowed(tmp_path / ".env", config, "read")
    assert not is_path_allowed(tmp_path / "secrets" / "token.txt", config, "write")
