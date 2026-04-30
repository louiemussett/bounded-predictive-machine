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

## Proposed Documentation Structure

The broader technical documentation set should be developed as follows. Each file should use Prototype 3 sources first. Prototype 2 and Prototype 1 sources should be used only as supporting material unless their details are confirmed by Prototype 3.

### `README.md`

Purpose: provide the documentation index, source hierarchy, source precedence rule, reading order, and status of the technical documentation set.

Prototype 3 sources:

- `Source Documents/0. Doc outline.md`
- Root source inventory in `Source Documents/`

Supporting older sources:

- `Source Documents/1-17/00. Future outline.md`
- `Source Documents/1-17/16. First Build Plan.md`

### `01-overview.md`

Purpose: define the current bounded predictive machine architecture, distinguish it from a model, chatbot, generic AI agent, safety wrapper, or memory system, and explain how older prototype sources should be read.

Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/6. Safety as the Outer Shell.md`

Supporting older sources:

- `Source Documents/1-17/0A. Core Cognitive Thesis.md`
- `Source Documents/V0 - V9/0. White Paper.md`

### `02-architecture.md`

Purpose: describe the current architecture, including machine body, boundary, signal flow, prediction, interpretation, belief update, action, memory, safety shell, and first-build shape.

Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting older sources:

- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/V0 - V9/0. White Paper.md`

### `03-core-concepts.md`

Purpose: define the current technical vocabulary: bounded predictive machine, machine body, boundary, signal, prediction, surprise, precision, belief, action, memory, uncertainty, safety shell, and first build.

Prototype 3 sources:

- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting older sources:

- Relevant Prototype 2 A-series concept files in `Source Documents/1-17/`

### `04-cognitive-tick.md`

Purpose: specify the current cognitive loop from expectation through signal, interpretation, evidence quality, belief update, action/no-op, outcome, memory, uncertainty, and next prediction.

Prototype 3 sources:

- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/7. The First Build.md`

Supporting older sources:

- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/16. First Build Plan.md`

Note: the 26-phase tick from Prototype 2 should be treated as supporting detail unless Prototype 3 explicitly adopts that full phase structure.

### `05-machine-body.md`

Purpose: define the current machine body: runtime, files, permissions, memory, sensors, actions, logs, boundary, safety limits, state, trace, and viability.

Prototype 3 sources:

- `Source Documents/3. The Machine Body.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting older sources:

- `Source Documents/1-17/1. Machine Body.md`
- `Source Documents/V0 - V9/1. Foundation.md`

### `06-data-model.md`

Purpose: document the current data-model requirements implied by Prototype 3: records for prediction, signal, interpretation, evidence quality, belief update, action, outcome, memory, uncertainty, and traceability.

Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/7. The First Build.md`

Supporting older sources:

- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/16. First Build Plan.md`

Note: Prototype 2 object families and schema sketches are supporting detail, not final current schemas unless confirmed by Prototype 3.

### `07-safety-model.md`

Purpose: document the current safety shell: boundary, traceability, viability, capability admission, controlled action, recovery, audit, and human review.

Prototype 3 sources:

- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/7. The First Build.md`

Supporting older sources:

- `Source Documents/1-17/15. Relationship to the Safety Canon.md`
- `Source Documents/V0 - V9/5. Controlled Change.md`
- `Source Documents/V0 - V9/6. Viability.md`
- `Source Documents/V0 - V9/7. Interfaces.md`
- `Source Documents/V0 - V9/10. Mature System.md`

### `08-implementation-plan.md`

Purpose: translate the current first-build description into implementation phases while marking inherited Prototype 2 or Prototype 1 specifics as supporting details when not confirmed by Prototype 3.

Prototype 3 sources:

- `Source Documents/7. The First Build.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/6. Safety as the Outer Shell.md`

Supporting older sources:

- `Source Documents/1-17/16. First Build Plan.md`
- `Source Documents/V0 - V9/0. White Paper.md`

### `09-positioning.md`

Purpose: position the current design relative to transformers, GPT, AI agents, predictive processing, active inference, control systems, event-sourced systems, prior prototypes, and cognitive architectures.

Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/0. Human brain and biology.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`

Supporting older sources:

- `Source Documents/1-17/00. White Paper.md`
- `Source Documents/1-17/17. Evaluation for Original Alignment.md`
- `Source Documents/V0 - V9/0. White Paper.md`

### `10-evaluation.md`

Purpose: define how to evaluate whether documentation and future implementation remain aligned with Prototype 3's current design.

Prototype 3 sources:

- `Source Documents/0. Doc outline.md`
- `Source Documents/7. The First Build.md`
- Current-design principles across root `Source Documents/`

Supporting older sources:

- `Source Documents/1-17/14. Developmental Ladder.md`
- `Source Documents/1-17/17. Evaluation for Original Alignment.md`

Note: Prototype 2 maturity gates and alignment scorecards are supporting evaluation detail unless Prototype 3 adopts them directly.

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
