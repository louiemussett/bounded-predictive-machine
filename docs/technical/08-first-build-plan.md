# First Build Plan

## Purpose

This document translates Prototype 3's first-build requirement into an
implementation-facing plan. The first build exists to prove that the bounded
predictive machine can run one careful loop from prior belief, to prediction, to
signal, to interpretation, to scoped update, to action or no-action, to outcome,
to reconstructive memory.

It is not intended to prove intelligence, autonomy, planning, broad tool use, or
product usefulness. It is intended to prove the architecture.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the source of truth for this document. Prototype 2 first-build,
data-model, and tick documents provide inherited implementation detail. Their
schemas, object lists, lifecycle states, and 26-phase tick are not mandatory
current requirements unless Prototype 3 confirms them. Prototype 1 runtime
paths are historical implementation lineage unless directly retained by
Prototype 3.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/7. The First Build.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/0. White Paper.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/16. First Build Plan.md`
- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/12. Cognitive Tick.md`

## First-Build Purpose

The first build should prove that the runtime can answer these questions from
records:

- What was the current model or belief state?
- What did the system predict before evaluating the signal?
- What signal arrived?
- What source and boundary checks applied?
- What did the signal probably mean?
- Did it match, mismatch, or fail to resolve against the prediction?
- How reliable was the evidence for each update target?
- What belief changed, if any?
- Was an action justified?
- Was the action allowed?
- What outcome was observed?
- What memory trace preserves the chain?
- What uncertainty remains?

The smallest successful build is one inspectable loop. It should be possible to
reconstruct the loop without relying on hidden prompt context, unstructured log
text, or a model's unsupported explanation.

## Explicit Non-Goals

The first build is not:

- A chatbot.
- A general AI agent.
- A planning system.
- A goal-pursuing system.
- A tool-using assistant.
- A web-browsing system.
- A long-term user memory system.
- A self-improving system.
- A product demo.
- A full implementation of Prototype 2's 26-phase cognitive tick.
- A full implementation of Prototype 2's cognitive data model.
- A mandatory execution of Prototype 1's V0-V9 runtime path.

The first build should not begin with broad shell execution, network access,
external file editing, background automation, autonomous task execution, or
natural-language command execution. Internal writes for trace, state, memory,
and status records are allowed only if they are inside the declared boundary and
registered as first-build actions.

## Implementation Posture

The first implementation should prefer:

- Small deterministic modules.
- Explicit records.
- Schema validation where schemas exist.
- JSON or JSONL-compatible records.
- Plain trace files before databases.
- Clear failure states.
- No hidden belief state.
- No action without expected effect.
- No memory without source references.

Storage choice is not the core design decision. Prototype 3 requires that the
loop be traceable and reconstructable. Prototype 2's data model gives useful
inherited structure, but exact schema names, field sets, and storage mechanisms
remain unresolved unless promoted later.

## Minimal Repository Layout

The following layout is a proposed first-build implementation shape. It is not
an existing-file requirement and not a final schema contract.

```text
config/
  boundary.json
  bootstrap.json
  action_registry.json
  viability_rules.json

schemas/
  base.schema.json
  body_state.schema.json
  signal.schema.json
  prediction.schema.json
  interpretation.schema.json
  evidence_quality.schema.json
  belief.schema.json
  belief_update.schema.json
  action.schema.json
  outcome.schema.json
  memory_trace.schema.json
  tick.schema.json

state/
  current_body_state.json
  current_viability.json
  current_belief.json
  runtime_status.json

traces/
  events.jsonl
  ticks.jsonl
  signals.jsonl
  predictions.jsonl
  belief_updates.jsonl
  actions.jsonl
  outcomes.jsonl
  memory.jsonl

src/
  body/
  boundary/
  trace/
  viability/
  prediction/
  signal/
  interpretation/
  belief/
  action/
  memory/
  safety/
  loop/

tests/
  first_loop/
  negative/
```

Status of this layout:

- `config/`, `state/`, `traces/`, and a small runtime are current first-build
  needs in Prototype 3.
- `schemas/` is strongly supported by Prototype 3's traceability requirement
  and Prototype 2's inherited data-model detail, but exact schema files are
  unresolved.
- `src/` module names are implementation guidance, not current canon.
- A quarantine area for invalid records is inherited from Prototype 2 and
  remains optional until Prototype 3 specifies invalid-record handling in more
  detail.

## Minimal Machine Body

The first build's machine body should include:

- A runtime identity.
- A declared project boundary.
- Configuration loaded from known paths.
- Current body state.
- Current viability state.
- A minimal current belief state.
- A small sensor registry.
- A small action registry.
- A trace writer.
- A memory-trace writer.
- A safety-shell check before action.

The first machine body does not need broad environment introspection. It only
needs enough body knowledge to decide whether the first loop can run safely and
whether its records can be written.

## Minimal Boundary and Config Files

The first build should have explicit boundary and bootstrap configuration.

`boundary.json` should define, at minimum:

- The project root or runtime root.
- Paths considered inside the first-build boundary.
- Paths that may be read.
- Paths that may be written.
- Paths that are explicitly read-only.
- Paths that are forbidden.
- Default treatment for unknown paths.

`bootstrap.json` should define, at minimum:

- Runtime id or instance id.
- Initial runtime mode.
- Config file locations.
- Trace file locations.
- State file locations.
- Schema version or schema registry location, if schemas are implemented.

`action_registry.json` should define, at minimum:

- Allowed action names.
- Expected effect for each action.
- Required boundary status.
- Required viability status.
- Required capability or permission.
- Whether the action must produce an outcome record.

`viability_rules.json` is recommended but unresolved. Prototype 3 requires
viability classification; it does not yet specify a final rule format.

## Minimal Sensors

Prototype 3 supports a small first sensor set:

- Manual text input.
- Clock or timestamp source.
- Runtime status.
- Trace-store status.
- Config status.
- Schema validation result.
- Viability status.

Each sensor should declare what it can and cannot establish. Manual text can be
strong evidence for what text was provided and weaker evidence for intent,
truth, cause, or permission. Runtime status can be evidence about the running
process, but not about user intent. Trace-store status can be evidence about
whether records can be preserved, but not about semantic task correctness.

Sensors should not be treated as truth. A signal must be wrapped, sourced,
checked, interpreted, and weighted before it can affect belief.

## Minimal Allowed Actions

The first action set should stay small:

- `no_action`: make no external or state-changing move beyond trace-required
  records.
- `write_trace`: write an event or loop trace.
- `write_status`: write runtime, body, or viability status.
- `write_memory_trace`: write a reconstructive memory trace for the loop.
- `ask_clarification`: request a more precise manual text signal.
- `enter_safe_mode`: reduce action scope because viability or traceability is
  unsafe.
- `stop_safely`: stop the loop when continuation is not justified.
- `produce_response`: produce a bounded response when allowed.

Prototype 2 includes additional possible action machinery. That detail is
inherited support. The first build should not add broader actions until the
boundary, action registry, expected effect, outcome observation, and safety
checks are working.

## Minimal Loop Stages

The first build should implement this Prototype 3 loop:

```text
load current belief
-> make prediction
-> receive signal
-> check signal source and boundary
-> wrap signal as evidence
-> interpret signal
-> compare interpretation with prediction
-> classify match, mismatch, surprise, or inconclusive result
-> judge evidence quality / precision
-> apply scoped belief update or no update
-> consider action candidate or no-action
-> run safety-shell check
-> act, ask clarification, stop, enter safe mode, or choose no-action
-> observe outcome
-> write memory trace
-> record remaining uncertainty
-> prepare next prediction
```

Prototype 2's 26-phase cognitive tick is useful inherited detail for dependency
discipline. It should not be implemented as mandatory current structure unless
the first-build team explicitly promotes it after the Prototype 3 loop works.

## Minimal Trace and Memory Records

The first build should produce enough records to reconstruct the loop:

- Body state record.
- Viability record.
- Prediction record.
- Signal record.
- Interpretation record.
- Evidence quality record.
- Belief update or no-update record.
- Action candidate record.
- Safety-shell check record.
- Selected action, blocked action, or no-action record.
- Outcome record.
- Memory trace.
- Uncertainty record.
- Loop or tick record linking the chain.

Prototype 2's cognitive data model proposes a larger object set, including
`MachineBodyState`, `SensorModel`, `SignalEnvelope`, `PredictionFrame`,
`InterpretedObservation`, `PredictionError`, `PrecisionEstimate`,
`BeliefState`, `BeliefUpdate`, `ActionCandidate`, `SelectedAction`,
`ActionOutcome`, `MemoryTrace`, `MetacognitiveState`, `CognitiveTick`, and
`AuditTrace`. These names are inherited implementation guidance. Prototype 3
currently requires the distinctions and traceability, not every object name.

At minimum, each record should carry:

- A stable id.
- Object or record type.
- Timestamp.
- Source or provenance.
- Status.
- Links to upstream records where applicable.
- Relevant confidence or evidence quality.
- Remaining uncertainty.
- Schema version if schemas are implemented.

Exact field names and schema formats are unresolved.

## Viability States

Prototype 3 identifies these viability states:

- `safe`
- `degraded`
- `critical`
- `failed`
- `unknown`

`unknown` is not safe. When viability is unknown, the runtime should shrink
action scope, ask for clarification, enter safe mode, or stop safely depending
on the current safety policy.

A practical first-build interpretation is:

- `safe`: boundary, config, trace writing, required schemas, and required state
  are usable enough to run the loop.
- `degraded`: the loop can continue with reduced confidence or reduced action
  scope.
- `critical`: the loop may preserve evidence and restrict action, but should
  not proceed with normal updates or nonessential actions.
- `failed`: the runtime cannot continue the loop safely.
- `unknown`: there is insufficient evidence to classify viability.

The exact transition rules are unresolved. Prototype 2 suggests useful inherited
rules, such as treating boundary invalidity, trace failure, missing required
configuration, and schema invalidity as safety-relevant. Those should be used as
starting tests, not as final current policy.

## Safety-Shell Checks

Before any selected action executes, the safety shell should check:

- Is the action registered?
- Is the expected effect stated?
- Is the target inside boundary?
- Is the required capability admitted?
- Is permission scoped to this action?
- Is current viability sufficient?
- Can the action be traced?
- Can the outcome be observed?
- Is the action recoverable or safely stoppable?
- Is human review required?

The cognitive core may decide an action is meaningful. The safety shell decides
whether it may be allowed. If the check fails, the runtime should block the
action and choose no-action, clarification, safe mode, stop, or another allowed
fallback.

## First Manual-Text Signal Scenario

This scenario is the recommended first proof.

### Starting State

Current belief:

```text
The runtime is operating inside a declared project boundary.
Manual text input is an admitted sensor.
Trace writing is expected to work.
Allowed first actions are limited to no-action, trace/status/memory writes,
clarification, safe mode, stop, and bounded response.
```

Prediction:

```text
The next signal may be a manual text instruction or clarification request.
It should arrive from the manual text sensor.
It may identify a bounded documentation or runtime task.
```

### Signal

Manual text signal:

```text
Create docs/technical/08-first-build-plan.md.
Do not modify Source Documents/.
Do not commit.
```

Source and boundary check:

```text
Source: manual text input.
Target write path: docs/technical/08-first-build-plan.md.
Read-only reference path: Source Documents/.
Commit action: not permitted because the operator explicitly disallowed it.
```

### Interpretation

Primary interpretation:

```text
The operator requests creation of one technical documentation file inside
docs/technical/, using Source Documents/ only as read-only reference material.
```

Alternative interpretation:

```text
The operator may expect implementation planning content only, not runtime code.
```

Evidence quality:

```text
High for requested target file.
High for Source Documents/ being read-only.
High for no commit.
Moderate for exact depth and schema specificity.
```

### Update and Action

Belief update:

```text
Current task becomes creation of docs/technical/08-first-build-plan.md.
Source Documents/ remains read-only.
No commit is allowed.
Exact schemas remain unresolved.
```

Action candidate:

```text
Create docs/technical/08-first-build-plan.md.
```

Expected effect:

```text
The target file exists and contains a practical first-build plan aligned with
Prototype 3 source precedence.
```

Safety-shell result:

```text
Allowed if the target path is inside docs/technical/, Source Documents/ is not
modified, no dependency installation is needed, no deletion is needed, and no
commit is attempted.
```

Outcome:

```text
File created and read back; user evaluation pending.
```

Memory trace:

```text
Preserve prior belief, prediction, manual signal, interpretation, evidence
quality, belief update, action candidate, safety check, outcome, and remaining
uncertainty.
```

Next prediction:

```text
The next signal may request review, correction, or the next technical document.
```

## Pass Criteria

The first build passes when it can demonstrate:

- One complete loop from prior belief through next prediction.
- Prediction is recorded before signal evaluation.
- Signal is separated from interpretation.
- Interpretation is separated from belief update.
- Match, mismatch, surprise, or inconclusive result is recorded.
- Evidence quality is assessed before belief update.
- Belief update is scoped, or no update is explicitly selected.
- No-action is available as a valid result.
- Any action has an expected effect.
- Safety-shell checks occur before execution.
- Outcome is separated from action attempt.
- Memory reconstructs the loop from source records.
- Uncertainty is carried forward.
- Records can be inspected after the loop.
- Invalid or unsafe conditions block downstream cognition rather than silently
  driving it.

The first build does not need to be impressive. It needs to be reconstructable.

## Failure Criteria

The first build fails if:

- Human input directly becomes action.
- Human input directly becomes belief.
- Prediction is written after the signal is interpreted.
- Raw signal is treated as truth.
- Interpretation is skipped.
- Evidence quality is absent or global.
- Belief update is broad rather than scoped.
- Action lacks expected effect.
- Safety checks occur after action.
- Technical access is treated as permission.
- Outcome is assumed from intent.
- Memory is only a transcript.
- Trace failure is ignored.
- Uncertainty disappears from the record.
- Prototype 2's full tick or data model is treated as mandatory current canon.
- Prototype 1's V0-V9 runtime path is treated as the required implementation
  path.

## Negative Tests

The first build should include negative tests for:

- Invalid or missing boundary configuration.
- Attempted write to `Source Documents/`.
- Attempted commit when no commit is allowed.
- Unknown signal source.
- Manual text that says only `do it` with no clear target.
- Belief update attempted before prediction.
- Belief update attempted from raw signal without interpretation.
- High-confidence update attempted from low-quality evidence.
- Action candidate without expected effect.
- Unregistered action.
- Capability technically available but not admitted.
- Trace store unavailable.
- Invalid schema record used downstream.
- Outcome recorded as success without observation.
- Memory trace without source references.
- Retrospective prediction written after seeing the signal.

These tests should prove that the runtime resists the shortcuts Prototype 3 is
designed to prevent.

## Implementation Risks

Key risks:

- Building a chatbot instead of a loop.
- Starting with an LLM as the core rather than a possible later component.
- Treating trace as ordinary logs.
- Treating schema sketches from Prototype 2 as final current contracts.
- Treating Prototype 1 runtime sequencing as mandatory.
- Making the first build too broad.
- Adding sensors before sensor limits are defined.
- Adding actions before the action registry and expected-effect checks work.
- Treating no-action as failure.
- Treating user approval as unlimited permission.
- Letting memory become unsupported narrative.
- Hiding uncertainty for the sake of clean output.
- Failing open when boundary, trace, config, or viability is unknown.

The safest first implementation is deliberately small. Expansion should happen
only after the loop can prove, from records, why it predicted, updated, acted,
remembered, and remained uncertain.

## Relationship to Older Prototype Material

Prototype 2 provides useful inherited implementation scaffolding:

- `16. First Build Plan.md` offers an illustrative first runtime layout,
  allowed/forbidden actions, pass/fail criteria, and negative tests.
- `13. Cognitive Data Model.md` offers record families and relationship rules
  that can guide schema design.
- `12. Cognitive Tick.md` offers dependency ordering and failure discipline.

These details should support the current first build. They should not flatten
the hierarchy. Prototype 3 defines the current architecture; Prototype 2 helps
make it buildable where Prototype 3 is still underspecified.

Prototype 1 V0-V9 material is historical implementation lineage. It may inspire
future runtime engineering, especially around bounded state, trace, and
developmental sequencing, but it is not the current required path.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- What programming language should the first implementation use?
- Are JSON and JSONL required, or just the recommended first storage format?
- What is the minimal required schema set for Prototype 3?
- Which Prototype 2 object names should be promoted first, if any?
- What exact fields are required on every first-build record?
- How should ids be generated and made stable?
- What is the final format for `boundary.json`?
- What is the final format for the action registry?
- What are the exact viability transition rules?
- How should failed trace writing be handled if the failure cannot be traced
  normally?
- Should invalid records be rejected, quarantined, or both?
- What privacy classes apply to manual text, trace records, and memory traces?
- What is the first-build test runner and pass/fail reporting format?
- What role, if any, may an LLM play in the first build?
- What minimum human-review mechanism is required before capabilities expand?
