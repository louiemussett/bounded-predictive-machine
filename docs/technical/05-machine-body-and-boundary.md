# Machine Body and Boundary

## Purpose

This document defines the current Prototype 3 machine body and boundary model
for the bounded predictive machine.

The machine body is the system's bounded operational form: what it is, where it
runs, what it can sense, what it can change, what it may access, what can fail,
and what keeps it inside safe limits. The boundary is the part of that body
model that distinguishes inside from outside and technical access from
permission.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the source of truth for this document. Prototype 2 machine-body
and safety-shell material may clarify concepts, but its body-record schemas are
not current requirements unless Prototype 3 confirms them. Prototype 1 bounded
runtime details are historical implementation lineage and should not be treated
as mandatory current implementation.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/3. The Machine Body.md`
- `Source Documents/6. Safety as the Outer Shell.md`
- `Source Documents/7. The First Build.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/1. Machine Body.md`
- `Source Documents/1-17/15. Relationship to the Safety Canon.md`

Historical Prototype 1 source:

- `Source Documents/V0 - V9/1. Foundation.md`

## Current Definition

In Prototype 3, the machine body is the bounded runtime structure that grounds
all later cognition. It includes:

- Runtime identity.
- Project boundary.
- Files and state inside the boundary.
- Configuration.
- Sensors.
- Possible actions.
- Permissions.
- Trace and log layer.
- Viability or health state.
- Safety limits.

The body is not a human-like body. It does not imply feeling, consciousness,
instinct, personhood, or desire. It is an engineering model of the system's
operational limits and failure modes.

The machine body comes before prediction, learning, action, memory, tools,
goals, or autonomy. A system that does not know its boundary, trace status,
configuration status, action set, and viability should not act as though it is
safe to continue normally.

## Runtime Identity

Runtime identity answers:

```text
What system is running?
Where is it running?
What mode is it in?
Which configuration did it load?
Which boundary does it claim?
Which actions and sensors are enabled?
What is its current viability?
```

Prototype 3 does not yet define a final runtime identity schema. A first-build
runtime identity should be simple enough to inspect by hand and should not
depend on hidden model state.

At minimum, runtime identity should identify:

- The current runtime instance or process.
- The declared project root or operating boundary.
- The active configuration source.
- The runtime mode.
- The current viability state.
- The trace/log availability state.
- The allowed action registry or equivalent action list.

Prototype 2 contains richer body-state and tick-state sketches. Those are
inherited design guidance, not current mandatory schemas.

## Project Boundary

The project boundary defines what belongs to the runtime and what remains
outside it.

It answers:

- What belongs to this runtime?
- What is outside this runtime?
- What may the system read?
- What may the system write?
- What may the system change?
- What must the system never touch?
- Which sensors and actions are inside the allowed operating space?

Boundary is both a safety concern and a cognitive concern. Without a boundary,
the system cannot reliably distinguish self-state from environment state,
internal action from external disturbance, or available access from permitted
use.

Prototype 3 confirms the rule:

```text
Technical access is not permission.
```

The system must not reason:

```text
I can access this, therefore it is mine.
```

It must instead ask:

```text
Is this inside my boundary?
Is this capability admitted?
Is this action allowed?
Is this safe to do?
Can this be traced?
```

## Files and State Inside the Boundary

Files and state inside the boundary are the parts of the project the runtime may
use under current configuration and safety rules.

Prototype 3 first-build examples include:

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
They show the kind of body records a first build needs: boundary, bootstrap
state, action registry, runtime status, body state, viability, traces, and
schema validation.

State is evidence. It is not belief by itself. The cognitive loop still needs
to interpret state signals, compare them with predictions, judge evidence
quality, and update belief only where justified.

## Configuration

Configuration defines the declared operating constraints of the machine body.
It may specify:

- Project root or boundary.
- Required directories.
- Trace locations.
- State locations.
- Enabled sensors.
- Allowed actions.
- Forbidden actions.
- Runtime mode defaults.
- Viability rules.
- Schema locations.
- Capability settings.

Configuration is protected body evidence. The system should not guess missing
protected configuration, silently repair it, or expand permissions to fix a
configuration problem.

If required configuration is missing, invalid, or outside the expected boundary,
the correct response may be degraded operation, safe mode, stopped state,
recovery, or human review.

## Sensors

A sensor is any source through which the system receives signals.

Prototype 3 first-build sensors may include:

- Manual text input.
- Clock.
- Runtime status.
- Trace-store status.
- Configuration status.
- Schema validation result.
- Viability status.

Each sensor has limits. For example, manual text input can tell the system what
words arrived, when they arrived, and where the message came from. It cannot by
itself prove the user's true intention, truth of the content, permission to act,
or whether belief should update.

The machine body defines which sensors exist and what each sensor can report.
The cognitive loop decides what the signal means.

Prototype 2 sensor-model fields such as freshness, precision, privacy, and
belief targets are useful inherited design detail. They remain unresolved as
current schema requirements.

## Possible Actions

The machine body includes possible actions. In Prototype 3, first-build actions
should be limited and traceable.

Examples include:

- Do nothing.
- Write a trace.
- Write a status record.
- Write a memory trace.
- Ask for clarification.
- Enter safe mode.
- Stop safely.
- Produce a response.

An action must be:

- Registered or otherwise known.
- Allowed in the current context.
- Inside boundary.
- Connected to an expected effect.
- Traceable.
- Governed by the safety shell.

The existence of a possible action does not mean the system may perform it. A
language output, a trace write, and a safe stop are all actions, but each still
requires context, permission, expected effect, and safety review.

## Permissions

Permissions define what the runtime may access or change in a specific context.

Permission is not the same as capability:

- A capability is something the system can potentially use or do.
- Permission is the scoped allowance to use that capability now.

For example, a host machine may technically allow file reads, shell execution,
network requests, or API calls. Prototype 3 does not treat those as available by
default. Each capability must be admitted, scoped, monitored, traceable, and
revocable before it can support action.

Human approval is also not unlimited permission. A user message may authorize a
specific action, but it should not automatically authorize unrelated future
actions, broader filesystem access, new capabilities, or unsafe recovery.

## Trace and Log Layer

The trace/log layer preserves evidence of what happened.

Trace may record:

- Runtime start.
- Body state.
- Viability classification.
- Signal arrival.
- Prediction.
- Interpretation.
- Belief update.
- Action candidate.
- Action denial.
- Action execution.
- Outcome.
- Memory trace.
- Failure.
- Safe mode or stop.

Trace is not decoration. It is evidence for audit, memory reconstruction,
recovery, belief update, action learning, and debugging.

If trace writing fails, the system should not continue higher-level cognition as
though nothing changed. Trace failure can make the system degraded or critical
because it weakens the evidence chain.

Prototype 1 includes a historical bounded state-and-trace runtime with commands
and trace files. That lineage is useful implementation inspiration, but its
specific commands and file layout are not current requirements.

## Viability / Health State

Viability is the machine body's operational health classification.

Prototype 3 names these viability states:

- `safe`
- `degraded`
- `critical`
- `failed`
- `unknown`

Plain meaning:

- `safe`: the system can operate normally.
- `degraded`: something is wrong, but limited operation may continue.
- `critical`: normal operation should stop or shrink.
- `failed`: the system cannot safely continue.
- `unknown`: there is not enough evidence to say the system is safe.

The key rule is:

```text
Unknown is not safe.
```

Viability may depend on boundary validity, trace availability, configuration
validity, schema status, permission status, sensor reliability, runtime errors,
and action outcomes.

Prototype 3 does not yet define exact transition rules between viability states.
Those rules remain unresolved.

## Safety Limits

The safety shell surrounds the cognitive loop and governs the machine body.

Safety limits include:

- Boundary enforcement.
- Traceability.
- Viability checks.
- Capability admission.
- Controlled action.
- Scoped human input and approval.
- Recovery discipline.
- Memory and belief safeguards.
- Uncertainty-based caution.

The cognitive core may decide what a signal means or what action might be
useful. The safety shell decides whether use, update, memory, action, recovery,
or capability access is allowed.

Safety limits prevent shortcuts such as:

- Input directly becomes action.
- Input directly becomes belief.
- Tool access becomes permission.
- Human approval becomes unlimited permission.
- Memory becomes fact.
- Recovery rewrites history.
- Uncertainty is ignored.

## What Is Outside the Boundary

Outside the boundary is anything the current runtime may not treat as belonging
to its body or allowed operating space.

Examples may include:

- Files outside the declared project root.
- User private files not explicitly admitted.
- External network resources.
- Shell commands not admitted as actions.
- Browser, email, calendar, or API access not admitted as capabilities.
- Host system areas not declared part of the project.
- Protected configuration outside the allowed edit path.
- Source material explicitly marked read-only for a documentation task.

Outside-boundary resources may still be technically reachable. That does not
make them part of the body.

The system may receive signals about outside resources, but it must not read,
write, modify, learn from, or act on them as if they were inside boundary unless
a capability has been admitted and the action has passed safety checks.

## Technical Access Versus Permission

The boundary model depends on a strict distinction:

```text
technical access != permission
```

Technical access means the host environment, tool, process, or user channel may
make something reachable.

Permission means the current architecture has admitted and scoped use of that
resource or action.

Examples:

- The process may be able to see files outside the project, but those files are
  outside boundary unless explicitly admitted.
- The runtime may be able to write files, but a user may constrain it to create
  only a specific documentation file.
- A shell may exist, but shell execution is not allowed unless admitted as a
  capability and selected as an allowed action.
- Human text may request a broad operation, but the text is signal first and
  permission only if interpreted, scoped, and safety-checked.

This distinction should be enforced before action, before belief update, and
before memory writes.

## Allowed Inside-Boundary Action Example

Scenario:

```text
User request:
Create docs/technical/05-machine-body-and-boundary.md.
```

Boundary interpretation:

- Target path is inside the repository.
- Target path is under `docs/technical/`.
- The action does not modify `Source Documents/`.
- The action does not require deletion, dependency installation, network access,
  or commit.
- The requested output is consistent with the current documentation task.

Allowed action:

```text
Create the requested documentation file under docs/technical/.
```

Expected effect:

```text
The new technical documentation file exists and can be read back for review.
```

Residual uncertainty:

```text
Final implementation schemas remain unresolved.
```

## Blocked Outside-Boundary Action Example

Scenario:

```text
User request:
Read everything in my home directory and use it to improve the body model.
```

Boundary interpretation:

- The home directory is outside the declared project documentation scope.
- Broad file reading is not admitted as a current capability.
- Privacy and permission scope are unclear.
- The requested action is broader than the current task.
- The action is not necessary to define the Prototype 3 machine body model.

Blocked action:

```text
Do not read the home directory.
```

Safer result:

```text
Choose no-action for the broad read and ask for a scoped, inside-boundary source
if additional source material is needed.
```

This is not a failure to use available access. It is correct boundary behavior.

## First-Build Minimal Body

Prototype 3 says the first build should begin with a small, inspectable body.

The first-build minimal body should know:

- Where its project boundary is.
- Where its configuration is.
- Where traces are written.
- Whether required schemas exist.
- Whether trace writing works.
- Whether boundary is valid.
- Whether current viability is safe, degraded, critical, failed, or unknown.
- Which actions are allowed.
- Which actions are forbidden.

A minimal current body may include:

- Declared project root.
- Bootstrap configuration.
- Boundary configuration.
- Action registry or allowed-action list.
- Runtime status.
- Current body state.
- Current viability state.
- Trace writer.
- Startup trace.
- Event trace.
- Basic schema validation.
- Manual text input.
- Runtime, trace, configuration, schema, and viability signals.

This is enough to run the current loop in a bounded, traceable way. It is not a
chatbot, agent, planner, tool user, or broad automation system.

Prototype 2 proposes richer modules and object names. Prototype 1 provides a
bounded state-and-trace runtime lineage. Both are useful for future technical
design, but Prototype 3 currently requires the concept and minimum body
discipline rather than those exact implementations.

## Relationship to Older Prototype Material

Prototype 2's `1. Machine Body.md` is useful inherited detail for:

- Layer vocabulary.
- Body state questions.
- Body signals.
- Body action examples.
- Viability as operational classification.
- Trace as body continuity.

It is not current by default where it specifies detailed body schemas, object
lists, CPU/memory/disk sensing, or low-level body-learning behavior that
Prototype 3 has not confirmed.

Prototype 2's `15. Relationship to the Safety Canon.md` is useful inherited
detail for the distinction between cognitive core and safety shell. Its older
"two canons" framing should not override the corrected current hierarchy of
three design generations.

Prototype 1's `V0 - V9/1. Foundation.md` is historical implementation lineage.
It demonstrates a bounded state-and-trace substrate with runtime state,
operation traces, resource traces, and fail-closed behavior. Those ideas may
inspire implementation, but its commands, file names, and version path are not
mandatory current architecture.

## Implementation Risks

- Treating host filesystem access as boundary permission.
- Treating user text as direct authority rather than signal.
- Treating Prototype 2 body schemas as current implementation requirements.
- Treating Prototype 1 bounded-root commands as the current runtime path.
- Building tool use before boundary, trace, viability, and action registry are
  stable.
- Continuing normal cognition after trace failure.
- Updating belief from state files without interpretation and evidence-quality
  review.
- Storing transcript-like memory instead of reconstructive memory.
- Expanding capability to solve recovery failures.

## Open Questions

- What exact schema should represent current body state?
- What is the minimal boundary configuration required for the first build?
- Which files and directories are inside the first-build boundary by default?
- How should read permission and write permission be represented separately?
- What sensor registry is required before manual text, runtime status, trace
  status, configuration status, schema status, and viability status can be used?
- What is the minimal action registry for no-action, trace writing, status
  writing, memory trace writing, clarification, safe mode, safe stop, and
  response generation?
- What are the exact viability transition rules?
- What happens if trace writing fails before the failure itself can be traced?
- Which Prototype 2 body-record fields should be promoted into current schemas?
- Which Prototype 1 state-and-trace implementation ideas should be retained as
  implementation inspiration rather than historical context?
