"""Boundary config loading and deterministic path checks."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


BoundaryConfig = dict[str, Any]


def load_boundary_config(path: str | Path) -> BoundaryConfig:
    """Load a JSON boundary config file."""

    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def is_path_allowed(
    path: str | Path,
    boundary_config: BoundaryConfig,
    access_type: str,
) -> bool:
    """Return whether a path is allowed for read or write access."""

    if access_type not in {"read", "write"}:
        raise ValueError("access_type must be 'read' or 'write'")

    project_root = _resolve_path(boundary_config["project_root"], None)
    target_path = _resolve_path(path, project_root)

    if _matches_any(target_path, boundary_config.get("forbidden_paths", []), project_root):
        return False

    if access_type == "read":
        readable_paths = [
            *boundary_config.get("allowed_read_paths", []),
            *boundary_config.get("allowed_write_paths", []),
            *boundary_config.get("read_only_paths", []),
        ]
        return _matches_any(target_path, readable_paths, project_root)

    if _matches_any(target_path, boundary_config.get("read_only_paths", []), project_root):
        return False

    return _matches_any(
        target_path,
        boundary_config.get("allowed_write_paths", []),
        project_root,
    )


def _resolve_path(path: str | Path, project_root: Path | None) -> Path:
    candidate = Path(path)
    if not candidate.is_absolute() and project_root is not None:
        candidate = project_root / candidate
    return candidate.resolve(strict=False)


def _matches_any(path: Path, candidate_paths: list[str], project_root: Path) -> bool:
    return any(_is_within(path, _resolve_path(candidate, project_root)) for candidate in candidate_paths)


def _is_within(path: Path, boundary: Path) -> bool:
    normalized_path = os.path.normcase(str(path))
    normalized_boundary = os.path.normcase(str(boundary))

    try:
        os.path.commonpath([normalized_path, normalized_boundary])
    except ValueError:
        return False

    return os.path.commonpath([normalized_path, normalized_boundary]) == normalized_boundary
