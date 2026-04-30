# Signal, Prediction, and Belief

## Purpose

This document defines the current Prototype 3 evidence pipeline: how signals
enter the bounded predictive machine, how predictions make those signals
evaluable, how interpretation turns signal into candidate meaning, and how
belief may update only when the evidence supports a scoped change.

The goal is to prevent direct shortcuts from input to belief, input to action,
or mismatch to overconfident learning.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the source of truth for this document. Prototype 2 signal,
prediction, interpretation, error, precision, and belief documents provide
inherited supporting detail. Their taxonomies, object lists, and schema sketches
are not mandatory current requirements unless Prototype 3 confirms them.
Prototype 1 material is historical unless directly retained by Prototype 3.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/1. The Big Idea.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/6. Safety as the Outer Shell.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/2. Sensorium and Signal.md`
- `Source Documents/1-17/4. Prediction Frame.md`
- `Source Documents/1-17/5. Interpretation of Signal.md`
- `Source Documents/1-17/6. Prediction Error and Precision.md`
- `Source Documents/1-17/7. Belief State and Belief Update.md`

## Pipeline Summary

The current Prototype 3 evidence pipeline is:

```text
current belief state
-> prediction
-> signal arrival
-> sensor, source, and boundary check
-> interpretation
-> match, mismatch, surprise, or inconclusive result
-> precision / evidence quality
-> scoped belief update or no update
-> uncertainty carry-forward
-> next prediction
```

This pipeline is the learning part of the current loop. It does not by itself
authorize action. Action, if considered, still requires expected effect,
permission, boundary, viability, traceability, and safety-shell review.

## Signal Is Not Truth

A signal is anything the system receives.

Examples include:

- User message.
- Sensor reading.
- File event.
- Trace result.
- System warning.
- Action result.
- Memory fragment.
- Error report.
- Model output.

A signal means:

```text
something arrived from somewhere
```

It does not automatically mean:

- The content is true.
- The content is safe.
- The content is permission.
- The content is a command.
- The content should update belief.
- The content should trigger action.
- The content should be stored as memory.

The current architecture rejects:

```text
signal -> belief
signal -> action
model output -> truth
human message -> unlimited authority
memory fragment -> fact
```

The required path is:

```text
signal
-> source and boundary check
-> interpretation
-> evidence quality
-> possible scoped belief update
```

## Sensor Limits

A sensor is a source or mechanism through which the system receives signals.

Prototype 3 first-build sensors may include:

- Manual text input.
- Clock.
- Runtime status.
- Trace-store status.
- Configuration status.
- Schema validation result.
- Viability status.

Each sensor has limits. A manual text sensor can show what words arrived, when
they arrived, and where they came from. It cannot directly show true intention,
truth of the content, permission to act, safety of the request, or whether
belief should update.

A trace-store sensor may have high evidence quality for whether a trace write
failed, but weaker evidence for why it failed. A schema validation result may
show that a record is invalid, but not by itself establish the cause of the
invalidity.

Prototype 2 defines richer sensor-model and signal-envelope fields such as
freshness, modality, latency, noise, privacy class, cost, precision, and belief
targets. These are useful inherited design concepts, but the current Prototype 3
docs do not yet make a final schema mandatory.

## Source and Boundary Checks

Before a signal can influence belief, the system should check:

- Which sensor produced the signal?
- Is the sensor known and allowed?
- Is the source inside boundary or admitted through a governed capability?
- Is the signal fresh enough for the current question?
- Is the signal allowed for the target belief?
- Does privacy, permission, or capability scope restrict use?
- Can the signal and downstream interpretation be traced?
- Is the current viability state safe enough for normal processing?

Source and boundary checks do not decide meaning. They decide whether the signal
is admissible enough to interpret and route.

If the source is unknown, outside boundary, privacy-blocked, stale,
untraceable, or inadmissible, the system should not use the signal for strong
belief update. It may reject it, quarantine it, record incident evidence, ask
for clarification, route to human review, or choose no update.

## Prediction Before Learning

Prediction means the system has an expectation before evaluating new evidence.

Prototype 3 examples include:

- The trace file should remain writable.
- The next user message may continue the current topic.
- A requested action should produce a certain result.
- A sensor should report a normal value.
- The system should remain inside its boundary.

Prediction matters because learning needs contrast between:

```text
what the system expected
```

and:

```text
what happened
```

If prediction is invented after the signal arrives, the system is explaining
after the fact rather than testing its model. The prediction should therefore
be recorded before signal evaluation.

Prediction is not certainty, desire, goal, or action authorization. It is an
evaluable expectation that makes match and mismatch meaningful.

## Interpretation Before Belief Update

Signal must be interpreted before it can update belief.

Interpretation asks:

- What does the signal probably mean?
- What else could it mean?
- Which prediction is relevant?
- Which belief target might it affect?
- How confident is the interpretation?
- What uncertainty remains?
- Is action relevance present but not yet authorized?

For example:

```text
Signal:
Continue.
```

Possible interpretations:

- Continue the current document.
- Continue the previous argument.
- Continue the sequence.
- Continue from the last stopped point.
- Proceed without asking further questions.
- Provide a low-information acknowledgement.

The system should not treat the raw text as self-explaining. If context is
strong, interpretation may be high confidence. If context is weak, the correct
result may be clarification or no update.

Interpretation is not belief update. It is not action. It is a candidate meaning
that can be compared against prediction.

## Match, Mismatch, Surprise, and Inconclusive Cases

After interpretation, the system compares the interpreted signal with the
prediction.

Results may include:

- Match.
- Partial match.
- Mismatch.
- Early signal.
- Late signal.
- Inconclusive signal.
- Unreliable signal.

Prototype 3 uses surprise to mean mismatch: something happened that did not fit
the prediction. But surprise is not proof. It is the beginning of careful
learning.

Mismatch may indicate:

- The belief model was wrong.
- The signal was noisy.
- The interpretation was wrong.
- The sensor failed.
- The cause is unknown.
- The prediction was too vague.
- The evidence is incomplete.

Inconclusive is a valid result. The system should not force unclear evidence
into match or mismatch merely to keep the loop moving.

## Precision / Evidence Quality

Precision means evidence quality:

```text
how much should this evidence count for this specific question?
```

Evidence quality may depend on:

- Source reliability.
- Sensor reliability.
- Freshness.
- Clarity.
- Relevance.
- Interpretation confidence.
- Alternative interpretations.
- Boundary and admissibility status.
- Privacy constraints.
- Contradictory evidence.
- Trace quality.

Precision is target-specific. A signal can strongly support one update target
while weakly supporting another.

Prototype 2 provides richer precision dimensions such as sensory, temporal,
semantic, causal, action-outcome, memory, and viability precision. Those are
useful inherited terms for future schema design. Prototype 3 currently requires
the general discipline that evidence quality must be judged before belief
update strength is chosen.

## Scoped Belief Update

Belief is the system's structured model of the current situation. It may include
the current task, system state, recent signals, likely user request, sensor
reliability, allowed actions, uncertainty, recent changes, and boundary or
viability information.

A belief update is a controlled change to part of that model.

A good belief update can say:

- This was the prior belief.
- This was the prediction.
- This signal arrived.
- This is how the signal was interpreted.
- This is how reliable the evidence was.
- This specific belief changed.
- This is the new belief.
- This uncertainty remains.

Belief update should be:

- Based on interpreted signal, not raw signal.
- Weighted by evidence quality.
- Scoped to the belief target the evidence supports.
- Traceable.
- Explicit about remaining uncertainty.

For example:

```text
Signal:
Create docs/technical/06-signal-prediction-belief.md.

Valid scoped update:
current_task = create the specified technical documentation file

Invalid broad update:
user always wants all future files in the same structure
```

## No Update

No update is valid and sometimes required.

The system should choose no update when:

- The signal is ambiguous.
- The source is unknown.
- Boundary or permission is unclear.
- The signal is inadmissible.
- Evidence quality is too low.
- The belief target is unclear.
- The proposed update would be too broad.
- Privacy blocks interpretation.
- Trace evidence is missing.
- The system is degraded or critical.

No update does not mean nothing happened. The system may still record
uncertainty, preserve the signal as incident evidence if allowed, ask for
clarification, observe again, or route to review.

## Uncertainty Carry-Forward

Uncertainty is a first-class output of the evidence pipeline.

Uncertainty may increase when:

- Signal source is unclear.
- Sensor quality is weak.
- Interpretation is ambiguous.
- Evidence is stale.
- Prediction result is inconclusive.
- Signals contradict each other.
- Privacy blocks inspection.
- Cause is unknown.
- Outcome cannot be observed.

Uncertainty may decrease when:

- Fresh high-quality evidence arrives.
- Interpretation is strongly supported.
- A prediction match is clear.
- A correction clarifies a specific target.
- Repeated evidence supports a scoped pattern.

The system should carry uncertainty into posterior belief and the next
prediction. It should not erase uncertainty to produce a cleaner story.

## Bad Belief Updates to Avoid

Avoid these update patterns:

- The user said X, so X is true.
- The user corrected one section, so every future section must change.
- One trace succeeded, so the trace system is always reliable.
- One trace failed, so the trace system is permanently broken.
- A model output sounded coherent, so it becomes belief.
- A memory summary says X, so X is fact.
- A command-like signal appeared, so action is authorized.
- A mismatch occurred, so the whole model must be rewritten.
- A prediction matched, so the system understands the cause.
- Missing evidence means the prediction was wrong.

These updates overreach the evidence. They confuse signal, interpretation,
belief, memory, action, and cause.

## Evidence Examples

### High-Quality Evidence

Signal:

```text
User says:
Update only docs/technical/README.md and docs/technical/01-overview.md.
Do not modify Source Documents/.
Do not commit.
```

Why it is high quality:

- Source is the operator's manual text signal.
- Target files are explicit.
- Forbidden areas are explicit.
- Action constraints are explicit.
- The signal is current and task-specific.

Supported update:

```text
current_task = update the two named docs only
boundary_constraint = Source Documents/ is read-only for this task
commit_permission = not granted
```

Remaining uncertainty:

```text
exact wording changes still require source comparison
```

### Low-Quality Evidence

Signal:

```text
The system feels slower after that action.
```

Why it is low quality:

- It may be subjective or indirect.
- The exact metric is unclear.
- Cause is not established.
- Other processes or sensor noise may explain the change.

Possible update:

```text
increase uncertainty about recent action cost
```

Avoid:

```text
recent action caused slowdown
all similar actions are unsafe
```

### Ambiguous Evidence

Signal:

```text
Do it.
```

Why it is ambiguous:

- The referent of `it` may be unclear.
- Multiple actions may be pending.
- The risk level depends on the intended action.
- Approval scope is not explicit.

Possible update:

```text
operator may be approving a pending action
action target is unresolved
```

Preferred result:

```text
ask clarification or choose no-action
```

Avoid:

```text
execute the most likely action automatically
```

### One Signal, Multiple Update Targets

Signal:

```text
User says:
That section is too long.
```

High-quality evidence for:

```text
operator_feedback.current_section_length = too long
```

Moderate evidence for:

```text
current_document_style may need shorter sections
```

Low-quality evidence for:

```text
all future documents should be short
operator dislikes technical detail generally
project documentation should become minimal
```

Valid update:

```text
adjust current section or current document length expectations
```

Invalid update:

```text
rewrite global documentation style permanently
```

### High Precision for State, Low Precision for Cause

Signal:

```text
Trace write failed.
```

High-quality evidence for:

```text
trace_store_state = write_failed
```

Possible evidence for:

```text
viability may be degraded or critical
```

Low-quality evidence for:

```text
disk is broken
permission model is wrong
recent action caused the failure
```

Valid update:

```text
trace availability is currently unreliable
increase uncertainty about cause
restrict nonessential cognition if trace is required
```

Avoid:

```text
assert a root cause without additional evidence
```

## First-Build Examples

### Manual Text Document Request

Current belief:

```text
The user is requesting sequential technical documentation files.
Source Documents/ is read-only reference material.
```

Prediction:

```text
The next manual text signal may request another docs/technical file.
```

Signal:

```text
Create docs/technical/06-signal-prediction-belief.md.
```

Interpretation:

```text
The user requests creation of the evidence-pipeline technical documentation
file.
```

Match result:

```text
Match: the request fits the prediction of another technical documentation file.
```

Evidence quality:

```text
High for current task and target path.
High for not modifying Source Documents/.
Low for final implementation schemas.
```

Scoped belief update:

```text
current_task = create docs/technical/06-signal-prediction-belief.md
```

No broad update:

```text
do not decide final schema design from this request
```

Uncertainty carry-forward:

```text
exact schema fields and thresholds remain unresolved
```

### Trace Failure Signal

Current belief:

```text
Trace writing should normally succeed.
```

Prediction:

```text
The next trace write should produce a valid trace record.
```

Signal:

```text
Trace write failed.
```

Interpretation:

```text
Trace-store failure occurred; cause unknown.
```

Mismatch result:

```text
Mismatch: expected trace write success, observed failure.
```

Evidence quality:

```text
High for trace-store state.
Medium for viability impact.
Low for root cause.
```

Scoped belief update:

```text
trace_store_state = failed or unavailable
viability_model = degraded or critical, depending on current rules
cause = unknown
```

No update:

```text
do not assert disk failure, permission failure, or self-cause without more
evidence
```

Uncertainty carry-forward:

```text
trace failure weakens memory and audit quality until resolved
```

### Ambiguous Continuation Signal

Current belief:

```text
Several possible continuation targets exist.
```

Prediction:

```text
The user may clarify which document or section to continue.
```

Signal:

```text
Continue.
```

Interpretation:

```text
Ambiguous continuation request.
```

Result:

```text
Inconclusive or partial match.
```

Evidence quality:

```text
Moderate for desire to proceed.
Low for exact target.
Low for action authorization if multiple actions are possible.
```

Belief update:

```text
increase uncertainty about intended target
```

No update:

```text
do not set a specific target if the context does not support it
```

Preferred next step:

```text
ask clarification or choose no-action
```

## Relationship to Prototype 2

Prototype 2 is useful inherited support for future implementation design:

- `2. Sensorium and Signal.md` adds sensor models, signal envelopes,
  admissibility, freshness, privacy, cost, and target-specific precision.
- `4. Prediction Frame.md` adds prediction scope, target, evaluation windows,
  match conditions, mismatch conditions, invalidation, and expiration.
- `5. Interpretation of Signal.md` adds interpreted observations, alternatives,
  confidence, update eligibility, and revision.
- `6. Prediction Error and Precision.md` adds typed error, precision dimensions,
  weighted error, and update eligibility.
- `7. Belief State and Belief Update.md` adds belief components, prior and
  posterior belief, update scope, update strength, blocked updates, and
  revision.

These are valuable design directions. They should not be flattened into the
current Prototype 3 canon as mandatory schemas or taxonomies until a current
technical spec adopts them.

## Implementation Risks

- Treating a raw signal as truth.
- Treating manual text as direct command authority.
- Generating predictions after seeing the signal.
- Skipping interpretation.
- Treating surprise as proof.
- Using one global trust score instead of target-specific evidence quality.
- Updating belief too broadly from one correction.
- Ignoring high-quality corrections because they are inconvenient.
- Treating no update as failure.
- Hiding uncertainty to make memory cleaner.
- Promoting Prototype 2 schema sketches to current requirements too early.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- What is the minimal current schema for a signal record?
- Should the first build include signal envelopes, or only simpler signal
  records with source, time, and admissibility?
- What fields are required for a current prediction record?
- How should evidence quality be represented before numeric scoring exists?
- Which Prototype 2 precision dimensions should be promoted first, if any?
- What are the minimal belief components for the first build?
- What update strengths should exist in the first implementation?
- How should no-update decisions be recorded?
- How should uncertainty carry forward between belief states?
- How should privacy-blocked signals affect prediction outcomes and uncertainty?
- What tests should prove that raw signal cannot directly update belief?
