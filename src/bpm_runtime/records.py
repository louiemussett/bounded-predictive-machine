"""Minimal record model for the first-build runtime.

These dataclasses intentionally capture only the common first-build fields.
They are not final JSON Schema.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
from uuid import uuid4


def _new_id() -> str:
    return str(uuid4())


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class BaseRecord:
    """Common fields shared by all first-build records."""

    id: str = field(default_factory=_new_id)
    record_type: str = field(init=False)
    created_at: str = field(default_factory=_now_utc)
    created_by: str = "bpm_runtime"
    loop_id: str | None = None
    status: str = "created"
    source_refs: list[str] = field(default_factory=list)
    uncertainty: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.record_type = self.__class__.__name__

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), sort_keys=True)


@dataclass
class BodyStateRecord(BaseRecord):
    pass


@dataclass
class ViabilityRecord(BaseRecord):
    pass


@dataclass
class BeliefStateRecord(BaseRecord):
    pass


@dataclass
class PredictionRecord(BaseRecord):
    target: str | None = None
    expected: str | None = None
    match_conditions: list[str] = field(default_factory=list)


@dataclass
class SignalRecord(BaseRecord):
    source: str | None = None
    payload: str | None = None
    payload_summary: str | None = None
    boundary_status: str | None = None
    admissibility_status: str | None = None


@dataclass
class InterpretationRecord(BaseRecord):
    primary_interpretation: str | None = None
    alternative_interpretations: list[str] = field(default_factory=list)
    relevant_belief_targets: list[str] = field(default_factory=list)
    interpretation_confidence: str | None = None


@dataclass
class EvidenceQualityRecord(BaseRecord):
    quality_label: str | None = None
    reasons: list[str] = field(default_factory=list)
    update_targets: list[str] = field(default_factory=list)
    prediction_result: str | None = None


@dataclass
class BeliefUpdateRecord(BaseRecord):
    pass


@dataclass
class NoUpdateRecord(BaseRecord):
    pass


@dataclass
class ActionCandidateRecord(BaseRecord):
    pass


@dataclass
class SafetyCheckRecord(BaseRecord):
    pass


@dataclass
class SelectedActionRecord(BaseRecord):
    pass


@dataclass
class NoActionRecord(BaseRecord):
    pass


@dataclass
class BlockedActionRecord(BaseRecord):
    pass


@dataclass
class OutcomeRecord(BaseRecord):
    pass


@dataclass
class MemoryTraceRecord(BaseRecord):
    pass


@dataclass
class UncertaintyRecord(BaseRecord):
    pass


@dataclass
class LoopRecord(BaseRecord):
    pass
