# Current Architecture

## Purpose

This document describes the current Prototype 3 architecture of the Bounded Predictive Machine.

Prototype 3 is the source of truth for this document. Prototype 2 and Prototype 1 are used only as supporting design history where useful.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Older prototype details must not be treated as current requirements unless Prototype 3 confirms them. When an older detail is useful but not confirmed by Prototype 3, this document labels it as inherited, historical, optional, or unresolved.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting older sources:

- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/15. Relationship to the Safety Canon.md`
- `Source Documents/V0 - V9/0. White Paper.md`

## Architectural Identity

The current architecture is a bounded predictive cognitive runtime.

It is not:

- A language model.
- A transformer variant.
- A chatbot.
- A generic AI agent.
- A prompt pattern.
- A memory database.
- A planning system.
- A safety wrapper alone.
- A tool orchestration system.

Its core concern is not how a model generates text. Its core concern is how a bounded machine runtime receives signals, predicts, interprets evidence, updates belief, chooses action or no action, preserves memory, monitors uncertainty, and remains governed by safety constraints.

## Current Architectural Claim

Prototype 3 defines the system around this claim:

> A machine should not be made powerful first and disciplined later. It should begin with boundary, prediction, evidence, uncertainty, careful updating, safe action, and traceable memory.

The system is current-design aligned when it can show:

- What it is operationally.
- What it can sense.
- What it expected.
- What signal arrived.
- How the signal was interpreted.
- How reliable the evidence was.
- What belief changed, if any.
- Whether action was justified.
- What happened after action.
- What should be remembered.
- What remains uncertain.

## Architecture at a Glance

The current architecture can be summarized as:

```text
machine body and boundary
-> prediction
-> signal
-> interpretation
-> mismatch / surprise
-> evidence quality
-> scoped belief update
-> action candidate or no action
-> safety check
-> outcome observation
-> reconstructive memory
-> uncertainty review
-> next prediction
```

This is the current Prototype 3 loop. Prototype 2's 26-phase cognitive tick is inherited supporting detail, not a mandatory current phase structure.

## Machine Body

The machine body is the bounded operational form of the system.

In Prototype 3, the machine body includes:

- The running program.
- Files.
- Memory.
- Configuration.
- Permissions.
- Sensors.
- Possible actions.
- Logs and traces.
- Safety boundaries.
- Health or viability status.

The machine body answers the first practical question:

> What is the system, operationally?

Before the system predicts, learns, remembers, acts, uses tools, or handles broad tasks, it must know its own operating limits.

## Boundary

Boundary is a foundational part of the machine body.

The boundary answers:

- What belongs to this runtime?
- What is outside this runtime?
- What may the system read?
- What may the system write?
- What must the system never touch?
- Which actions are inside the system's allowed area?

The current architecture treats technical access as different from permission. The system must not reason:

```text
I can access it, therefore it is mine.
```

It must instead ask:

```text
Is this inside my boundary?
Is this capability admitted?
Is this action allowed?
Is this safe to do?
```

Prototype 1 includes a historical bounded-root runtime implementation lineage. That lineage may inspire future implementation, but Prototype 3 does not currently require the exact V0-V9 runtime path.

## Sensors and Signals

The system receives signals through sensors.

Prototype 3 examples of possible first-version sensors include:

- Manual text input.
- Clock.
- Runtime status.
- Trace-store status.
- Configuration status.
- Schema validation result.
- Viability status.

A signal is not truth. It means something arrived from somewhere.

Signals may include:

- User messages.
- Sensor readings.
- File events.
- Trace results.
- System warnings.
- Action results.
- Memory fragments.
- Error reports.
- Model outputs.

The architecture rejects direct shortcuts such as:

```text
signal -> belief
signal -> action
model output -> truth
human message -> unlimited authority
```

Every meaningful signal must be interpreted before it can update belief or justify action.

## Prediction

Prediction means the system has an expectation before new evidence arrives.

Prototype 3 prediction is practical, not mystical. A prediction might be:

- The trace file should be writable.
- The next user message may continue the current topic.
- A requested action should produce a certain result.
- A sensor should report a normal value.
- The system should remain inside its boundary.

Prediction matters because learning requires contrast between:

- What the system expected.
- What happened.

If prediction is invented only after the signal arrives, the system is explaining after the fact rather than testing its model.

## Interpretation

A raw signal does not teach the system directly. It must be interpreted.

For example, the signal:

```text
Continue.
```

may mean:

- Continue the current document.
- Continue the previous argument.
- Continue the sequence.
- Continue from where the system stopped.
- Continue without asking questions.

The current architecture requires the system to treat that as an interpretation problem, not an automatic command.

The required order is:

```text
signal -> interpretation -> evidence quality -> possible belief update -> possible action
```

Prototype 2 adds inherited detail such as sensor models, signal envelopes, admissibility records, and interpretation objects. Those are useful design vocabulary but are not yet final Prototype 3 implementation requirements.

## Surprise and Mismatch

Surprise means mismatch between expectation and interpreted signal.

A signal may:

- Match the prediction.
- Partly match the prediction.
- Contradict the prediction.
- Arrive too early.
- Arrive too late.
- Be too unclear to judge.
- Come from an unreliable source.

Mismatch is useful because it can drive learning. But mismatch is not automatically truth, failure, or permission to act.

The system should treat surprise as a question:

> What does this mismatch actually tell me?

## Evidence Quality and Precision

Prototype 3 uses precision as the idea of evidence quality:

> How much should this evidence count for this specific question?

A signal can have high precision for one update target and low precision for another.

For example, a user request for a specific document is strong evidence about the current task. It is weaker evidence about global user preferences or future document style.

Precision protects the system from overlearning. A careful update is narrow and scoped to what the evidence supports.

Prototype 2 defines a richer taxonomy of typed prediction errors and precision dimensions. That taxonomy is inherited supporting detail and should not be treated as mandatory unless adopted by later Prototype 3 technical specs.

## Belief State

Belief is not a human-like opinion or feeling.

In Prototype 3, belief means the system's structured working model of what is going on. It may include:

- Current task.
- Current system state.
- Signals that have arrived.
- What the user probably requested.
- Which sensors are reliable.
- Which actions are allowed.
- What remains uncertain.
- What recently changed.

Belief should be inspectable. A human should be able to ask:

- What did the system think was happening?
- Why did it think that?
- What evidence supported it?
- How confident was it?
- What did it not know?

## Belief Update

Belief update means changing part of the system's working model.

Prototype 3 requires belief updates to be:

- Based on interpreted signals, not raw signals.
- Weighted by evidence quality.
- Scoped to the specific belief that evidence supports.
- Traceable enough to explain why the update happened.
- Explicit about remaining uncertainty.

A good belief update can say:

- This was the prior belief.
- This was the prediction.
- This signal arrived.
- This is how the signal was interpreted.
- This is how reliable the evidence was.
- This specific belief changed.
- This is the new belief.
- This uncertainty remains.

A bad belief update overgeneralizes:

```text
The user said X, so X is true.
One action failed, so the action never works.
One correction applies to every future case.
Memory says X, so X must be fact.
```

## Action

Action is not obedience.

In Prototype 3, action is a bounded intervention with an expected effect.

Before acting, the system should ask:

- What action is being considered?
- Is the request clear?
- Is the action allowed?
- Is it inside the system boundary?
- What effect is expected?
- Can the result be observed?
- What could go wrong?
- Is doing nothing safer?
- Should clarification be requested?

If the system cannot say what an action is expected to change, the action is not ready.

## No Action

No action is a valid architectural outcome.

The system should be able to choose no action when:

- The signal is unclear.
- The action is unsafe.
- Permission is missing.
- The system boundary is uncertain.
- The evidence is weak.
- The outcome cannot be observed.
- The system is degraded.

This is central to Prototype 3. A system that always acts is not more mature; it may simply be unable to stop.

## Outcome

Attempt is not outcome.

Prototype 3 separates:

- Selected action.
- Attempted action.
- Expected outcome.
- Observed outcome.
- Unresolved outcome.

For example:

```text
Selected action: write memory trace
Attempt: write operation ran
Outcome: write failed because trace store was unavailable
```

Action learning depends on the observed outcome, not on the system's intention.

## Memory

Memory is not storage.

Prototype 3 defines memory as reconstructive. A good memory preserves the chain of what happened:

- What the system believed before.
- What it expected.
- What signal arrived.
- How the signal was interpreted.
- What error, match, or mismatch occurred.
- How reliable the evidence was.
- What belief changed.
- What action was considered.
- What action happened or did not happen.
- What outcome occurred.
- What uncertainty remained.

Transcript memory is not enough. A transcript can show what was said but fail to show what the system expected, inferred, rejected, updated, or remained uncertain about.

Memory should not make the past cleaner than it was. If the system was uncertain at the time, memory should preserve that uncertainty.

## Uncertainty

Uncertainty is part of the current architecture.

The system should represent states such as:

- Unknown.
- Unclear.
- Low confidence.
- Conflicting evidence.
- Cause not known.
- Action not ready.
- Belief update not justified.
- Memory weak.
- Human review required.

Uncertainty should make the system more careful, not bolder.

Prototype 2 includes detailed metacognitive readiness objects. Those are inherited supporting detail. Prototype 3 confirms the broader requirement that the system should monitor uncertainty and avoid pretending to know more than it knows.

## Safety Shell

The cognitive core operates inside a safety shell.

The cognitive core asks:

- What did I expect?
- What signal arrived?
- What does it mean?
- Should belief change?
- Should I act?
- What happened after action?
- What should I remember?
- What remains uncertain?

The safety shell asks:

- Is this allowed?
- Is this inside the boundary?
- Is this traceable?
- Is the system healthy enough?
- Is this capability admitted?
- Can this be recovered if it goes wrong?
- Should a human review this?

The current design can be summarized as:

```text
The cognitive core decides what may be meaningful.
The safety shell decides what may be allowed.
```

Safety is not the whole project. It does not replace prediction, interpretation, belief update, action, memory, or uncertainty. It provides the conditions under which those processes can happen responsibly.

## Safety Responsibilities

Prototype 3 gives the safety shell responsibility for:

- Boundary enforcement.
- Traceability.
- Viability classification.
- Capability admission.
- Controlled action.
- Scoped human input and approval.
- Recovery.
- Memory and belief safeguards.
- Uncertainty-based caution.

The safety shell prevents shortcuts such as:

- Input directly becomes action.
- Input directly becomes belief.
- Model output becomes truth.
- Memory becomes fact.
- Tool access becomes permission.
- Prediction authorizes action.
- Human approval becomes unlimited permission.
- Recovery rewrites history.
- Uncertainty is ignored.

Prototype 2 and Prototype 1 contain more detailed safety/runtime machinery. Those details are inherited or historical unless current Prototype 3 docs adopt them.

## First-Build Architecture

Prototype 3 says the first build should prove the loop, not intelligence.

The first build should not be:

- A chatbot.
- A general AI agent.
- A goal system.
- A planning system.
- A tool-using assistant.
- A web-browsing system.
- A self-improving system.
- A product demo.

The first build should prove that the system can answer:

- What was my current model?
- What did I expect?
- What signal arrived?
- Where did the signal come from?
- What did the signal probably mean?
- Did it match what I expected?
- How reliable was the evidence?
- Should a belief change?
- Is action justified?
- What action, if any, is allowed?
- What happened after action?
- What should be remembered?
- What remains uncertain?

## First-Build Minimal Components

Prototype 3 implies these minimal architectural components:

- Machine body state.
- Boundary definition.
- Trace or record mechanism.
- Simple sensors.
- Prediction record.
- Signal record.
- Interpretation record.
- Evidence quality record.
- Belief update record.
- Action or no-action record.
- Outcome record.
- Memory trace.
- Uncertainty record.
- Tick or loop record.

Prototype 3 gives illustrative first-build files such as:

- `config/boundary.json`
- `config/bootstrap.json`
- `config/action_registry.json`
- `state/runtime_status.json`
- `state/current_body_state.json`
- `state/current_viability.json`
- `traces/startup.jsonl`
- `traces/events.jsonl`
- basic schemas

These names are current-design examples, not final implementation contracts.

## Older Prototype Details

Prototype 2's 26-phase cognitive tick is inherited supporting detail. It can help refine a future current tick specification, but it should not be treated as mandatory until Prototype 3 adopts it.

Prototype 2's cognitive data model is inherited supporting detail. Its object families and schema sketches are useful, but final current schemas remain unresolved.

Prototype 2's relationship-to-safety document is inherited supporting detail. It clarifies a useful distinction between cognitive core and safety shell, but Prototype 3's safety-shell document remains the current source of truth.

Prototype 1's V0-V9 runtime path is historical implementation lineage. It may inform implementation sequencing, but it is not the current implementation path unless Prototype 3 explicitly adopts it.

## Architectural Gaps and Risks

The current architecture is coherent, but several areas need technical tightening before implementation:

- The current loop is clear conceptually, but its required record formats are not final.
- The term "precision" is defined as evidence quality, but no scoring or classification model is current.
- The safety shell lists responsibilities, but not an executable policy model.
- Capability admission is required, but no formal admission protocol is current.
- Recovery is required, but no recovery state machine is current.
- The relationship between trace records, memory traces, and belief state needs a current data model.
- The first-build file names are examples, not normative schemas.
- The current design references viability states, but exact transition rules are not current.
- Human approval must be scoped, but command and approval grammar are unresolved.

These are not contradictions. They are the next technical documentation and implementation targets.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- Which Prototype 2 cognitive tick phases should be adopted by Prototype 3, if any?
- Which Prototype 2 data-model objects should become current implementation records?
- Should Prototype 3 use JSON/JSONL as an actual requirement or only as an illustrative first-build format?
- What is the minimal current schema set for the first build?
- What are the exact viability state transition rules?
- What does capability admission require in the first build?
- What actions are allowed in the first build beyond no-op, trace writing, clarification, safe mode, stop, and response generation?
- What is the minimum trace quality needed for belief update and memory formation?
- How should human approval be represented so it remains scoped and auditable?
- What recovery actions are allowed when trace, boundary, configuration, or schema validation fails?
