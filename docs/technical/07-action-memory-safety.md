# Action, Memory, and Safety

## Purpose

This document defines the current Prototype 3 model for action, memory, and the
safety shell. It explains how the bounded predictive machine moves from
interpreted evidence and belief update into action or no-action, how outcomes
are observed, and how memory preserves the event chain without becoming
uncontrolled storage.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the source of truth for this document. Prototype 2 action,
memory, and safety relationship documents provide inherited supporting detail.
Their taxonomies, object lists, lifecycle states, and schema sketches are not
mandatory current requirements unless Prototype 3 confirms them. Prototype 1
safety/runtime mechanics are historical unless directly retained by Prototype
3.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`
- `Source Documents/3. The Machine Body.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/8. Action as Future Error Management.md`
- `Source Documents/1-17/9. Memory as Reconstruction.md`
- `Source Documents/1-17/15. Relationship to the Safety Canon.md`

## Model Summary

The current Prototype 3 action, memory, and safety model is:

```text
belief state
-> action candidate or no-action
-> expected effect
-> boundary, permission, capability, viability, and safety-shell check
-> selected action or blocked action
-> attempted action, if allowed
-> observed outcome or unresolved outcome
-> action learning from outcome
-> reconstructive memory trace
-> uncertainty carried forward
```

The model prevents shortcuts such as:

- Human request directly becomes action.
- Model output directly authorizes action.
- Tool access becomes permission.
- Action attempt is treated as outcome.
- Memory becomes transcript storage.
- Trace failure is ignored.
- Safety is added after action rather than governing it before execution.

## Action Is Not Obedience

Action is a bounded move with an expected result. It is not obedience to a
command.

A human message may be:

- A request.
- A correction.
- A command candidate.
- A clarification.
- An approval candidate.
- A rejection.
- An ambiguous signal.

It must still pass through signal handling, interpretation, evidence quality,
belief update, action evaluation, and safety-shell review.

The rejected shortcut is:

```text
user says do X
-> system does X
```

The required path is:

```text
human signal
-> interpretation
-> evidence quality
-> belief update or no update
-> action candidate
-> expected effect
-> safety-shell check
-> action or no-action
```

## No-Action Is Valid

No-action is a valid architectural outcome.

The system should choose no-action when:

- The signal is unclear.
- The evidence is weak.
- The action is unsafe.
- Permission is missing.
- Boundary is uncertain.
- Capability is not admitted.
- The outcome cannot be observed.
- Traceability is unavailable.
- The system is degraded, critical, failed, or unknown.

No-action is not passivity. It is a controlled decision not to intervene. The
system should be able to record why no-action was selected.

## Action Requires Expected Effect

Every action must answer:

```text
What is this action expected to change?
```

Examples:

- `write_trace` should produce a valid trace record.
- `ask_clarification` should produce a more precise manual text signal.
- `enter_safe_mode` should reduce available action scope.
- `produce_response` should provide the requested response to the user.
- `no-action` should avoid unsafe or unjustified intervention while preserving
  uncertainty.

If the system cannot define the expected effect, the action is not ready.

An action without expected effect cannot be evaluated. An action that cannot be
evaluated cannot support responsible learning.

## Action State Distinctions

Prototype 3 separates action stages:

- **Action candidate:** a possible action under consideration.
- **Selected action:** the candidate chosen after evaluation.
- **Attempted action:** the selected action was actually tried.
- **Observed outcome:** what actually happened after the attempt or no-action.
- **Unresolved outcome:** the result is not yet known.

These must not be collapsed.

Example:

```text
Action candidate:
write memory trace

Selected action:
write memory trace for this loop

Attempted action:
write operation ran

Observed outcome:
write failed because trace store was unavailable
```

The attempt does not equal success. The system learns from observed outcome, not
from intent.

## Safety-Shell Check Before Execution

The safety shell governs action before execution.

It asks:

- Is the action registered or otherwise known?
- Is the action allowed?
- Is it inside boundary?
- Is the required capability admitted?
- Is permission valid and scoped?
- Is the system viable enough?
- Can the action be traced?
- Can the result be observed?
- Can the system recover if the action fails?
- Should human review be required?

The cognitive core may decide an action is meaningful or useful. The safety
shell decides whether it may be allowed.

If checks fail, the action should be blocked, delayed, replaced with no-action,
clarification, safe mode, stop, or human review.

## Capability Admission

Capability admission is the process by which a possible power becomes allowed
for bounded use.

Prototype 3 distinguishes:

- Technical availability.
- Capability.
- Permission.
- Action.

A host machine may technically support file reads, file writes, network access,
shell commands, API calls, or browser use. That does not make those capabilities
available to the bounded predictive machine.

A capability must be:

- Defined.
- Admitted.
- Scoped.
- Governed by boundary and permission.
- Traceable.
- Monitored.
- Revocable.
- Matched to allowed actions.

More powerful capabilities require stronger safety. Usefulness does not
override capability admission.

## Boundary and Permission Checks

Boundary and permission checks prevent the system from confusing reachability
with authority.

The system must not reason:

```text
I can access it, therefore I may use it.
```

It should ask:

- Is this inside the declared boundary?
- Is this action inside the current task scope?
- Did the user grant scoped permission?
- Does the permission apply to this action now?
- Is the source or target protected?
- Does the action affect `Source Documents/` or other read-only material?
- Is the requested write path allowed?
- Is the operation reversible or recoverable?

Technical access is not permission. Human approval is not unlimited permission.

## Outcome Observation

Outcome observation records what happened after action or no-action.

The system should distinguish:

- Expected outcome.
- Attempt result.
- Observed effect.
- Side effects.
- Partial success.
- Failure.
- Inconclusive or unresolved outcome.

Examples:

```text
Expected outcome:
user receives requested documentation

Observed outcome:
file was created and read back

Unresolved outcome:
user has not yet reviewed quality
```

or:

```text
Expected outcome:
valid trace record exists

Observed outcome:
trace write failed

Unresolved cause:
permission, path, schema, disk, or unknown
```

If the outcome cannot be observed, the system should carry uncertainty forward.

## Action Learning From Outcome

Action learning depends on comparing expected effect with observed outcome.

The system may update:

- Action reliability.
- Trace reliability.
- Sensor reliability.
- Viability.
- Boundary or permission assumptions.
- Operator model.
- Task model.
- Uncertainty.

The update must remain scoped.

Example:

```text
One trace write failed.
```

Valid update:

```text
trace availability is currently unreliable
cause remains unknown
viability may need restriction
```

Invalid update:

```text
all trace writing is permanently broken
the disk is definitely broken
the last action definitely caused the failure
```

Prototype 2 frames action as future error management. That is useful inherited
detail. Prototype 3 currently confirms the simpler requirement: action must have
expected effect, be safety-checked, produce an outcome, and feed learning only
through observed evidence.

## Memory as Reconstruction

Memory is not storage.

Prototype 3 memory preserves the chain of what happened:

- Prior belief.
- Prediction.
- Signal.
- Interpretation.
- Match, mismatch, or inconclusive result.
- Evidence quality.
- Belief update or no update.
- Action considered.
- Action taken or not taken.
- Outcome.
- Remaining uncertainty.

Transcript memory is not enough. A transcript can show what was said while
hiding what the system expected, inferred, rejected, changed, or remained
uncertain about.

Memory should help reconstruct why the system changed, why it acted or did not
act, and what evidence existed at the time.

## Memory Should Preserve Uncertainty

Memory must not make the past cleaner than it was.

Bad memory:

```text
The user wanted X.
```

Better memory:

```text
The signal was interpreted as a request for X.
Confidence was high because it matched the active sequence.
Uncertainty remained about exact desired length.
```

Memory should preserve:

- Alternative interpretations where relevant.
- Confidence limits.
- Evidence quality.
- Unknown cause.
- Pending user evaluation.
- Trace gaps.
- Privacy or source limitations.
- Later revisions.

If the system was uncertain at the time, memory should preserve that
uncertainty.

## Traceability and Audit

Traceability is the evidence substrate for action, memory, recovery, and audit.

Trace may record:

- Signal arrival.
- Prediction.
- Interpretation.
- Belief update.
- Action candidate.
- Action denial.
- Action execution.
- Action failure.
- Outcome.
- Memory trace.
- Safe mode.
- Recovery attempt.

Trace is not the same as memory. Trace records what happened in the system.
Memory reconstructs the event chain from trace and other evidence.

If the system cannot answer from records why it acted, why it blocked action,
what outcome occurred, or what uncertainty remained, the action/memory/safety
model is not yet adequate.

## Safety Shell Responsibilities

The safety shell is the outer governance layer around the cognitive core.

It is responsible for:

- Boundary enforcement.
- Traceability.
- Viability classification.
- Capability admission.
- Controlled action.
- Scoped human input and approval.
- Recovery discipline.
- Memory and belief safeguards.
- Uncertainty-based caution.

For action, it checks:

- Is the action allowed?
- Is the capability admitted?
- Is the system viable?
- Is the boundary respected?
- Can the action be traced?
- Can the result be observed?

For memory, it checks:

- Is the source trace valid?
- Is privacy respected?
- Is uncertainty preserved?
- Is the memory source-backed?
- Is retention or redaction required?

For belief, it checks:

- Is the evidence admissible?
- Is the signal allowed?
- Is the belief target protected?
- Is the update too broad?

Safety does not replace cognition. It governs the conditions under which
cognition may update, act, remember, and recover.

## First-Build Action Set

Prototype 3 first-build actions should remain small and inspectable.

Examples include:

- Do nothing.
- Write a trace.
- Write a status record.
- Write a memory trace.
- Ask for clarification.
- Enter safe mode.
- Stop safely.
- Produce a response.

The first build should not begin with:

- Broad tool use.
- Web browsing.
- External file editing.
- Shell execution.
- Autonomous task execution.
- Long-term user memory.
- Self-modification.
- Natural language command execution.

The first build should prove the loop, not broad agency.

## Examples

### Allowed Action

Scenario:

```text
User request:
Create docs/technical/07-action-memory-safety.md.
```

Action candidate:

```text
create the requested documentation file
```

Expected effect:

```text
docs/technical/07-action-memory-safety.md exists and contains the requested
technical documentation
```

Safety-shell result:

- Target path is inside repository boundary.
- The action does not modify `Source Documents/`.
- No dependency installation, deletion, network access, or commit is required.
- The action can be verified by reading the file back.

Selected action:

```text
create the file
```

Observed outcome:

```text
file created; user review pending
```

### Blocked Action

Scenario:

```text
User request:
Read all files in my home directory and use them for memory.
```

Action candidate:

```text
read broad home-directory contents
```

Safety-shell result:

- Target is outside the current project documentation boundary.
- Broad file-reading capability is not admitted.
- Privacy scope is unclear.
- Memory purpose is overbroad.
- The action is not needed for the current doc task.

Selected result:

```text
blocked action / no-action for the broad read
```

Possible response:

```text
ask for a scoped, inside-boundary source if more material is needed
```

### No-Action

Scenario:

```text
Signal:
Do it.
```

Context:

```text
multiple possible actions are pending
```

Interpretation:

```text
ambiguous command candidate
```

Evidence quality:

```text
low for exact action target
```

Selected result:

```text
no-action or ask clarification
```

Memory:

```text
record ambiguity, rejected action, and remaining uncertainty
```

### Failed Outcome

Scenario:

```text
Selected action:
write trace

Expected effect:
valid trace record exists

Attempt:
write operation ran

Observed outcome:
write failed
```

Valid learning:

```text
trace store currently unreliable
viability may be degraded or critical
cause remains unknown
```

Invalid learning:

```text
disk is definitely broken
all future trace writes will fail
the action that preceded the trace write caused the failure
```

Safety response:

```text
restrict nonessential cognition, enter safe mode, stop, or request review
depending on current policy
```

### Reconstructive Memory

Scenario:

```text
User requests a documentation file.
The system creates it.
User review has not occurred yet.
```

Weak memory:

```text
The user asked for 07-action-memory-safety.
```

Reconstructive memory:

```text
Prior belief:
the user is requesting sequential technical documentation files

Prediction:
the next signal may request the next docs/technical file

Signal:
Create docs/technical/07-action-memory-safety.md

Interpretation:
user requests the action/memory/safety technical document

Evidence quality:
high for current task and target file

Action considered:
create documentation file

Safety check:
inside docs/technical, Source Documents remains read-only, no commit requested

Selected action:
create file

Outcome:
file created; user evaluation pending

Uncertainty:
final schema and implementation details remain unresolved
```

This memory preserves the cognitive chain, not just the event label.

## Failure Cases

### Command-Like Text Bypasses Interpretation

Failure:

```text
raw text says "continue"
-> system continues automatically
```

Correct handling:

- Treat text as signal.
- Interpret possible meanings.
- Check evidence quality.
- Consider action only if target and scope are clear.
- Ask clarification or choose no-action when ambiguous.

### Action Has No Expected Effect

Failure:

```text
action selected because it seems useful
```

Correct handling:

- Block action until expected effect is defined.
- Define success and failure conditions where possible.
- Prefer no-action if outcome cannot be evaluated.

### Capability Creep

Failure:

```text
system uses a tool because the tool is available
```

Correct handling:

- Treat tool use as a capability requiring admission.
- Check scope, permission, boundary, traceability, and recovery.
- Block use if not admitted.

### Trace Failure Ignored

Failure:

```text
trace write fails
-> system continues normal belief update and action
```

Correct handling:

- Treat trace failure as safety-relevant evidence.
- Update viability or uncertainty.
- Restrict nonessential cognition.
- Preserve failure evidence if possible.

### Memory Becomes False Certainty

Failure:

```text
memory stores "the user wanted X" despite ambiguity
```

Correct handling:

- Store interpretation, confidence, alternatives, and uncertainty.
- Preserve the original signal reference where allowed.
- Allow later revision without erasing the original trace.

## Relationship to Prototype 2

Prototype 2 is useful inherited support for future implementation design:

- `8. Action as Future Error Management.md` adds action candidates, action
  policy, expected information gain, action costs, action risks, action
  lifecycle, and action-outcome learning.
- `9. Memory as Reconstruction.md` adds memory traces, memory fragments,
  reconstruction, revision, conflict, compression, privacy, confidence, and
  precision.
- `15. Relationship to the Safety Canon.md` clarifies the relationship between
  cognitive core and safety shell.

These details are valuable, but they should not be flattened into the current
Prototype 3 canon as mandatory machinery. Prototype 3 currently requires the
core discipline: action is bounded and expected-effect-bearing; no-action is
valid; safety checks precede execution; outcome is observed; memory reconstructs
the chain; uncertainty remains visible.

Prototype 1 safety/runtime mechanics are historical implementation lineage.
They may inspire future runtime engineering, but they are not mandatory current
mechanics unless Prototype 3 adopts them.

## Implementation Risks

- Treating action as obedience.
- Treating text generation as the only kind of action.
- Treating no-action as failure.
- Selecting action without expected effect.
- Attempting action before safety-shell checks.
- Treating technical access as permission.
- Allowing capability use without admission.
- Treating attempted action as successful outcome.
- Retrying failed action automatically.
- Storing transcript as memory.
- Hiding uncertainty in memory.
- Treating trace as optional logging.
- Promoting Prototype 2 action or memory schemas to current requirements too
  early.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- What is the minimal current action registry for the first build?
- What fields are required for an action candidate in Prototype 3?
- How should selected action, attempted action, and observed outcome be recorded?
- What is the minimum safety-shell check before a first-build action executes?
- What is the first-build capability admission process?
- How should human approval be represented so it remains scoped?
- What outcomes are observable for response-generation actions?
- How should failed trace writing be handled if the failure cannot itself be
  traced normally?
- What is the minimal reconstructive memory trace format?
- Which uncertainty fields must be preserved in memory?
- What privacy and retention rules apply to memory traces?
- Which Prototype 2 action and memory objects should be promoted first, if any?
