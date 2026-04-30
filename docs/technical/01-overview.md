# Overview

## Purpose

This document defines the Bounded Predictive Machine architecture at a technical level using the corrected source hierarchy.

Prototype 3, represented by the root files directly inside `Source Documents/`, is the current design. Prototype 2 in `Source Documents/1-17/` provides supporting prior design detail. Prototype 1 in `Source Documents/V0 - V9/` provides original/historical implementation lineage.

This document summarizes the current design as a bounded predictive cognitive runtime: a machine-runtime architecture that structures machine cognition around boundary, machine body, prediction, signal interpretation, evidence quality, belief update, governed action, reconstructive memory, uncertainty monitoring, and safety containment.

## Source Precedence

When source generations conflict, use this precedence:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting prior design detail: `Source Documents/1-17/`.
3. Prototype 1 original historical implementation lineage: `Source Documents/V0 - V9/`.

Older material must not override newer material. If a concept appears only in Prototype 2 or Prototype 1 and is not confirmed by Prototype 3, it should be labeled as historical, inherited, supporting detail, or unresolved for the current design.

## Sources Used

Current-design sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting prior-design sources:

- `Source Documents/1-17/0A. Core Cognitive Thesis.md`
- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/16. First Build Plan.md`
- `Source Documents/V0 - V9/0. White Paper.md`

## Design Generations

The source material represents three design generations.

Prototype 3 is the current design. It explains the project in terms of a bounded predictive machine that should not begin as a chatbot, generic agent, tool-using assistant, memory database, or safety wrapper. It centers the current loop:

1. Current model.
2. Prediction.
3. Signal.
4. Interpretation.
5. Mismatch or surprise check.
6. Evidence quality check.
7. Belief update.
8. Possible action or no action.
9. Outcome check.
10. Memory.
11. Uncertainty review.
12. Next prediction.

Prototype 2 is a detailed prior design. It expands many current concepts into A-series documents, including a more formal cognitive tick, object sketches, data-model families, developmental gates, and evaluation criteria. These details are useful but should not be treated as current requirements unless Prototype 3 confirms them.

Prototype 1 is the original design and implementation lineage. It describes a bounded trace-driven runtime evolving through V0-V9 stages. It is useful for historical context and possible implementation inspiration, but it is not the current source of truth.

## Architectural Identity

The current design defines the system as a Bounded Predictive Machine.

The most precise technical description is:

> A safety-governed predictive cognitive runtime architecture for bounded machine autonomy.

The architecture is not defined as a neural network, transformer variant, model training method, chatbot, prompt pattern, or tool orchestration framework. It is a runtime-level architecture that governs how a bounded machine receives signals, forms predictions, interprets evidence, judges evidence quality, updates belief, considers action, observes outcomes, writes memory, monitors uncertainty, and remains inside safety constraints.

## Architectural Category

The current architecture belongs to the category of cognitive runtime architecture.

A model architecture answers questions such as:

- How does a model transform input into output?
- How is the model trained?
- What objective does the model optimize?
- What learned representation does the model use?

A cognitive runtime architecture answers different questions:

- What is the system boundary?
- What is the machine body?
- What counts as signal?
- What did the system expect before the signal arrived?
- How is the signal interpreted?
- How reliable is the evidence?
- When may belief change?
- When may action occur?
- How are action outcomes observed?
- How is memory reconstructed from evidence?
- How is uncertainty monitored?
- How is capability governed?

The current design positions the system as pre-agent architecture: it defines structures that should exist before broad agent-like behavior is trusted.

## Core Design Principle

The current design can be summarized by this principle:

> Belief and action should change only through interpreted, evidence-weighted, safety-governed signals.

Prototype 2 states a stronger inherited formulation:

> Belief and action may change only through traceable, precision-weighted, safety-governed evidence.

That Prototype 2 wording is compatible with Prototype 3's direction, but the detailed record and schema implications should be treated as supporting detail until specified in current technical docs.

## Current Runtime Loop

Prototype 3 describes the loop in plain but technically meaningful terms:

1. The system has a current model.
2. The system forms a prediction.
3. A signal arrives.
4. The system interprets the signal.
5. The system compares interpretation against expectation.
6. Mismatch creates surprise or error pressure.
7. The system judges evidence quality, called precision in the current design.
8. The system updates only the belief that the evidence supports.
9. The system considers action only if action is justified and allowed.
10. The system records outcome.
11. Memory preserves the evidence chain.
12. Uncertainty remains visible.

Prototype 2 A12 defines a more formal 26-phase cognitive tick. That phase structure should be treated as supporting prior detail, not an automatically current requirement, unless later Prototype 3 technical docs adopt it.

## System Boundary and Machine Body

The current design begins with the machine body.

The machine body is not biological or anthropomorphic. It is the bounded operational form of the runtime. It includes:

- The running program.
- Files.
- Permissions.
- Memory.
- Sensors.
- Possible actions.
- Logs and traces.
- Configuration.
- Safety limits.
- Health or viability status.

The boundary separates technical access from permission. The system must not treat something as available merely because the host environment can access it. It should treat capabilities, files, tools, and external interfaces as available only when they are inside the boundary or admitted through a governed capability process.

Prototype 2 and Prototype 1 contain deeper body-layer and runtime-root detail. Use those as supporting implementation guidance unless current docs adopt the exact structure.

## Signal Discipline

The current architecture treats input as signal, not truth.

Signals may include:

- User messages.
- Runtime state.
- File or system events.
- Trace results.
- Error reports.
- Sensor readings.
- Action outcomes.
- Memory fragments.
- Model outputs.

A signal must be interpreted before it can affect belief or action. The architecture rejects shortcuts where input directly becomes belief or input directly becomes action.

Prototype 2 adds detailed concepts such as sensor models, signal envelopes, admissibility checks, privacy classes, and precision dimensions. These are useful supporting details, but only the broader signal-discipline principle is confirmed by Prototype 3.

## Prediction, Surprise, and Precision

Prediction means the system has an expectation before new evidence arrives.

Prediction does not mean speculative forecasting. It may include ordinary runtime expectations such as:

- A trace write should succeed.
- The runtime should remain inside boundary.
- A user may request the next document in a known sequence.
- A selected action should produce an observable result.
- A sensor should report within an expected range.

Surprise is mismatch between expectation and interpreted signal. Surprise is not automatically failure, truth, or permission to act. It starts evidence evaluation.

Precision means evidence quality for a specific question. A signal may have high precision for one belief update and low precision for another.

Prototype 2 defines many typed error categories and precision mechanics. Those should be documented as inherited design detail unless Prototype 3 adopts the full taxonomy.

## Belief Update

The current design defines belief as the system's structured working model, not as human-like opinion or feeling.

Belief updates should be:

- Scoped.
- Evidence-weighted.
- Narrow enough to avoid overgeneralization.
- Explicit about remaining uncertainty.
- Connected to what the system expected and what signal arrived.

The system should not update belief directly from raw input, memory summaries, or language model output.

Prototype 2 adds detailed belief-state and belief-update object sketches. These are supporting detail, not final current schemas.

## Action Model

Action is not obedience.

An action is a bounded intervention expected to affect future signal, uncertainty, system state, viability, or error. Before action, the system should be able to identify:

- The candidate action.
- The expected effect.
- Whether the request is clear.
- Whether the action is allowed.
- Whether the action is inside boundary.
- Whether permission exists.
- Whether the result can be observed.
- Whether doing nothing is safer.

No action is a valid choice when the signal is unclear, evidence is weak, permission is missing, the action is unsafe, or the system cannot observe the result.

Prototype 2 expands this into action candidates, success/failure conditions, action thresholds, and action outcome objects. Those are supporting detail unless adopted by Prototype 3 technical specs.

## Memory Model

Memory is not storage.

The current design defines memory as reconstructive and evidence-linked. A memory should preserve the chain of:

- What the system believed.
- What it expected.
- What signal arrived.
- How the signal was interpreted.
- How reliable the evidence was.
- What changed in belief.
- What action was considered or taken.
- What happened afterward.
- What remained uncertain.

Memory must not make past events cleaner or more certain than they were at the time. If the system was uncertain, memory should preserve that uncertainty.

Prototype 2 adds detailed memory-trace and source-lineage object design. Treat that as supporting detail unless current docs adopt specific record formats.

## Safety Shell

The current cognitive core operates inside a safety shell.

The cognitive core evaluates meaning:

- What was expected?
- What happened?
- What does it probably mean?
- Should belief change?
- Should action be considered?
- What should be remembered?

The safety shell governs permission:

- Is this inside boundary?
- Is this allowed?
- Is this traceable?
- Is the system healthy enough?
- Is this capability admitted?
- Can this be recovered if it goes wrong?
- Should a human review this?

The current design keeps the distinction clear:

- The cognitive core decides what may be meaningful.
- The safety shell decides what may be allowed.

Prototype 2 and Prototype 1 contain much more detailed safety/runtime machinery. That machinery should be treated as historical or inherited unless Prototype 3 confirms it.

## Inherited Prototype 2 Details

Prototype 2 adds several detailed concepts that are useful but currently overweighted if treated as mandatory:

- A12's 26-phase cognitive tick.
- A13's full cognitive data model object families.
- A14's developmental ladder.
- A17's original-alignment scorecards and reports.
- Detailed self/other-cause model fields.
- Detailed metacognitive readiness objects.
- Detailed schema/version/lifecycle/quarantine records.

These may become current technical requirements later, but for now they should be labeled as inherited Prototype 2 supporting detail unless Prototype 3 root documents explicitly retain them.

## Historical Prototype 1 Details

Prototype 1 describes an original bounded trace-driven runtime with V0-V9 stages:

- Foundation runtime.
- Adaptive layer.
- Predictive layer.
- Feedback loop.
- Controlled action.
- Viability-aware behavior.
- Interface governance.
- Constrained task system.
- Human interface.
- Mature system operations.

These stages are historical implementation lineage. They may inform implementation planning, but they should not be presented as the current version map unless Prototype 3 adopts them.

## Relationship to AI Agents

The current design explicitly distinguishes this architecture from ordinary AI agents.

A common agent architecture starts with:

- Goal.
- Plan.
- Tool use.
- Memory.
- Task completion.

The Bounded Predictive Machine starts with:

- Boundary.
- Machine body.
- Signal.
- Prediction.
- Interpretation.
- Evidence quality.
- Belief update.
- Safe action or no action.
- Outcome.
- Reconstructive memory.
- Uncertainty monitoring.

Agent-like behavior may be added later, but only after the lower runtime structures exist and capability is governed.

## Relationship to Transformers and LLMs

The architecture is not a transformer competitor.

A transformer model may later be used as an internal component for tasks such as:

- Proposing interpretations.
- Summarizing traces.
- Detecting ambiguity.
- Rendering language.
- Compressing memory records.

The model should not become the owner of belief, action authorization, memory authority, capability admission, safety override, or runtime control.

This principle appears across generations, but the current design states it most simply: the project is not a chatbot, not a language model, and not an agent wrapper.

## First-Build Implication

Prototype 3 says the first build should prove the loop, not intelligence.

The first version should not begin with:

- Chatbot behavior as the core.
- Web browsing.
- Tool use.
- Free-form chat.
- Goal pursuit.
- Broad autonomy.

The first build should instead show:

- What the system believed.
- What it expected.
- What signal arrived.
- What the signal probably meant.
- Whether it matched the expectation.
- How reliable the evidence was.
- Whether belief should update.
- Whether action is justified.
- What action, if any, is allowed.
- What happened after action.
- What should be remembered.
- What remains uncertain.

Prototype 2's first-build plan includes modules, schema files, JSON/JSONL storage, tests, and milestones. Those are useful implementation guidance, but they should remain marked as inherited until Prototype 3 adopts them as current requirements.

## Non-Goals

The current design states that the architecture is not:

- An AI model.
- A neural architecture.
- A transformer variant.
- A chatbot.
- A prompt pattern.
- A generic agent loop.
- A memory database.
- A planning system.
- A safety wrapper alone.
- A consciousness architecture.
- A personality framework.
- A goal-maximizer.
- A tool orchestration system.

These components may exist inside a later system, but they do not define the current architecture.

## Resolved, Inherited, and Unresolved Areas

Resolved by Prototype 3 current design:

- Project identity as a bounded predictive machine.
- Distinction from chatbot, generic agent, memory system, and safety wrapper.
- Core loop from prediction through signal, interpretation, update, action/no-action, memory, uncertainty, and next prediction.
- Machine body and boundary as foundational.
- Signal is not truth.
- Precision as evidence quality.
- Belief update should be scoped and evidence-grounded.
- Action should have expected effect and safety permission.
- Memory should reconstruct the chain.
- Safety shell surrounds the cognitive core.
- The first build should prove the loop, not intelligence.

Inherited or supporting from Prototype 2:

- Full A-series vocabulary.
- Formal cognitive tick phases.
- Cognitive data-model object families.
- Schema sketches and object lineage rules.
- Developmental ladder.
- Original-alignment evaluation framework.
- Detailed first-build implementation plan.

Historical from Prototype 1:

- V0-V9 runtime version ladder.
- Trace-first runtime substrate.
- Adaptive regularity extraction.
- Structured command interface.
- CLI examples.
- Mature system operations.

Still unresolved for the current design:

- Which Prototype 2 schemas and object families are adopted by Prototype 3.
- Final machine-readable schemas.
- Runtime language and framework.
- Boundary, bootstrap, viability, and action-registry file formats.
- Executable safety policy engine.
- General capability-admission protocol.
- Recovery state machine.
- Human approval scoping and command grammar.
