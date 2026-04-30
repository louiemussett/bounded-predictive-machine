# Current Loop

## Purpose

This document defines the current Prototype 3 operating loop for the bounded
predictive machine. It describes the ordered path from current belief state to
next prediction, with safety, uncertainty, and memory preserved across the
cycle.

This is not a full implementation specification. It is the current architectural
loop that future schemas, tests, and runtime code should preserve.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the source of truth for this document. Prototype 2's cognitive
tick and first-build plan are inherited supporting detail. They can clarify
dependencies and failure cases, but they do not make the 26-phase tick mandatory
for the current architecture. Prototype 1 material is historical unless
Prototype 3 explicitly retains the idea.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/7. The First Build.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/6. Safety as the Outer Shell.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/16. First Build Plan.md`

Prototype 1 sources under `Source Documents/V0 - V9/` are treated as historical
implementation lineage unless a current Prototype 3 source confirms the detail.

## Loop Summary

The current Prototype 3 loop is:

```text
current model / belief state
-> prediction
-> signal arrival
-> signal source and boundary check
-> interpretation
-> match, mismatch, or inconclusive result
-> evidence quality / precision
-> scoped belief update or no update
-> action candidate or no-action
-> safety-shell check
-> outcome observation
-> memory trace
-> uncertainty review
-> next prediction
```

The loop exists to prevent shortcuts such as:

- Raw input directly becoming belief.
- Raw input directly becoming action.
- Prediction being invented after the signal.
- Mismatch being treated as truth.
- Action being selected without expected effect.
- Outcome being assumed because an action was attempted.
- Memory becoming a transcript without the reasoning chain.
- Uncertainty being hidden.

## Current Loop Rules

The current loop has these dependency rules:

- Belief state must exist before prediction can be meaningful.
- Prediction must exist before signal evaluation.
- Signal source and boundary must be checked before signal use.
- Signal must be interpreted before belief update.
- Match, mismatch, or inconclusive status must be assessed before update.
- Evidence quality must be judged before update strength is chosen.
- Belief update must be scoped to what the evidence supports.
- No-action must remain available.
- Action must have an expected effect.
- Safety-shell approval must precede execution.
- Outcome must be observed or marked unresolved.
- Memory must preserve the event chain.
- Uncertainty must carry forward.
- The next prediction must be based on the resulting belief and uncertainty.

Prototype 2 describes a richer cognitive tick dependency law. That law is useful
inherited detail, but the current requirement is the Prototype 3 ordering above.

## Stage 1: Current Model / Belief State

The loop begins with the machine's current structured model of what is going on.
This belief state may include:

- Current task.
- Current body state.
- Current viability state.
- Recent signals.
- Sensor reliability.
- Allowed actions.
- Boundary status.
- Trace status.
- Relevant uncertainty.

The belief state is not memory, personality, or model output. It is the current
working model used to make predictions and evaluate signals.

If no belief state can be loaded, the loop should not pretend normal operation.
The correct result may be no-action, safe mode, recovery, or human review.

## Stage 2: Prediction

The system forms an expectation before evaluating new evidence.

A first-build prediction may be simple:

- The trace store should remain writable.
- The system should remain inside its boundary.
- The next manual text signal may continue the current task.
- A requested response action should produce a user-visible response.
- The viability state should remain safe unless a body signal indicates
  otherwise.

Prediction is not certainty and not permission. It gives the system something to
compare against.

The prediction should be recorded. A prediction that exists only after the
signal arrives is retrospective explanation, not a valid predictive loop.

## Stage 3: Signal Arrival

A signal is anything the system receives through a sensor. Prototype 3 first
signals may include:

- Manual text input.
- Runtime status.
- Trace status.
- Configuration status.
- Schema validation result.
- Viability status.

The signal is evidence that something arrived. It is not automatically truth,
permission, instruction, or action authority.

## Stage 4: Signal Source and Boundary Check

Before a signal can be used, the system should check where it came from and
whether it is inside the current boundary and sensor model.

This stage asks:

- Which sensor produced the signal?
- Is that sensor known and allowed?
- Is the signal inside the runtime boundary?
- Is the signal fresh enough to use?
- Is the source allowed for the target belief or action?
- Does privacy, permission, or capability scope restrict use?
- Is the trace system available to preserve evidence?

Prototype 3 does not require a final signal-envelope schema yet. Prototype 2's
signal-envelope and admissibility details are useful inherited design guidance,
but they should not be treated as final current schema requirements.

If source or boundary status is invalid, the loop should block belief update and
action from that signal. It may record an incident, ask for review, enter safe
mode, or choose no-action.

## Stage 5: Interpretation

The system assigns possible meaning to the signal before using it.

Interpretation should preserve:

- Likely meaning.
- Alternative meanings.
- Confidence.
- Relevant prediction.
- Possible belief target.
- Ambiguity.
- Remaining uncertainty.

For example, the signal `Continue.` may mean continue the current document,
continue the prior argument, continue a sequence, continue from the last stopped
point, or proceed without asking further questions. The system should not treat
that text as self-explaining.

Interpretation is not belief update. It is not safety approval. It is the bridge
between raw signal and possible update.

## Stage 6: Match, Mismatch, or Inconclusive Result

The interpreted signal is compared against the prediction.

The result may be:

- Match.
- Partial match.
- Mismatch.
- Early signal.
- Late signal.
- Inconclusive signal.
- Unreliable signal.

Prototype 3 uses surprise to mean mismatch between expectation and signal, but
it also preserves inconclusive cases. The loop should not force every result
into right or wrong.

Mismatch is useful information. It is not proof that the signal is true, proof
that the prior belief is false, or permission to act.

## Stage 7: Evidence Quality / Precision

The system judges how much the interpreted signal should count for the specific
question at hand.

Evidence quality may consider:

- Source reliability.
- Sensor reliability.
- Freshness.
- Clarity.
- Relevance to the belief target.
- Ambiguity.
- Whether the signal is direct or indirect.
- Whether the signal is sufficient for action.

Evidence can be high precision for one target and low precision for another.
For example, a user saying `Create 04-current-loop.md` is strong evidence about
the current task, weaker evidence about future documentation preferences, and no
evidence by itself that file creation is safe in all contexts.

Prototype 2 offers richer precision and typed-error detail. That detail is
inherited and may inform future schemas, but Prototype 3 currently requires the
general evidence-quality judgment rather than a fixed scoring model.

## Stage 8: Scoped Belief Update or No Update

If evidence quality supports an update, the system updates only the belief that
the evidence justifies.

A scoped belief update should preserve:

- Prior belief.
- Prediction.
- Signal.
- Interpretation.
- Evidence quality.
- Target belief.
- Update strength.
- Posterior belief.
- Remaining uncertainty.

No update is valid when:

- The signal is ambiguous.
- The source is inadmissible.
- Evidence quality is too weak.
- The belief target is unclear.
- The update would be too broad.
- The system cannot preserve a trace.
- Boundary or viability state blocks continued cognition.

The loop should not update global beliefs from local evidence.

## Stage 9: Action Candidate or No-Action

After belief update, or after deciding not to update, the system may consider
action.

An action candidate should have:

- Action name.
- Expected effect.
- Reason for considering it.
- Required capability.
- Boundary scope.
- Risk.
- Traceability.
- Observable outcome.
- Relevant uncertainty.

Current Prototype 3 first-build actions are limited. Examples include:

- Do nothing.
- Write a trace.
- Write a status record.
- Write a memory trace.
- Ask for clarification.
- Enter safe mode.
- Stop safely.
- Produce a response.

No-action is not failure. It is the correct result when action is unclear,
unsafe, unsupported, untraceable, outside boundary, or blocked by uncertainty.

## Stage 10: Safety-Shell Check

The safety shell governs whether an action candidate may proceed.

It asks:

- Is the action registered?
- Is the action allowed?
- Is the capability admitted?
- Is the action inside boundary?
- Is permission valid and scoped?
- Is the system viable enough?
- Can the action be traced?
- Can the outcome be observed?
- Is recovery possible if the action fails?
- Should human review be required?

The cognitive core may decide an action is meaningful. The safety shell decides
whether it is allowed.

If safety checks fail, the system should block the action and select no-action,
ask for clarification, enter safe mode, stop, or route to human review.

## Stage 11: Outcome Observation

Outcome is what actually happened after the selected action or no-action.

The loop should keep separate:

- Action candidate.
- Selected action.
- Attempted action.
- Expected outcome.
- Observed outcome.
- Unresolved outcome.

For example:

```text
Selected action: write trace
Expected outcome: valid trace record exists
Observed outcome: trace write failed
```

The system should learn from observed outcome, not from intention. If outcome
cannot be observed, that uncertainty should be recorded.

## Stage 12: Memory Trace

Memory preserves the event chain.

A memory trace should be reconstructive. It should preserve enough information
to answer:

- What did the system believe before?
- What did it predict?
- What signal arrived?
- Where did the signal come from?
- How was it interpreted?
- Did it match, mismatch, or remain inconclusive?
- How reliable was the evidence?
- What belief changed, if any?
- What action was considered?
- What action was taken or not taken?
- What outcome occurred?
- What uncertainty remained?

Memory is not transcript storage. It should not make the event cleaner or more
certain than it was.

## Stage 13: Uncertainty Review

Before the loop completes, the system reviews uncertainty.

Uncertainty may concern:

- Signal meaning.
- Source reliability.
- Boundary status.
- Viability state.
- Evidence strength.
- Belief update strength.
- Action readiness.
- Outcome success.
- User satisfaction.
- Memory completeness.
- Cause of a failure.

Uncertainty should constrain future action. It may reduce confidence, block a
belief update, require clarification, force no-action, or move the runtime into
a more restricted state.

Unknown is not safe.

## Stage 14: Next Prediction

The loop ends by preparing the next prediction from the resulting belief state,
memory trace, outcome, and uncertainty.

The next prediction may include:

- Expected continuation of the current task.
- Expected user feedback.
- Expected trace availability.
- Expected viability state.
- Expected result of a pending action.
- Expected need for clarification.

The posterior belief becomes the prior for the next loop. This creates
continuity without pretending the system is certain.

## Example First-Build Loop: Manual Text Signal

This example uses a simple manual text signal. It is illustrative, not a final
schema.

```text
1. Current model / belief state
   The system is operating inside a valid project boundary.
   Trace writing is available.
   Current task context is technical documentation.
   The user has been requesting sequential docs/technical files.

2. Prediction
   The next manual text signal may request another technical documentation file.

3. Signal arrival
   Manual text signal arrives:
   "Create docs/technical/04-current-loop.md."

4. Signal source and boundary check
   Source is manual text input from the operator.
   Target path is inside the project boundary.
   Requested action is file creation under docs/technical/.
   Source Documents/ remains read-only by instruction.

5. Interpretation
   Likely meaning:
   the user requests creation of the current-loop technical documentation file.

   Alternative meaning:
   the user may be asking for a draft rather than a committed repository change.

   Confidence:
   high, because the instruction explicitly names the file and constraints.

6. Match, mismatch, or inconclusive result
   Match:
   the signal matches the prediction that the user may request the next
   technical documentation file.

7. Evidence quality / precision
   High precision for current task and target file.
   High precision for read-only treatment of Source Documents/.
   Low precision for future implementation schemas.

8. Scoped belief update or no update
   Update current task:
   create docs/technical/04-current-loop.md.

   Do not update:
   global future documentation structure beyond this file.

9. Action candidate or no-action
   Candidate:
   create the requested documentation file.

   Expected effect:
   docs/technical/04-current-loop.md exists and contains Prototype 3-first loop
   documentation.

10. Safety-shell check
   Action is inside repository boundary.
   Action modifies docs/technical/, not Source Documents/.
   No dependency, deletion, network access, or commit is required.
   Action is traceable by file diff or readback.

11. Outcome observation
   File creation succeeds or fails.
   If created, content is read back for hierarchy and terminology checks.

12. Memory trace
   Record the prediction, signal, interpretation, action, outcome, and
   uncertainty in the documentation history or trace system when one exists.

13. Uncertainty review
   Current uncertainty remains around final schema names, evidence-quality
   thresholds, and exact safety-shell enforcement.

14. Next prediction
   The user may request review, revision, or the next technical documentation
   file.
```

The visible action in this example is writing documentation. In a first runtime
implementation, the same loop should be represented as structured records rather
than only prose.

## Failure Cases

### Ambiguous Manual Text

Signal:

```text
Do it.
```

If several possible actions are pending, the loop should not guess.

Expected handling:

- Interpret the signal as an ambiguous command candidate.
- Mark the prediction result as inconclusive or partial.
- Assign low evidence quality for exact action selection.
- Block strong belief update.
- Select ask-clarification or no-action.
- Preserve uncertainty in memory.

This is a successful loop because it avoids unsafe action from weak evidence.

### Boundary Uncertain

Signal:

```text
Create a file outside the project.
```

Expected handling:

- Treat the request as a manual text signal, not permission.
- Check target against boundary.
- Mark action as outside boundary or boundary-uncertain.
- Block action.
- Choose no-action, ask for clarification, or route to human review depending
  on policy.
- Preserve the blocked action and reason in trace or memory.

Technical access does not equal permission.

### Trace Failure

Signal:

```text
Trace write failed.
```

Expected handling:

- Interpret as trace-state evidence.
- Compare against prediction that trace writing should succeed.
- Mark mismatch.
- Treat evidence quality as high for trace failure, but low for root cause
  unless additional evidence exists.
- Update viability to critical or degraded as appropriate.
- Block nonessential action.
- Enter safe mode, stop, or request human review.
- Preserve failure evidence if any trace path remains available.

Trace failure is not a minor logging issue. It weakens belief, memory, recovery,
and auditability.

### Low Evidence Quality

Signal:

```text
The previous output felt wrong.
```

Expected handling:

- Interpret as negative feedback with unclear target.
- Mark evidence as useful but under-specified.
- Avoid broad belief update.
- Ask what was wrong or update only a narrow uncertainty field.
- Choose clarification or no-action rather than rewriting global style rules.

The system should not overlearn from underspecified feedback.

### Safety-Shell Rejection

Action candidate:

```text
Read all local files to improve context.
```

Expected handling:

- Recognize the action may be useful but requires file-access capability.
- Check boundary, permission, privacy, traceability, and capability admission.
- Block action if the capability is not admitted or scope is unclear.
- Ask for scoped approval or select no-action.
- Record that action was considered and rejected.

Usefulness does not override capability admission.

### Outcome Unobservable

Action:

```text
Produce a response.
```

Expected outcome:

```text
The user receives useful documentation.
```

Observed outcome:

```text
The response was produced, but user satisfaction is pending.
```

Expected handling:

- Record the produced response as completed.
- Keep satisfaction unresolved.
- Avoid updating belief that the output was successful until feedback arrives.
- Carry uncertainty into the next prediction.

Attempt is not outcome.

## Relationship to Prototype 2 Cognitive Tick

Prototype 2's `12. Cognitive Tick.md` describes a 26-phase tick with more
granular objects and stage names. That material is useful inherited detail for:

- Dependency validation.
- Future schema design.
- Failure statuses.
- Tick records.
- Signal envelopes.
- Precision estimates.
- Memory trace references.
- Negative tests.

It is not current by default. The current Prototype 3 loop should not be
expanded into the 26-phase sequence unless a future Prototype 3 technical spec
adopts those phases.

Prototype 2's `16. First Build Plan.md` is also useful inherited detail for
minimal implementation constraints. It supports the current view that the first
build should prove the loop, avoid broad agency, preserve records, and keep
manual text as signal rather than command authority.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- What exact record schemas should represent each loop stage?
- Should the current loop use a single tick record, separate records per stage,
  or both?
- Which Prototype 2 tick fields should be promoted into current Prototype 3
  schemas?
- What minimum source and boundary checks are required before a manual text
  signal can influence belief?
- How should evidence quality be represented without overcommitting to numeric
  scoring too early?
- What safety-shell policy language should govern allowed first-build actions?
- How should the loop behave when trace writing is unavailable but the system
  still needs to preserve failure evidence?
- What makes an outcome sufficiently observed for action learning?
- How should uncertainty be carried between loops without becoming vague
  caution text?
