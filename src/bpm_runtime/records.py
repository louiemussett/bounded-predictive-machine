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
    evidence_score: float | None = None
    update_threshold: float | None = None
    score_components: dict[str, object] = field(default_factory=dict)


@dataclass
class BeliefUpdateRecord(BaseRecord):
    update_target: str | None = None
    update_summary: str | None = None
    evidence_quality_used: str | None = None
    evidence_score: float | None = None
    prior_confidence: float | None = None
    posterior_confidence: float | None = None
    confidence_delta: float | None = None
    update_threshold: float | None = None
    score_components: dict[str, object] = field(default_factory=dict)


@dataclass
class NoUpdateRecord(BaseRecord):
    update_target: str | None = None
    no_update_reason: str | None = None
    evidence_quality_used: str | None = None
    evidence_score: float | None = None
    prior_confidence: float | None = None
    posterior_confidence: float | None = None
    confidence_delta: float | None = None
    update_threshold: float | None = None
    score_components: dict[str, object] = field(default_factory=dict)


@dataclass
class ActionCandidateRecord(BaseRecord):
    action_name: str | None = None
    expected_effect: str | None = None
    target_path: str | None = None
    reason: str | None = None


@dataclass
class SafetyCheckRecord(BaseRecord):
    pass


@dataclass
class SelectedActionRecord(BaseRecord):
    pass


@dataclass
class NoActionRecord(BaseRecord):
    reason: str | None = None


@dataclass
class UncertaintyGateRecord(BaseRecord):
    decision: str | None = None
    reason: str | None = None
    allow_belief_update: bool = False
    allow_action: bool = False
    evidence_quality: str | None = None
    interpretation_confidence: str | None = None
    prediction_result: str | None = None


@dataclass
class AbstentionRecord(BaseRecord):
    reason: str | None = None
    gate_decision: str | None = None


@dataclass
class ClarificationRequestRecord(BaseRecord):
    request: str | None = None
    reason: str | None = None


@dataclass
class BlockedActionRecord(BaseRecord):
    pass


@dataclass
class OutcomeRecord(BaseRecord):
    action_ref: str | None = None
    observed_effect: str | None = None
    success: bool | None = None
    unresolved_questions: list[str] = field(default_factory=list)


@dataclass
class MemoryTraceRecord(BaseRecord):
    referenced_record_ids: list[str] = field(default_factory=list)
    reconstruction_summary: str | None = None


@dataclass
class MemoryRetrievalRecord(BaseRecord):
    query: str | None = None
    match_count: int = 0
    matched_record_ids: list[str] = field(default_factory=list)
    matched_record_types: list[str] = field(default_factory=list)


@dataclass
class RetrievedRecordMatch(BaseRecord):
    matched_record_id: str | None = None
    matched_record_type: str | None = None
    match_reason: str | None = None
    matched_fields: list[str] = field(default_factory=list)


@dataclass
class UncertaintyRecord(BaseRecord):
    pass


@dataclass
class LoopRecord(BaseRecord):
    ordered_record_ids: list[str] = field(default_factory=list)
    record_types: list[str] = field(default_factory=list)
