# Data Records

## Purpose

This document defines a proposed minimum record model for the Prototype 3 first
build. The goal is to make the bounded predictive machine's first loop
inspectable, traceable, testable, and reconstructable from records.

This is not final JSON Schema. It is an implementation-facing record model that
identifies the minimum records the first build probably needs in order to prove
the current Prototype 3 loop.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the source of truth for this document. Prototype 2's cognitive
data model, first-build plan, and cognitive tick provide inherited supporting
detail. Their object names, schemas, lifecycle states, and full data model are
not mandatory current requirements unless explicitly adopted by the first-build
implementation.

Prototype 1 material is historical unless a future implementation explicitly
retains it.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/7. The First Build.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/6. Safety as the Outer Shell.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/16. First Build Plan.md`
- `Source Documents/1-17/12. Cognitive Tick.md`

## Why Records Exist

Prototype 3 defines the bounded predictive machine as a trace-governed runtime.
It should be able to show what it expected, what signal arrived, how that signal
was interpreted, what changed, what did not change, what action was considered,
what was allowed, what outcome occurred, and what uncertainty remains.

Records prevent the first build from collapsing into:

- Hidden prompt state.
- Unstructured logs.
- Transcript memory.
- Retrospective explanations.
- Model output treated as truth.
- Action without expected effect.
- Belief update without evidence lineage.

The first build passes only if its loop can be reconstructed from explicit
records.

## Record Categories

### Trace Records

Trace records are evidence of what happened in the runtime. They may record
signal arrival, prediction creation, interpretation, evidence-quality judgment,
belief update, action evaluation, safety checks, outcome observation, failure,
safe mode, or stop.

Trace records are chronological evidence. They are not the same as belief,
memory, or audit.

### Memory Traces

Memory traces reconstruct the meaning of a loop from source records. A memory
trace should preserve the chain from prior belief through prediction, signal,
interpretation, update, action or no-action, outcome, and uncertainty.

Memory is not storage by itself. It should reference source records rather than
replace them.

### State Records

State records describe current runtime state, such as body state, viability,
current belief, runtime mode, or trace-store status.

State records are evidence. They do not directly become belief without
interpretation and evidence-quality review.

### Audit and Loop Records

Audit and loop records link the event chain. A loop or tick record should make
it possible to find all records involved in one first-build loop.

Audit records are useful for review, recovery, debugging, and verification.
They should not become memory summaries unless a memory trace reconstructs from
them.

## Base Fields

Every first-build record should probably have:

- `id`: stable record identifier.
- `record_type`: record type name.
- `created_at`: timestamp.
- `created_by`: runtime component or module.
- `loop_id`: id of the loop or tick that produced the record, if applicable.
- `status`: current record status.
- `source_refs`: upstream records or source material used to produce this
  record.
- `schema_version`: schema or record-format version, if schemas exist.
- `privacy_class`: privacy or exposure class, if privacy classification exists.
- `confidence`: targeted confidence, if relevant.
- `uncertainty`: remaining uncertainty.

These fields are proposed first-build fields, not final JSON Schema. Prototype
2's base-object fields are inherited support for this shape. Prototype 3
requires the evidence discipline; exact field names remain unresolved.

## Minimal First-Build Record Types

### BodyStateRecord

Purpose:

```text
Record the runtime's current operational body state.
```

Should capture:

- Runtime identity.
- Runtime mode.
- Boundary status.
- Config status.
- Trace-store status.
- Sensor status.
- Action registry status.
- Current viability reference.
- Known body uncertainty.

Status:

```text
Proposed first-build record name. Inherited from Prototype 2's richer
MachineBodyState concept, but simplified for Prototype 3.
```

### ViabilityRecord

Purpose:

```text
Record whether the runtime is safe, degraded, critical, failed, or unknown.
```

Should capture:

- Viability state.
- Evidence used for classification.
- Rule or rationale used.
- Action constraints caused by viability.
- Remaining uncertainty.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Exact
transition rules are unresolved.
```

### PredictionRecord

Purpose:

```text
Record what the system expected before evaluating the signal.
```

Should capture:

- Prior belief reference.
- Prediction target.
- Expected signal, state, or outcome.
- Match conditions.
- Mismatch or surprise conditions.
- Evaluation window, if known.
- Confidence and uncertainty.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
PredictionFrame and Prediction objects are inherited supporting detail.
```

### SignalRecord

Purpose:

```text
Record that something arrived from a source or sensor.
```

Should capture:

- Sensor or source id.
- Raw payload reference or safe payload summary.
- Source and boundary status.
- Freshness or timestamp.
- Admissibility status.
- Belief targets the signal may affect.
- Privacy class.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
SignalEnvelope is inherited supporting detail, not a mandatory current schema.
```

### InterpretationRecord

Purpose:

```text
Record candidate meaning derived from a signal.
```

Should capture:

- Signal reference.
- Active prediction reference.
- Primary interpretation.
- Alternative interpretations.
- Interpretation confidence.
- Relevant belief targets.
- Update eligibility.
- Remaining uncertainty.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
InterpretedObservation is inherited supporting detail.
```

### EvidenceQualityRecord

Purpose:

```text
Record how much the evidence should count for each target.
```

Should capture:

- Signal and interpretation references.
- Prediction result: match, mismatch, surprise, partial, or inconclusive.
- Evidence quality by target.
- Reliability limits.
- Reasons the evidence is strong, weak, ambiguous, or inadmissible.
- Whether update is allowed, blocked, or delayed.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
PrecisionEstimate and WeightedPredictionError are inherited supporting detail.
```

### BeliefStateRecord

Purpose:

```text
Record the runtime's current structured model before or after update.
```

Should capture:

- Current task or operating context.
- Body and viability assumptions.
- Recent relevant signals.
- Sensor reliability assumptions.
- Boundary and permission assumptions.
- Allowed actions.
- Known uncertainty.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Exact belief
components are unresolved.
```

### BeliefUpdateRecord or NoUpdateRecord

Purpose:

```text
Record a scoped belief change, or record why no belief update occurred.
```

Should capture for update:

- Prior belief reference.
- Evidence quality reference.
- Specific belief target.
- Previous value or state.
- New value or state.
- Update strength.
- Posterior belief reference.
- Remaining uncertainty.

Should capture for no update:

- Prior belief reference.
- Evidence quality reference.
- Reason update was blocked or unnecessary.
- Uncertainty carried forward.
- Recommended next step, if any.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
BeliefUpdate is inherited supporting detail.
```

### ActionCandidateRecord

Purpose:

```text
Record a possible action considered by the system.
```

Should capture:

- Candidate action name.
- Belief or update that made it relevant.
- Expected effect.
- Preconditions.
- Risks or costs.
- No-action comparison.
- Required capability or permission.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
ActionCandidate is inherited supporting detail.
```

### SafetyCheckRecord

Purpose:

```text
Record the safety-shell review before action.
```

Should capture:

- Action candidate reference.
- Boundary result.
- Permission result.
- Capability admission result.
- Viability result.
- Traceability result.
- Recoverability result.
- Human review requirement.
- Decision: allow, block, delay, clarify, safe mode, or stop.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Exact policy
fields are unresolved.
```

### SelectedActionRecord, NoActionRecord, or BlockedActionRecord

Purpose:

```text
Record the action decision after safety review.
```

Selected action should capture:

- Selected candidate reference.
- Safety-check reference.
- Expected effect.
- Execution status.
- Outcome expectation.

No-action should capture:

- Reason no-action was chosen.
- Whether no-action was safety-driven, evidence-driven, ambiguity-driven, or
  viability-driven.
- Uncertainty carried forward.

Blocked action should capture:

- Blocked candidate reference.
- Blocking safety result.
- Safer replacement, if any.

Status:

```text
Current Prototype 3 concept; proposed first-build record names. Prototype 2
SelectedAction is inherited supporting detail.
```

### OutcomeRecord

Purpose:

```text
Record what happened after an action, blocked action, or no-action.
```

Should capture:

- Selected action, blocked action, or no-action reference.
- Expected effect.
- Attempt result, if an attempt occurred.
- Observed effect.
- Match or mismatch with expected effect.
- Side effects, if known.
- Outcome confidence.
- Unresolved outcome questions.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
ActionOutcome is inherited supporting detail.
```

### MemoryTraceRecord

Purpose:

```text
Reconstruct the loop from source records.
```

Should capture:

- Prior belief reference.
- Prediction reference.
- Signal reference.
- Interpretation reference.
- Evidence quality reference.
- Belief update or no-update reference.
- Action decision reference.
- Outcome reference.
- Uncertainty reference.
- Human-readable reconstruction.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
MemoryTrace is inherited supporting detail.
```

### UncertaintyRecord

Purpose:

```text
Record what remains unknown after the loop.
```

Should capture:

- Target of uncertainty.
- Source records that caused or reduced uncertainty.
- Severity or importance.
- Whether uncertainty blocks update, action, memory, or next prediction.
- Recommended next observation or clarification, if any.

Status:

```text
Current Prototype 3 concept; proposed first-build record name. Prototype 2
metacognitive uncertainty objects are inherited supporting detail.
```

### LoopRecord or TickRecord

Purpose:

```text
Link the records from one complete first-build loop.
```

Should capture:

- Loop id.
- Started and ended timestamps.
- Runtime mode.
- Prior belief reference.
- Prediction reference.
- Signal references.
- Interpretation references.
- Evidence quality references.
- Belief update or no-update references.
- Action decision references.
- Outcome references.
- Memory trace reference.
- Uncertainty references.
- Next prediction reference, if produced.
- Final loop status.

Status:

```text
Current Prototype 3 needs a loop-linking record. `LoopRecord` is the proposed
first-build name. The name `TickRecord` is inherited from Prototype 2 and
useful, but the full Prototype 2 cognitive tick is not mandatory.
```

## Relationship and Linking Rules

The first-build record model should enforce these relationships:

- A `PredictionRecord` must reference a prior `BeliefStateRecord` or explicit
  starting model.
- A `SignalRecord` must identify a source or sensor.
- An `InterpretationRecord` must reference a `SignalRecord`.
- An `EvidenceQualityRecord` must reference the prediction and interpretation
  it evaluates.
- A `BeliefUpdateRecord` must reference prior belief and evidence quality.
- A `NoUpdateRecord` must reference the evidence it refused to use.
- An `ActionCandidateRecord` must reference the belief, update, or uncertainty
  that made the action relevant.
- A `SafetyCheckRecord` must reference an `ActionCandidateRecord`.
- A `SelectedActionRecord` must reference an allowed safety check.
- A `BlockedActionRecord` must reference a failed safety check.
- A `NoActionRecord` must explain why no-action was selected.
- An `OutcomeRecord` must reference the action decision it evaluates.
- A `MemoryTraceRecord` must reference source records; it must not replace
  them.
- An `UncertaintyRecord` must identify the target of uncertainty.
- A `LoopRecord` or `TickRecord` must link the chain.

Rejected shortcuts:

- Signal directly updates belief.
- Signal directly selects action.
- Prediction is invented after signal evaluation.
- Interpretation becomes belief without evidence-quality review.
- Action is selected without expected effect.
- Outcome is assumed from attempted action.
- Memory summarizes without source references.
- Confidence is global rather than target-specific.

## Example Linked Record Chain

This pseudo-JSON shows one complete first-build chain. Field names are
illustrative and not final JSON Schema.

```json
{
  "loop": {
    "id": "loop_0001",
    "record_type": "LoopRecord",
    "status": "completed_with_uncertainty",
    "prior_belief_ref": "belief_0000",
    "prediction_ref": "prediction_0001",
    "signal_refs": ["signal_0001"],
    "interpretation_refs": ["interpretation_0001"],
    "evidence_quality_refs": ["evidence_quality_0001"],
    "belief_update_refs": ["belief_update_0001"],
    "action_decision_refs": ["selected_action_0001"],
    "outcome_refs": ["outcome_0001"],
    "memory_trace_ref": "memory_trace_0001",
    "uncertainty_refs": ["uncertainty_0001"]
  },
  "prediction": {
    "id": "prediction_0001",
    "record_type": "PredictionRecord",
    "source_refs": ["belief_0000"],
    "prediction": "next manual text signal may request another technical documentation file",
    "match_conditions": ["explicit docs/technical target"],
    "uncertainty": ["exact next file unknown"]
  },
  "signal": {
    "id": "signal_0001",
    "record_type": "SignalRecord",
    "source": "manual_text",
    "payload_summary": "create docs/technical/09-data-records.md",
    "boundary_status": "target_inside_docs_technical",
    "admissibility": "admissible_for_task_interpretation"
  },
  "interpretation": {
    "id": "interpretation_0001",
    "record_type": "InterpretationRecord",
    "source_refs": ["signal_0001", "prediction_0001"],
    "primary_meaning": "operator requests creation of the data-records technical document",
    "alternatives": ["operator may expect schema guidance but not final schemas"],
    "confidence": {
      "task_target": "high",
      "final_schema_detail": "low"
    }
  },
  "evidence_quality": {
    "id": "evidence_quality_0001",
    "record_type": "EvidenceQualityRecord",
    "source_refs": ["prediction_0001", "interpretation_0001"],
    "prediction_result": "match",
    "quality_by_target": {
      "current_task": "high",
      "source_precedence": "high",
      "final_json_schema": "low"
    }
  },
  "belief_update": {
    "id": "belief_update_0001",
    "record_type": "BeliefUpdateRecord",
    "source_refs": ["belief_0000", "evidence_quality_0001"],
    "target": "current_task",
    "new_value": "create docs/technical/09-data-records.md",
    "posterior_belief_ref": "belief_0001",
    "uncertainty": ["exact schema fields remain unresolved"]
  },
  "action_candidate": {
    "id": "action_candidate_0001",
    "record_type": "ActionCandidateRecord",
    "source_refs": ["belief_update_0001"],
    "action": "create_file",
    "target": "docs/technical/09-data-records.md",
    "expected_effect": "file exists with proposed minimum record model"
  },
  "safety_check": {
    "id": "safety_check_0001",
    "record_type": "SafetyCheckRecord",
    "source_refs": ["action_candidate_0001"],
    "boundary": "inside_repository_docs_technical",
    "permission": "explicit_user_request",
    "source_documents": "read_only",
    "commit": "not_allowed",
    "decision": "allow"
  },
  "selected_action": {
    "id": "selected_action_0001",
    "record_type": "SelectedActionRecord",
    "source_refs": ["action_candidate_0001", "safety_check_0001"],
    "selected_action": "create_file",
    "expected_effect": "target file can be read back"
  },
  "outcome": {
    "id": "outcome_0001",
    "record_type": "OutcomeRecord",
    "source_refs": ["selected_action_0001"],
    "observed_effect": "file created",
    "pending": ["operator quality review"]
  },
  "memory_trace": {
    "id": "memory_trace_0001",
    "record_type": "MemoryTraceRecord",
    "source_refs": [
      "belief_0000",
      "prediction_0001",
      "signal_0001",
      "interpretation_0001",
      "evidence_quality_0001",
      "belief_update_0001",
      "selected_action_0001",
      "outcome_0001"
    ],
    "reconstruction": "operator requested the data-records document; evidence strongly supported the target file and source constraints; final schemas remain unresolved"
  }
}
```

## Invalid Record Handling

Invalid records must not drive belief update, action, memory reconstruction, or
next prediction.

A record may be invalid when:

- Required fields are missing.
- Source references are missing or broken.
- It claims a belief update without evidence.
- It claims an action without expected effect.
- It claims an outcome without an action decision.
- It treats raw signal as interpretation.
- It lacks privacy or boundary status when required.
- It fails schema validation, if schemas exist.
- It was created outside the allowed boundary.
- Its provenance is unknown.

First-build handling should be fail-closed:

- Mark the record invalid.
- Exclude it from downstream cognition.
- Preserve the failure as trace evidence where possible.
- Increase uncertainty about affected targets.
- Reduce viability if the invalid record affects boundary, trace, schema,
  action, or memory integrity.
- Ask for clarification, enter safe mode, stop safely, or route to review if
  the invalidity blocks safe continuation.

Prototype 2 proposes quarantine records and lifecycle states. Those are useful
inherited support. Prototype 3 has not yet made a final quarantine mechanism
mandatory, so the first build should at least reject invalid records and record
the rejection.

## Relationship to Prototype 2

Prototype 2's `13. Cognitive Data Model.md` provides a rich inherited data
model with object families such as `MachineBodyState`, `SensorModel`,
`SignalEnvelope`, `PredictionFrame`, `InterpretedObservation`,
`PredictionError`, `PrecisionEstimate`, `BeliefState`, `BeliefUpdate`,
`ActionCandidate`, `SelectedAction`, `ActionOutcome`, `MemoryTrace`,
`MetacognitiveState`, `CognitiveTick`, and `AuditTrace`.

This document adopts a smaller first-build naming layer:

- `BodyStateRecord`
- `ViabilityRecord`
- `PredictionRecord`
- `SignalRecord`
- `InterpretationRecord`
- `EvidenceQualityRecord`
- `BeliefStateRecord`
- `BeliefUpdateRecord`
- `NoUpdateRecord`
- `ActionCandidateRecord`
- `SafetyCheckRecord`
- `SelectedActionRecord`
- `NoActionRecord`
- `BlockedActionRecord`
- `OutcomeRecord`
- `MemoryTraceRecord`
- `UncertaintyRecord`
- `LoopRecord` or `TickRecord`

These names are proposed current first-build names. They preserve the
Prototype 3 distinctions while avoiding premature adoption of the full Prototype
2 data model.

Prototype 2 remains useful for later schema expansion, relationship rules,
record lifecycle handling, invalid-record quarantine, privacy classes, and
metacognitive readiness. It should not be treated as mandatory current canon by
default.

## Implementation Risks

- Treating this document as final JSON Schema.
- Implementing the full Prototype 2 data model before the first loop works.
- Using unstructured logs instead of linked records.
- Letting memory traces replace source records.
- Recording prediction after signal interpretation.
- Treating evidence quality as a global confidence score.
- Allowing invalid records to drive belief update.
- Treating a selected action as an observed outcome.
- Omitting no-update, no-action, and blocked-action records.
- Failing to link records into a reconstructable loop.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- Which base fields are mandatory in the first implementation?
- Should `LoopRecord` or `TickRecord` be the current first-build name?
- What id format should records use?
- What record statuses are required for the first build?
- Are JSON and JSONL required, or only recommended?
- What privacy classes are required before the first build can run?
- Which record types need schema validation first?
- Should invalid records be rejected only, or rejected and quarantined?
- What is the minimum viable schema registry?
- How should payload references avoid storing sensitive raw input unnecessarily?
- Should `EvidenceQualityRecord` include numeric scores, categorical labels, or
  both?
- How should uncertainty be represented across belief, memory, and loop
  records?
- Which Prototype 2 object names should be promoted into current schema names
  later?
