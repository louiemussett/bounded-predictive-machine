# Open Questions

## Purpose

This document collects unresolved technical questions across the current
Prototype 3 documentation set. It is a decision tracker, not a new architecture
specification.

The goal is to make uncertainty explicit before implementation begins. Where
Prototype 2 or Prototype 1 gives useful guidance, this document labels it as
inherited or historical rather than silently treating it as current.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the current source of truth. Prototype 2 can provide inherited
supporting detail. Prototype 1 can provide historical implementation precedent.
Neither older generation should resolve a question automatically unless
Prototype 3 confirms or a current technical decision explicitly adopts it.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/14. Developmental Ladder.md`
- `Source Documents/1-17/16. First Build Plan.md`
- `Source Documents/1-17/17. Evaluation for Original Alignment.md`

Prototype 1/V0-V9 material is historical implementation lineage unless
directly useful as precedent.

## How to Use This Document

Use this document to decide what must be clarified before implementation,
schema work, policy design, testing, or future documentation.

Each question includes:

- Question.
- Why it matters.
- Current best answer, if any.
- Status label.
- Likely source of resolution.

Status labels:

- `unresolved`: no current answer.
- `proposed`: current docs recommend a likely answer, but it is not final.
- `inherited`: Prototype 2 gives useful guidance, but Prototype 3 has not made
  it mandatory.
- `optional`: a valid implementation choice, not a current requirement.
- `blocked`: cannot be resolved until another decision is made.

Resolution sources:

- Prototype 3 decision.
- Implementation experiment.
- Schema design.
- Safety policy.
- User decision.
- Future research.

## Top 10 Decisions Before Implementation

### 1. First-build implementation language

- Question: What programming language should the first implementation use?
- Why it matters: Language choice affects file layout, schema validation,
  test tooling, trace writing, packaging, and runtime constraints.
- Current best answer: Use a small, deterministic implementation stack; no
  specific language is current.
- Status: unresolved.
- Likely source of resolution: user decision.

### 2. JSON/JSONL requirement

- Question: Are JSON and JSONL required, or just recommended first storage
  formats?
- Why it matters: The docs repeatedly use JSON/JSONL examples, but final
  storage contracts are not specified.
- Current best answer: JSON/JSONL are proposed first-build formats, not final
  architecture requirements.
- Status: proposed.
- Likely source of resolution: schema design.

### 3. Minimal schema set

- Question: What schemas are required before the first loop can run?
- Why it matters: Too few schemas weaken auditability; too many schemas risk
  implementing Prototype 2's full data model prematurely.
- Current best answer: Start with records for body, viability, prediction,
  signal, interpretation, evidence quality, belief update/no update, action
  decision, outcome, memory trace, uncertainty, and loop.
- Status: proposed.
- Likely source of resolution: schema design.

### 4. Boundary configuration

- Question: What is the final format for the first-build boundary
  configuration?
- Why it matters: Boundary is the first safety and body constraint.
- Current best answer: It should define project root, read paths, write paths,
  read-only paths, forbidden paths, and default handling for unknown paths.
- Status: proposed.
- Likely source of resolution: safety policy.

### 5. Action registry

- Question: What is the final format for the first-build action registry?
- Why it matters: Action cannot be governed if allowed actions, expected
  effects, permissions, and capability requirements are not explicit.
- Current best answer: The registry should include action name, expected
  effect, boundary requirement, viability requirement, permission/capability
  requirement, and outcome-record requirement.
- Status: proposed.
- Likely source of resolution: safety policy.

### 6. Viability transitions

- Question: What exact rules move the runtime between `safe`, `degraded`,
  `critical`, `failed`, and `unknown`?
- Why it matters: Viability controls whether the system may update, act,
  restrict itself, enter safe mode, or stop.
- Current best answer: Prototype 3 names states; transition rules remain
  unresolved. Prototype 2 gives inherited examples.
- Status: unresolved.
- Likely source of resolution: safety policy.

### 7. Trace failure behavior

- Question: What happens if trace writing fails before the failure itself can
  be traced normally?
- Why it matters: Trace is evidence for memory, audit, and recovery; trace
  failure weakens the whole loop.
- Current best answer: The runtime should shrink capability, preserve failure
  evidence if possible, and move toward safe mode or stop.
- Status: proposed.
- Likely source of resolution: implementation experiment.

### 8. Capability admission

- Question: What is the first-build capability admission process?
- Why it matters: Technical access must not become permission.
- Current best answer: Capability should be defined, scoped, allowed by
  boundary and policy, traceable, monitored, and revocable.
- Status: proposed.
- Likely source of resolution: safety policy.

### 9. Human approval representation

- Question: How should human approval be represented so it remains scoped and
  auditable?
- Why it matters: Human text is signal, not unlimited authority.
- Current best answer: Approval should be interpreted as a scoped signal tied
  to a specific action, boundary, time, and permission context.
- Status: proposed.
- Likely source of resolution: safety policy.

### 10. Loop record name

- Question: Should the current first-build linker be called `LoopRecord` or
  `TickRecord`?
- Why it matters: `TickRecord` connects to Prototype 2 lineage, while
  `LoopRecord` may avoid importing the full 26-phase tick.
- Current best answer: Use `LoopRecord` for the first build unless a current
  decision adopts `TickRecord`.
- Status: proposed.
- Likely source of resolution: schema design.

## Architecture Questions

### A1. What is the minimum current architecture?

- Question: Which components are required for the system to count as a
  Prototype 3 bounded predictive machine?
- Why it matters: Without a minimum, implementation may drift into either
  overbuilding or generic agent behavior.
- Current best answer: Machine body, boundary, prediction, signal,
  interpretation, evidence quality, scoped belief update or no update, action
  or no-action, safety check, outcome, memory trace, uncertainty, and next
  prediction.
- Status: proposed.
- Likely source of resolution: Prototype 3 decision.

### A2. What must remain outside first-build scope?

- Question: Which capabilities should remain explicitly out of scope for the
  first build?
- Why it matters: The source documents warn against starting with chat,
  tools, goals, planning, broad memory, or autonomy.
- Current best answer: Exclude broad tool use, web browsing, external file
  editing, shell execution, autonomous task execution, goals, and long-term
  user memory.
- Status: proposed.
- Likely source of resolution: Prototype 3 decision.

## First-Build Scope Questions

### F1. What must the first build prove?

- Question: What is the first build's pass target?
- Why it matters: The first build should prove structure, not intelligence or
  usefulness.
- Current best answer: It must prove one reconstructable loop from current
  belief through next prediction.
- Status: proposed.
- Likely source of resolution: Prototype 3 decision.

### F2. How much Prototype 2 first-build detail should be used?

- Question: Should Prototype 2's first-build modules and milestones become the
  current implementation plan?
- Why it matters: Prototype 2 is useful but may over-specify the current first
  build.
- Current best answer: Use Prototype 2 as inherited guidance only; adopt
  details explicitly and narrowly.
- Status: inherited.
- Likely source of resolution: implementation experiment.

## Machine Body and Boundary Questions

### B1. What belongs inside the first-build boundary?

- Question: Which files and directories are inside the first-build boundary by
  default?
- Why it matters: The runtime cannot distinguish allowed action from unsafe
  reachability without this.
- Current best answer: `docs/technical/` is an allowed documentation target in
  the current task; `Source Documents/` is read-only reference material.
  Runtime implementation paths remain unresolved.
- Status: unresolved.
- Likely source of resolution: safety policy.

### B2. How should read and write permissions differ?

- Question: How should read permission and write permission be represented
  separately?
- Why it matters: A source can be readable for evidence while forbidden as a
  write target.
- Current best answer: Boundary config should separate allowed reads, allowed
  writes, read-only paths, and forbidden paths.
- Status: proposed.
- Likely source of resolution: schema design.

### B3. What body-state fields are mandatory?

- Question: What exact schema should represent current body state?
- Why it matters: Body state grounds prediction, viability, sensors, and
  action readiness.
- Current best answer: Runtime identity, mode, boundary status, config status,
  trace status, sensor status, action registry status, viability reference, and
  uncertainty are likely required.
- Status: proposed.
- Likely source of resolution: schema design.

## Signal, Prediction, Interpretation, and Belief Questions

### S1. What is the minimal signal record?

- Question: Should the first build use simple `SignalRecord` objects or full
  Prototype 2-style signal envelopes?
- Why it matters: Signal handling must be disciplined, but the first build
  should not import the full Prototype 2 data model by default.
- Current best answer: Use a simple `SignalRecord` with source, payload or
  payload reference, timestamp, boundary/admissibility status, belief targets,
  and uncertainty.
- Status: proposed.
- Likely source of resolution: schema design.

### S2. How should evidence quality be represented?

- Question: Should evidence quality use numeric scores, categorical labels, or
  both?
- Why it matters: Belief updates depend on target-specific evidence quality,
  but premature scoring may create fake precision.
- Current best answer: Start with categorical labels and reasons; numeric
  scoring is optional later.
- Status: proposed.
- Likely source of resolution: implementation experiment.

### S3. What are the minimal belief components?

- Question: What should the first `BeliefStateRecord` contain?
- Why it matters: Belief cannot be hidden prose, but full belief modeling may
  be too large for the first build.
- Current best answer: Current task, boundary assumptions, body/viability
  assumptions, recent relevant signals, allowed actions, sensor reliability
  assumptions, and uncertainty.
- Status: proposed.
- Likely source of resolution: schema design.

### S4. How is no-update recorded?

- Question: How should the runtime record that evidence did not justify belief
  change?
- Why it matters: No update is a valid outcome and prevents overlearning.
- Current best answer: Use `NoUpdateRecord` with prior belief, evidence
  quality reference, reason, uncertainty, and recommended next step if any.
- Status: proposed.
- Likely source of resolution: schema design.

## Action, No-Action, Outcome, and Safety Questions

### AC1. What actions are allowed in the first build?

- Question: Which actions are allowed beyond no-action, trace writing,
  clarification, safe mode, stop, status writing, memory trace writing, and
  bounded response?
- Why it matters: Expanding action too early risks tool-first drift.
- Current best answer: No broader actions are currently confirmed.
- Status: unresolved.
- Likely source of resolution: safety policy.

### AC2. What fields define an action candidate?

- Question: What fields are required for an action candidate in Prototype 3?
- Why it matters: Action must have expected effect and be evaluable.
- Current best answer: Candidate name, source belief/update, expected effect,
  preconditions, risks, no-action comparison, required capability, and
  permission requirement.
- Status: proposed.
- Likely source of resolution: schema design.

### AC3. What makes an outcome sufficiently observed?

- Question: What observation is enough to learn from an action?
- Why it matters: Attempt is not outcome; learning from assumed success would
  corrupt the action model.
- Current best answer: The outcome must reference expected effect, attempt
  result if any, observed effect, and unresolved outcome questions.
- Status: proposed.
- Likely source of resolution: implementation experiment.

### AC4. What is the minimum safety check?

- Question: What safety-shell check must run before a first-build action?
- Why it matters: The system must not act merely because an action is useful or
  requested.
- Current best answer: Check registration, expected effect, boundary,
  permission, capability admission, viability, traceability, observability,
  recoverability, and human review need.
- Status: proposed.
- Likely source of resolution: safety policy.

## Memory, Trace, and Audit Questions

### M1. What is the minimal memory trace format?

- Question: What must a `MemoryTraceRecord` preserve?
- Why it matters: Memory must reconstruct the loop, not just summarize the
  event.
- Current best answer: Prior belief, prediction, signal, interpretation,
  evidence quality, update/no update, action decision, outcome, uncertainty,
  and a human-readable reconstruction.
- Status: proposed.
- Likely source of resolution: schema design.

### M2. What trace quality is required for belief update?

- Question: What minimum trace quality is needed before evidence can update
  belief or form memory?
- Why it matters: Weak or missing trace undermines audit, memory, and recovery.
- Current best answer: Trace should be source-known, linked, valid enough for
  reconstruction, and not privacy-blocked for its intended use.
- Status: unresolved.
- Likely source of resolution: safety policy.

### M3. What retention and deletion rules apply?

- Question: What retention, review, redaction, and deletion rules should apply
  to trace and memory records?
- Why it matters: Memory and trace may contain operator input or sensitive
  source references.
- Current best answer: Prototype 3 requires source-backed memory and safety;
  retention policy is not specified.
- Status: unresolved.
- Likely source of resolution: safety policy.

## Data Record and Schema Questions

### D1. Which base fields are mandatory?

- Question: Which base fields must appear on every first-build record?
- Why it matters: Consistent base fields make records linkable and auditable.
- Current best answer: `id`, `record_type`, `created_at`, `created_by`,
  `status`, `source_refs`, `loop_id`, uncertainty, and schema version are
  proposed.
- Status: proposed.
- Likely source of resolution: schema design.

### D2. How should ids be generated?

- Question: What id format should records use?
- Why it matters: Record chains need stable references that do not depend on
  prose titles.
- Current best answer: Use stable typed ids; exact format is unresolved.
- Status: unresolved.
- Likely source of resolution: schema design.

### D3. Should invalid records be rejected or quarantined?

- Question: Should invalid records be rejected only, or rejected and
  quarantined?
- Why it matters: Invalid records should not drive cognition, but failure
  evidence may still matter.
- Current best answer: Reject invalid records from downstream cognition;
  quarantine is inherited Prototype 2 guidance and likely useful.
- Status: inherited.
- Likely source of resolution: implementation experiment.

## Viability and Recovery Questions

### V1. What are exact viability transition rules?

- Question: What evidence causes `safe`, `degraded`, `critical`, `failed`, or
  `unknown`?
- Why it matters: Viability affects update, action, recovery, and stop
  decisions.
- Current best answer: Prototype 3 names the states. Prototype 2 suggests
  inherited rules around boundary, trace, config, and schema failures.
- Status: unresolved.
- Likely source of resolution: safety policy.

### V2. What recovery actions are allowed?

- Question: What recovery actions are allowed when trace, boundary,
  configuration, or schema validation fails?
- Why it matters: Recovery must not rewrite history, guess protected config, or
  expand capability to fix itself.
- Current best answer: Preserve evidence, shrink capability, ask for review,
  enter safe mode, or stop safely. Exact recovery state machine is unresolved.
- Status: unresolved.
- Likely source of resolution: safety policy.

## Capability Admission and Permission Questions

### C1. What is the first capability admission protocol?

- Question: How does a possible capability become admitted for use?
- Why it matters: Capability growth is the main path to unsafe drift.
- Current best answer: Define, scope, register, permission-check, trace,
  monitor, make revocable, and bind to allowed actions.
- Status: proposed.
- Likely source of resolution: safety policy.

### C2. Which capabilities are explicitly not admitted?

- Question: Which technically available capabilities should be blocked in the
  first build?
- Why it matters: Technical access is not permission.
- Current best answer: Network access, broad shell execution, broad external
  file editing, browser use, autonomous task execution, self-modification, and
  long-term user memory are not current first-build capabilities.
- Status: proposed.
- Likely source of resolution: Prototype 3 decision.

## Human Approval and Command-Scope Questions

### H1. What counts as scoped approval?

- Question: How should approval be represented so it applies only to the
  intended action?
- Why it matters: Human approval must not become unlimited permission.
- Current best answer: Approval should cite signal, interpretation, action
  candidate, boundary, time or loop, and allowed effect.
- Status: proposed.
- Likely source of resolution: safety policy.

### H2. Is there a command grammar?

- Question: Should the first build define a structured command grammar?
- Why it matters: Prototype 1 includes a historical structured command
  channel, but Prototype 3 treats human text as signal first.
- Current best answer: No current command grammar is specified. Use manual
  text as signal in the first build.
- Status: unresolved.
- Likely source of resolution: user decision.

## Implementation Language and Storage Questions

### I1. What language and framework should be used?

- Question: Should implementation begin in Python, JavaScript/TypeScript, or
  another language?
- Why it matters: Runtime, test, schema, and packaging decisions depend on it.
- Current best answer: Keep the first implementation small and deterministic;
  no language is current.
- Status: unresolved.
- Likely source of resolution: user decision.

### I2. What storage backend should be used?

- Question: Should first-build records use files, SQLite, a database, or an
  event store?
- Why it matters: Storage affects audit, recovery, performance, and schema
  validation.
- Current best answer: Plain files with JSON/JSONL are proposed for the first
  build; other storage is optional future work.
- Status: proposed.
- Likely source of resolution: implementation experiment.

## Testing and Evaluation Questions

### T1. What is the first-build test runner?

- Question: What tool and reporting format should run first-build tests?
- Why it matters: Pass/fail criteria need executable checks, not only prose.
- Current best answer: Unresolved until implementation language is chosen.
- Status: blocked.
- Likely source of resolution: user decision.

### T2. Which negative tests are mandatory?

- Question: Which negative tests must pass before the first build is accepted?
- Why it matters: The architecture is defined as much by rejected shortcuts as
  by positive behavior.
- Current best answer: Mandatory candidates include raw signal to belief,
  raw signal to action, retrospective prediction, invalid record downstream
  use, unregistered action, trace failure ignored, and attempted write to
  read-only source material.
- Status: proposed.
- Likely source of resolution: safety policy.

### T3. Should original-alignment reporting be required?

- Question: Should Prototype 2's original-alignment report become a required
  evaluation artifact?
- Why it matters: Alignment reporting can prevent drift, but may overburden
  the first build.
- Current best answer: Use as inherited guidance first; decide after the first
  loop exists.
- Status: inherited.
- Likely source of resolution: Prototype 3 decision.

## Prototype-Lineage / Adoption Questions

### L1. Which Prototype 2 object names should be promoted?

- Question: Which Prototype 2 object names should become current schema names?
- Why it matters: Names such as `SignalEnvelope` and `CognitiveTick` carry
  useful lineage but may imply full Prototype 2 machinery.
- Current best answer: Use simpler first-build names unless explicitly
  adopting the richer concept.
- Status: proposed.
- Likely source of resolution: schema design.

### L2. Should any V0-V9 sequence be retained?

- Question: Does Prototype 3 preserve any part of Prototype 1's V0-V9 version
  sequence as an official roadmap?
- Why it matters: V0-V9 is useful historical lineage but not current by
  default.
- Current best answer: Treat V0-V9 as historical implementation inspiration.
- Status: optional.
- Likely source of resolution: Prototype 3 decision.

### L3. How should older details be adopted?

- Question: What exact process promotes older prototype detail into current
  architecture?
- Why it matters: Without an adoption process, inherited detail may become
  current accidentally.
- Current best answer: A current doc should name the older detail, adoption
  scope, status change, and unresolved limits.
- Status: proposed.
- Likely source of resolution: Prototype 3 decision.

## Positioning and Naming Questions

### P1. What is the standard architecture name?

- Question: Should the project standardize on bounded predictive machine,
  bounded predictive cognitive runtime, or safety-governed predictive
  cognitive runtime?
- Why it matters: Naming affects how the architecture is compared with models,
  agents, safety systems, and cognitive architectures.
- Current best answer: Use "Bounded Predictive Machine" as the short name and
  "bounded predictive cognitive runtime" as the technical name.
- Status: proposed.
- Likely source of resolution: user decision.

### P2. How should predictive-processing influence be cited?

- Question: How should future docs cite predictive processing and active
  inference without implying biological or mathematical equivalence?
- Why it matters: The design is inspired by those ideas but is not a brain
  theory or full active-inference implementation.
- Current best answer: Say "predictive-processing-inspired machine runtime"
  and explicitly deny biological implementation claims.
- Status: proposed.
- Likely source of resolution: future research.

### P3. What role may an LLM play?

- Question: What role, if any, may an LLM play in the first implementation?
- Why it matters: The source docs repeatedly warn against making an LLM the
  cognitive core.
- Current best answer: No LLM is required for the first build. Later, an LLM
  may be a bounded component for interpretation proposals, summaries, or
  language rendering.
- Status: proposed.
- Likely source of resolution: Prototype 3 decision.

## Priority Decision List

Resolve these first:

1. Implementation language.
2. First-build storage format.
3. Minimal schema set.
4. Boundary configuration format.
5. Action registry format.
6. Viability transition rules.
7. Trace failure behavior.
8. Capability admission protocol.
9. Human approval representation.
10. Required negative tests.

Resolve these after the first loop exists:

1. Whether to use `LoopRecord` or `TickRecord`.
2. Which Prototype 2 object names to promote.
3. Whether quarantine is required.
4. Whether original-alignment reporting is mandatory.
5. Which Prototype 1 implementation ideas should be retained.
6. Whether any LLM component should be admitted.
