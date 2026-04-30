# Core Concepts

## Purpose

This file defines the core terms used by the current Prototype 3 architecture.
It is a technical glossary, not a product overview. Each term is defined in the
context of a bounded predictive machine whose behavior is organized around
body, boundary, prediction, signal, interpretation, belief update, action,
memory, uncertainty, and safety.

## Source Precedence

The documentation follows this source hierarchy:

1. Prototype 3 root `Source Documents/` files are the current source of truth.
2. Prototype 2 files under `Source Documents/1-17/` may provide supporting prior
   design detail where they clarify a Prototype 3 concept.
3. Prototype 1 files under `Source Documents/V0 - V9/` are historical or
   original implementation lineage unless Prototype 3 explicitly retains the
   idea.

When older prototype material is not confirmed by Prototype 3, it should be
treated as historical, inherited, optional, or unresolved rather than current.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/3. The Machine Body.md`
- `Source Documents/4. Prediction, Signal, and Surprise.md`
- `Source Documents/5. Belief, Action, and Memory.md`
- `Source Documents/6. Safety as the Outer Shell.md`

Supporting Prototype 2 sources may be used only where they clarify a Prototype 3
term. Prototype 1 sources are historical unless explicitly noted.

## Status Labels

- **Current:** Confirmed by Prototype 3 and part of the present architecture.
- **Inherited:** Compatible with Prototype 3 and useful as prior design detail,
  but not independently mandatory unless Prototype 3 confirms it.
- **Optional:** A possible implementation choice, not a required architectural
  rule.
- **Historical:** Part of Prototype 1 lineage or older design framing.
- **Unresolved:** Not specified clearly enough by Prototype 3 to define as
  current behavior.

## Bounded Predictive Machine

**Plain definition:** A system that operates within known limits and uses
expectations to understand incoming evidence before deciding whether to update
belief or act.

**Technical meaning:** In Prototype 3, this is the central architectural
identity. The machine is bounded because it must know what it is, what it can
sense, what it can access, what it can change, what it must not touch, and what
state it is in. It is predictive because it forms expectations before receiving
or evaluating signals, then uses mismatch, evidence quality, and uncertainty to
decide whether belief or action should change.

**What it is not:** It is not a chatbot with memory, a conventional task agent,
an unconstrained tool user, or a planner that begins from goals and commands.
It is also not a safety wrapper around an otherwise ordinary agent.

**Status:** Current Prototype 3 concept. Prototype 2 and Prototype 1 may contain
implementation lineage, but the current definition is Prototype 3-first.

## Machine Body

**Plain definition:** The concrete operating shape of the machine.

**Technical meaning:** The machine body includes the running program, files,
configuration, memory, permissions, sensors, possible actions, logs, traces,
safety boundaries, and health or viability state. It defines what the system is
made of operationally before any prediction, signal interpretation, or action
can be trusted.

**What it is not:** It is not a metaphor for personality, embodiment, or a
human-like self. It is also not only the model, process, or runtime environment
in isolation.

**Status:** Current Prototype 3 concept. Older prototype material may provide
implementation inspiration for body records or trace formats, but those details
are inherited or historical unless retained by Prototype 3.

## Boundary

**Plain definition:** The line between what the machine may treat as inside its
allowed operating space and what remains outside it.

**Technical meaning:** A boundary specifies what belongs to the machine body,
what may be read, what may be written, what may be changed, what is external,
and what must not be touched. Prototype 3 treats technical access and permission
as separate: the fact that something can be reached does not mean it is inside
the allowed boundary.

**What it is not:** It is not a simple file-system path check, a list of tools,
or a static access-control flag. It is also not permission to act merely because
the user requests action.

**Status:** Current Prototype 3 concept. The exact implementation form of
boundary records, policies, or enforcement hooks remains unresolved unless
specified by a later technical design.

## Signal

**Plain definition:** Anything the machine receives from the world, the user, or
its own runtime.

**Technical meaning:** A signal is input evidence, not truth. Prototype 3
examples include manual text input, clock or timing data, runtime status, trace
store status, configuration status, schema validation results, and viability
status. Signals must be interpreted before they can affect belief or action.

**What it is not:** A signal is not automatically a fact, instruction,
permission, goal, or reliable account of the world. Human language is still a
signal, not a direct command channel.

**Status:** Current Prototype 3 concept. Prototype 2 may offer supporting
detail about signal handling, but Prototype 3 defines the current role.

## Sensor

**Plain definition:** A source or mechanism through which the machine receives
signals.

**Technical meaning:** A sensor can be human-facing, runtime-facing, or
system-facing. Prototype 3 starts with modest sensors such as manual text input,
runtime status, trace status, configuration status, schema validation results,
and viability status. Each sensor has limits; for example, text input can expose
words, timing, and source, but not automatically intention, truth, permission,
or safe belief updates.

**What it is not:** A sensor is not a guarantee that the received signal is
accurate, complete, safe, or action-authorizing. It is also not necessarily a
physical device.

**Status:** Current Prototype 3 concept. Specific sensor schemas and expansion
rules are unresolved beyond the first-build examples.

## Prediction

**Plain definition:** An expectation formed before evaluating new evidence.

**Technical meaning:** Prediction gives the machine a prior expectation against
which signals can be compared. It may concern expected user intent, expected
runtime state, expected file state, expected trace continuity, expected action
outcome, or expected safety status. Prediction is required for meaningful
surprise because mismatch can only be detected against a prior expectation.

**What it is not:** Prediction is not fortune telling, certainty, permission to
act, or a commitment to ignore evidence that does not match the expectation.

**Status:** Current Prototype 3 concept. Prototype 2 tick designs may describe
more granular prediction phases, but those phase counts are inherited detail,
not mandatory current architecture.

## Surprise / Mismatch

**Plain definition:** The difference between what the machine expected and what
the signal appears to show.

**Technical meaning:** Surprise is the architecture's mismatch detector. A
signal may match expectation, partially match, contradict it, arrive early or
late, be unclear, or be unreliable. Surprise triggers interpretation, evidence
quality review, scoped belief update, possible action consideration, and safety
review; it does not directly force belief change or action.

**What it is not:** Surprise is not proof that the machine was wrong, proof that
the signal is true, or automatic permission to act. It is also not an emotional
state.

**Status:** Current Prototype 3 concept. More elaborate mismatch taxonomies from
older prototypes should be treated as inherited or optional unless Prototype 3
adopts them explicitly.

## Interpretation

**Plain definition:** The machine's attempt to assign meaning to a signal before
using it.

**Technical meaning:** Interpretation sits between signal receipt and belief
update. It may include possible meanings, confidence, ambiguity, source
assessment, relation to prediction, and whether the signal is relevant to the
current belief or viability state. Prototype 3 requires interpretation because
signals are not self-explaining.

**What it is not:** Interpretation is not the same as accepting a signal as
true. It is not a final belief update, a safety decision, or an action decision.

**Status:** Current Prototype 3 concept. The required internal representation
for interpretations remains unresolved.

## Precision / Evidence Quality

**Plain definition:** A judgment about how much a signal should count for the
specific question being considered.

**Technical meaning:** Precision, or evidence quality, determines whether a
signal is strong, weak, ambiguous, stale, indirect, incomplete, unreliable, or
otherwise limited. Prototype 3 uses evidence quality to prevent over-updating
belief from weak signals and to decide whether uncertainty should remain high.

**What it is not:** Precision is not general confidence in the model, confidence
in the user, or a universal trust score. It is question-specific and context
specific.

**Status:** Current Prototype 3 concept. Numeric scoring schemes, thresholds,
or precision taxonomies are unresolved unless defined by future implementation
documents.

## Belief

**Plain definition:** The machine's structured view of the current situation.

**Technical meaning:** A belief may represent the current task, current state,
recent signals, likely user request, sensor reliability, allowed actions,
uncertainty, recent changes, and relevant boundary or viability information.
Belief is practical and operational: it helps the machine decide what is true
enough, uncertain enough, or unsafe enough for the next step.

**What it is not:** Belief is not opinion, personality, memory, model output, or
an unqualified assertion of truth. It is also not automatically changed by every
signal.

**Status:** Current Prototype 3 concept. The exact data model for belief state
is unresolved.

## Belief Update

**Plain definition:** A scoped change to belief after comparing prediction,
signal, interpretation, and evidence quality.

**Technical meaning:** A belief update asks what the prior belief was, what was
predicted, what signal arrived, how it was interpreted, how strong the evidence
is, which belief should change, how much it should change, and what uncertainty
remains. Prototype 3 emphasizes narrow updates rather than broad rewriting.

**What it is not:** A belief update is not automatic acceptance of input,
replacement of memory, unrestricted learning, or global self-modification.

**Status:** Current Prototype 3 concept. Prototype 2 may contain inherited
detail about update phases, but Prototype 3 does not make a 26-phase tick or
similar prior structure mandatory.

## Action

**Plain definition:** A bounded move the machine may take with an expected
effect.

**Technical meaning:** An action must be registered, allowed, scoped,
traceable, and connected to an expected outcome. Prototype 3 examples include
doing nothing, writing a trace or status, asking for clarification, entering
safe mode, stopping safely, or producing a response. Before action, the machine
must consider clarity, boundary, permission, expected effect, observability,
risk, whether no-action is safer, and safety-shell approval.

**What it is not:** Action is not obedience, tool use by default, execution of
natural language commands, or proof that the machine understood correctly.

**Status:** Current Prototype 3 concept. Expanded action catalogs from older
prototypes are inherited or historical unless Prototype 3 confirms them.

## No-Action

**Plain definition:** An intentional decision not to act.

**Technical meaning:** No-action is a valid architectural outcome when the
signal is unclear, action is unsafe, permission is missing, boundary is
uncertain, evidence is weak, the outcome cannot be observed, or viability is
degraded. It preserves the distinction between noticing something and changing
the world.

**What it is not:** No-action is not failure, passivity, or absence of
processing. It can be the correct result of prediction, interpretation,
uncertainty review, and safety checking.

**Status:** Current Prototype 3 concept.

## Outcome

**Plain definition:** What actually happened after an action or no-action
decision.

**Technical meaning:** Prototype 3 separates selected action, attempted action,
expected outcome, and observed outcome. Outcome evidence feeds memory,
uncertainty, future prediction, and possible belief updates. A failed attempt,
partial result, unobservable result, or unexpected side effect should be
recorded differently from the intended effect.

**What it is not:** Outcome is not the same as intent, action selection, or
successful execution. It is not assumed merely because the machine tried.

**Status:** Current Prototype 3 concept. Detailed outcome schemas are
unresolved.

## Memory

**Plain definition:** A record that helps the machine reconstruct what happened
and why.

**Technical meaning:** Prototype 3 treats memory as reconstructive, not as raw
storage. A useful memory trace may preserve prior belief, prediction, signal,
interpretation, match or mismatch, evidence quality, belief change, action
considered, action taken or not taken, outcome, and remaining uncertainty.
Memory supports future prediction and review without pretending every stored
item is a fact.

**What it is not:** Memory is not a pile of conversation history, permanent
truth, user profiling by default, or automatic long-term learning.

**Status:** Current Prototype 3 concept. Prototype 1 memory mechanisms are
historical unless Prototype 3 re-adopts them. Specific storage technology,
retention rules, and summarization behavior remain unresolved.

## Uncertainty

**Plain definition:** What the machine does not know, cannot safely infer, or
cannot yet verify.

**Technical meaning:** Uncertainty should remain visible across prediction,
interpretation, evidence quality, belief update, action, outcome, memory, and
viability. It can block action, require clarification, lower update strength,
or cause the system to preserve multiple interpretations. Prototype 3 treats
unknown as materially different from safe.

**What it is not:** Uncertainty is not an error to hide, a lack of usefulness,
or a reason to invent missing details. It is also not solved merely by model
confidence.

**Status:** Current Prototype 3 concept. How uncertainty is represented,
aggregated, or thresholded remains unresolved.

## Safety Shell

**Plain definition:** The outer governance layer that decides whether proposed
belief updates, actions, memory writes, recovery steps, and capability use are
allowed.

**Technical meaning:** The safety shell contains and governs the cognitive core.
It checks boundary, allowed action, traceability, viability, capability
admission, recovery path, memory and belief safety, human input safety, and
uncertainty. Prototype 3 draws a clear split: the cognitive core decides what
may be meaningful, while the safety shell decides what may be allowed.

**What it is not:** It is not the whole architecture, an after-the-fact policy
filter, or a generic refusal layer. It is also not evidence that the cognitive
core may ignore safety internally.

**Status:** Current Prototype 3 concept. Prototype 2 safety-canon material may
be inherited where it clarifies shell responsibilities, but it should not
override Prototype 3.

## Viability

**Plain definition:** The machine's operational health and ability to continue
safely.

**Technical meaning:** Viability indicates whether the system is safe,
degraded, critical, failed, or unknown. It is part of the machine body's state
and affects whether the machine may continue, act, ask for clarification, enter
safe mode, or stop. Prototype 3 explicitly treats unknown as not safe.

**What it is not:** Viability is not general performance quality, user
satisfaction, uptime alone, or proof that a specific action is permitted.

**Status:** Current Prototype 3 concept. Specific viability thresholds,
monitoring metrics, and transition rules remain unresolved.

## Capability Admission

**Plain definition:** The process by which a possible capability becomes
allowed for bounded use.

**Technical meaning:** Prototype 3 distinguishes capability from permission and
from action. A capability must be admitted, scoped, monitored, traceable, and
revocable before it can safely support actions. More powerful capabilities
require stronger safety constraints, clearer boundaries, better traceability,
and more careful recovery behavior.

**What it is not:** Capability admission is not the same as installing a tool,
having API access, receiving user approval, or deciding that a capability is
useful. Technical availability does not equal architectural permission.

**Status:** Current Prototype 3 concept. Detailed admission criteria and
implementation workflow are unresolved. Older capability and tool-use designs
should be treated as inherited or historical unless Prototype 3 confirms them.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- What concrete schemas will represent prediction, signal, interpretation,
  belief state, belief update, action candidate, outcome, memory trace, and
  uncertainty?
- What thresholds or qualitative rules determine evidence quality, viability
  state, and acceptable action risk?
- How should the safety shell enforce capability admission in the first build?
- Which Prototype 2 tick details, if any, should be retained as inherited
  implementation guidance rather than historical design context?
- What retention, review, and deletion rules should apply to reconstructive
  memory?
