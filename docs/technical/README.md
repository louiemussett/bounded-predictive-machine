# Technical Documentation

This directory contains technical documentation for the Bounded Predictive Machine architecture described in `Source Documents/`.

The source material represents three design generations:

- Prototype 3 / current design: root files directly inside `Source Documents/`.
- Prototype 2 design: files inside `Source Documents/1-17/`.
- Prototype 1 / original design: files inside `Source Documents/V0 - V9/`.

Prototype 3 is the current source of truth. Prototype 2 provides supporting prior design detail. Prototype 1 provides original/historical implementation lineage.

## Source Precedence

When source generations conflict, use this precedence:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 design detail: `Source Documents/1-17/`.
3. Prototype 1 original design: `Source Documents/V0 - V9/`.

Older material must not override newer material. If a concept appears only in Prototype 2 or Prototype 1 and is not confirmed by Prototype 3, label it as historical, inherited, supporting detail, or unresolved for the current design.

## Current Design Summary

Prototype 3 defines the project as a bounded predictive machine: a machine-runtime architecture organized around boundary, machine body, signal discipline, prediction, interpreted evidence, precision-weighted belief update, governed action, reconstructive memory, uncertainty monitoring, and a safety shell.

This documentation should preserve the current design while using older generations carefully for lineage and detail. When a detail is not specified by Prototype 3, it should not be treated as current merely because it appears in older prototype material.

## Source Material

The documentation draws from the read-only source set in `Source Documents/`.

### Prototype 3 / Current Design

These files are the current source of truth:

- `Source Documents/0. Doc outline.md`
- `Source Documents/0. Human brain and biology.md`
- `Source Documents/0. White Paper.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

### Prototype 2 / Supporting Prior Design Detail

These files provide detailed prior design material. Use them to clarify Prototype 3 only where they do not contradict the current design:

- `Source Documents/1-17/0A. Core Cognitive Thesis.md`
- `Source Documents/1-17/1. Machine Body.md`
- `Source Documents/1-17/2. Sensorium and Signal.md`
- `Source Documents/1-17/3. Priors and Minimal Starting Model.md`
- `Source Documents/1-17/4. Prediction Frame.md`
- `Source Documents/1-17/5. Interpretation of Signal.md`
- `Source Documents/1-17/6. Prediction Error and Precision.md`
- `Source Documents/1-17/7. Belief State and Belief Update.md`
- `Source Documents/1-17/8. Action as Future Error Management.md`
- `Source Documents/1-17/9. Memory as Reconstruction.md`
- `Source Documents/1-17/10. Self-Model and Other-Cause Model.md`
- `Source Documents/1-17/11. Machine Metacognition.md`
- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/14. Developmental Ladder.md`
- `Source Documents/1-17/15. Relationship to the Safety Canon.md`
- `Source Documents/1-17/16. First Build Plan.md`
- `Source Documents/1-17/17. Evaluation for Original Alignment.md`

Supporting Prototype 2 planning and future-work files are also present in `Source Documents/1-17/`.

### Prototype 1 / Original Historical Implementation Lineage

These files describe the original design and implementation lineage. Use them for historical context, earlier tradeoffs, and optional implementation ideas unless Prototype 3 confirms the detail:

- `Source Documents/V0 - V9/0. White Paper.md`
- `Source Documents/V0 - V9/0A. Overview.md`
- `Source Documents/V0 - V9/1. Foundation.md`
- `Source Documents/V0 - V9/2. Adaptive.md`
- `Source Documents/V0 - V9/3. Predictive.md`
- `Source Documents/V0 - V9/4. Loop.md`
- `Source Documents/V0 - V9/5. Controlled Change.md`
- `Source Documents/V0 - V9/6. Viability.md`
- `Source Documents/V0 - V9/7. Interfaces.md`
- `Source Documents/V0 - V9/8. Tasks.md`
- `Source Documents/V0 - V9/9. Human Interface.md`
- `Source Documents/V0 - V9/10. Mature System.md`

Some duplicate or alternate-numbered Prototype 1 files are present. Treat these as historical source quirks unless later current-design material adopts them.

## Current Documentation Set

### `01-overview.md`

Defines the current architecture at a technical level. It explains what the system is, what it is not, how the three design generations should be interpreted, and which details remain unresolved or inherited rather than confirmed by Prototype 3.

Current-design sources used:

- `Source Documents/0. White Paper.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting prior-design sources used:

- `Source Documents/1-17/0A. Core Cognitive Thesis.md`
- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/16. First Build Plan.md`
- `Source Documents/V0 - V9/0. White Paper.md`

### `02-current-architecture.md`

Describes the current Prototype 3 architecture as the source of truth: machine body, boundary, prediction, signal, interpretation, evidence quality, belief update, action or no-action, outcome, memory, uncertainty, safety shell, and first-build scope.

### `03-core-concepts.md`

Defines the core technical terms used across the documentation set, including bounded predictive machine, machine body, boundary, signal, sensor, prediction, surprise, interpretation, precision, belief, belief update, action, no-action, outcome, memory, uncertainty, safety shell, viability, and capability admission.

### `04-current-loop.md`

Documents the current Prototype 3 loop from current belief through prediction, signal arrival, source and boundary checks, interpretation, match or mismatch, evidence quality, scoped update or no update, action or no-action, safety check, outcome observation, memory trace, uncertainty review, and next prediction.

### `05-machine-body-and-boundary.md`

Defines the current Prototype 3 machine body and boundary model, including runtime identity, project boundary, files and state inside the boundary, configuration, sensors, possible actions, permissions, trace/log layer, viability, safety limits, and the difference between technical access and permission.

### `06-signal-prediction-belief.md`

Explains the current Prototype 3 evidence pipeline: signal as not truth, sensor limits, source and boundary checks, prediction before learning, interpretation before belief update, match/mismatch/inconclusive cases, evidence quality, scoped update, no update, uncertainty carry-forward, and bad belief updates to avoid.

### `07-action-memory-safety.md`

Explains the current Prototype 3 action, memory, and safety model: action as bounded expected effect rather than obedience, no-action, safety-shell checks, capability admission, boundary and permission checks, outcome observation, action learning, reconstructive memory, traceability, and failure cases.

### `08-first-build-plan.md`

Translates Prototype 3's "first build proves the loop" principle into an implementation-facing plan, including minimal repository layout, machine body, boundary/config files, sensors, allowed actions, loop stages, trace and memory records, viability states, safety checks, manual-text scenario, pass/fail criteria, negative tests, risks, and open questions.

### `09-data-records.md`

Defines the proposed minimum first-build record model, including trace records, memory traces, state records, audit/loop records, base fields, minimal record types, linking rules, an example linked record chain, invalid-record handling, and unresolved schema questions.

### `10-prototype-lineage.md`

Explains how the three design generations relate: Prototype 1 as original V0-V9 implementation lineage, Prototype 2 as expanded cognitive prototype and inherited detail, and Prototype 3 as the current design. It also defines conflict-handling rules and citation guidance for future documentation.

### `11-positioning.md`

Positions Prototype 3 relative to GPT and transformer models, ChatGPT-style products, ordinary AI agents, tool orchestration systems, memory systems, safety wrappers, predictive processing, active inference, control systems, cognitive architectures, and event-sourced systems. It distinguishes model architecture from cognitive runtime architecture and avoids overclaiming novelty.

### `12-open-questions.md`

Collects unresolved questions across the current technical documentation set. It is a decision tracker, not a new architecture spec, and organizes questions by architecture, first-build scope, machine body and boundary, evidence pipeline, action and safety, memory and trace, records and schemas, viability and recovery, capability admission, human approval, implementation choices, testing, lineage adoption, and positioning.

## Remaining Work

The current technical-documentation phase is complete enough to support implementation planning. Remaining work should resolve the open decisions without weakening the Prototype 3 > Prototype 2 > Prototype 1 source hierarchy.

- Finalize schemas.
- Choose implementation language.
- Define safety policy.
- Define viability transitions.
- Define capability admission.
- Define human approval representation.
- Create executable tests.
- Decide which Prototype 2 details to adopt.

## Resolved, Inherited, and Unresolved Inputs

The expanded source set provides useful prior detail, but not all prior detail is current.

Resolved by Prototype 3 current design:

- Current project identity as a bounded predictive machine.
- Current distinction from chatbots, generic agents, memory systems, and safety wrappers.
- Current concepts of machine body, boundary, signal, prediction, surprise, precision, belief, action, memory, uncertainty, safety shell, and first build.
- Current first-build principle: prove the loop, not intelligence.

Inherited or supporting from Prototype 2:

- Detailed A-series vocabulary and object sketches.
- Detailed cognitive tick phase structure.
- Detailed cognitive data-model object families.
- Developmental ladder and original-alignment evaluation.
- First-build implementation plan with modules, milestones, and tests.

Inherited or historical from Prototype 1:

- V0-V9 runtime version lineage.
- Trace-first implementation substrate.
- Adaptive, predictive, loop, controlled-action, viability, interface, task, human-interface, and maturity stages.
- CLI and structured-command examples.

Still unresolved for the current design:

- Which Prototype 2 schema sketches are officially adopted by Prototype 3.
- Final machine-readable JSON Schema files.
- Runtime language and framework.
- Boundary, bootstrap, viability, and action-registry file schemas.
- Executable safety policy engine.
- General capability-admission protocol.
- Recovery state machine.
- Human approval scoping and command grammar beyond the current high-level safety-shell description.
