# Prototype Lineage

## Purpose

This document explains how the three source generations relate to each other
and how future technical documentation should use them.

The goal is to preserve Prototype 3 as the current source of truth while still
using Prototype 2 and Prototype 1 correctly: Prototype 2 as supporting prior
cognitive detail, and Prototype 1 as historical implementation lineage.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

The rule is:

```text
Prototype 3 current design
> Prototype 2 supporting design detail
> Prototype 1 original implementation lineage
```

Older material should not be flattened into the current canon. If a Prototype 2
or Prototype 1 detail is not confirmed by Prototype 3, label it as inherited,
historical, optional, or unresolved rather than current.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`
- `Source Documents/7. The First Build.md`

Supporting Prototype 2 sources:

- `Source Documents/1-17/0A. Core Cognitive Thesis.md`
- `Source Documents/1-17/12. Cognitive Tick.md`
- `Source Documents/1-17/13. Cognitive Data Model.md`
- `Source Documents/1-17/14. Developmental Ladder.md`
- `Source Documents/1-17/17. Evaluation for Original Alignment.md`

Historical Prototype 1 sources:

- `Source Documents/V0 - V9/0. White Paper.md`
- `Source Documents/V0 - V9/0A. Overview.md`
- `Source Documents/V0 - V9/1. Foundation.md`

## Generation Summary

### Prototype 1: Original Design Lineage

Prototype 1 is the original V0-V9 design lineage. It describes a bounded,
trace-driven runtime that grows through versioned implementation layers:

- Bounded runtime root.
- State and trace persistence.
- Adaptive regularity extraction.
- Expectations and predictions.
- Mismatch checking.
- Controlled action.
- Viability-aware behavior.
- Interface governance.
- Constrained tasks.
- Structured human command channel.
- Health, recovery, compaction, and summary operations.

Prototype 1 is valuable because it provides an implementation lineage for
bounded runtime engineering. It shows how boundary, trace, viability,
controlled action, and governed interfaces can be made concrete.

Prototype 1 should not be treated as the current implementation contract. Its
specific runtime root, CLI commands, version sequence, file names, schemas,
task system, and command interface are historical or optional unless Prototype
3 explicitly adopts them.

### Prototype 2: Expanded Cognitive Prototype

Prototype 2 is the expanded cognitive prototype. It develops the bounded
predictive machine into a detailed cognitive canon with documents for:

- Machine body.
- Sensorium and signal.
- Priors and starting model.
- Prediction frames.
- Signal interpretation.
- Prediction error and precision.
- Belief state and belief update.
- Action as future error management.
- Memory as reconstruction.
- Self/other-cause modeling.
- Machine metacognition.
- Cognitive tick.
- Cognitive data model.
- Developmental ladder.
- Relationship to safety.
- First build.
- Original alignment evaluation.

Prototype 2 is useful because it gives technical depth to the current design.
It contains relationship rules, object names, maturity gates, negative tests,
alignment invariants, and detailed implementation sketches.

Prototype 2 should be treated as inherited supporting detail. It clarifies
Prototype 3 concepts, but its full 26-phase cognitive tick, complete data
model, developmental rung list, and A-series schema vocabulary are not
mandatory current requirements unless adopted by a current Prototype 3-facing
technical document.

### Prototype 3: Current Design

Prototype 3 is the current design. Its root files directly inside
`Source Documents/` provide the present source of truth.

Prototype 3 reframes the project as a bounded predictive machine or bounded
predictive cognitive runtime. It emphasizes:

- Not starting as a chatbot, generic agent, tool wrapper, memory assistant, or
  goal system.
- Machine body and boundary before capability.
- Signal as not truth.
- Prediction before learning.
- Interpretation before belief update.
- Evidence quality before update strength.
- Belief as structured model state.
- Action as bounded and expected-effect-bearing, not obedience.
- No-action as valid.
- Memory as reconstructive, not storage.
- Uncertainty as a first-class output.
- Safety shell around the cognitive core.
- First build proving one clean loop rather than broad usefulness.

Prototype 3 is less exhaustive than Prototype 2, but it has higher precedence.
Where Prototype 3 is simpler or less specific, the missing detail should be
marked unresolved rather than filled in automatically from older generations.

## What Changed Between Generations

Prototype 1 to Prototype 2:

- Shifted from runtime-governance implementation lineage to explicit cognitive
  architecture.
- Expanded state, trace, adaptation, prediction, action, and recovery into
  machine body, signal, prediction, interpretation, error, precision, belief,
  action, memory, cause, metacognition, tick, and data model.
- Clarified that safety governance is necessary but not the whole cognitive
  architecture.
- Added developmental and alignment checks to prevent drift into generic
  agents.

Prototype 2 to Prototype 3:

- Reframed the project in clearer public and technical language.
- Simplified the current loop around Prototype 3's practical terms:
  prediction, signal, interpretation, mismatch, evidence quality, scoped belief
  update, action or no-action, outcome, memory, uncertainty.
- Made the first build explicitly narrow: prove the loop, not intelligence.
- Softened or deferred detailed Prototype 2 machinery where the current design
  has not confirmed it.
- Clarified the system as pre-agent and boundary-first rather than
  agent-first.

Across all generations:

- The project rejects unbounded agent behavior.
- Boundary and trace matter.
- Prediction matters.
- Signals are not truth.
- Action must be governed.
- Memory must remain evidence-linked.
- Capability should grow through controlled stages rather than convenience.

## Ideas That Survived Across All Generations

These ideas are stable lineage concepts:

- The system is bounded.
- Technical access is not permission.
- Traceability is foundational.
- Capability should be added conservatively.
- The runtime should fail closed or shrink capability when safety evidence is
  missing.
- Prediction or expectation should precede evaluation.
- Mismatch matters only when interpreted and weighted.
- Learning should be evidence-grounded.
- Action should be constrained and expected-effect-bearing.
- Outcome should be observed separately from action attempt.
- Memory should preserve evidence rather than become unsupported summary.
- Human input should be governed rather than treated as unlimited authority.
- The system should avoid generic agent, chatbot, tool-first, memory-first, and
  goal-first drift.

These ideas may be cited as cross-generation continuity, but the current
wording and requirements should still come from Prototype 3 where available.

## Prototype 2 Details That Are Inherited but Not Mandatory

Prototype 2 details should be treated as inherited support unless adopted by
current technical docs. Examples include:

- The full 26-phase cognitive tick.
- Exact A-series object names such as `PredictionFrame`,
  `SignalEnvelope`, `InterpretedObservation`, `PredictionError`,
  `PrecisionEstimate`, `WeightedPredictionError`, `MetacognitiveState`, and
  `CognitiveTick`.
- The full cognitive data model and all proposed schema fields.
- Detailed developmental rungs D0-D14.
- Alignment scorecards and full original-alignment evaluation report formats.
- Detailed lifecycle states such as quarantined, superseded, revised,
  archived, or delayed.
- Rich precision taxonomies and typed error taxonomies.
- Complete cause-classification machinery.

These are often good implementation candidates. They should be introduced as
current only when the current documentation explicitly promotes them.

## Prototype 1 Details That Are Historical or Optional

Prototype 1 details should be treated as historical implementation lineage or
optional inspiration. Examples include:

- The V0-V9 version sequence as the required build order.
- The `machine_cognition_runtime/` bounded root as a required runtime path.
- Specific CLI commands such as `run-once`, `status`, `traces`, `adapt`,
  `predict`, `check-predictions`, `recover`, or `process-commands`.
- Specific state files such as `current_state.json`,
  `previous_state.json`, `runtime_status.json`, or `viability.json`.
- Specific trace files such as `events.jsonl`.
- The structured command queue and result stream as the required human
  interface.
- The constrained task system with max-step limits as a current requirement.
- Exact controlled actions such as `heartbeat_write`, `no_op`, or
  `read_external`.

Prototype 1 remains useful as proof that bounded state, trace, viability,
governed interfaces, and recovery can be implemented. It should not override
Prototype 3's current first-build scope.

## Conflict Handling Rules

When source generations conflict, use these rules:

- Prototype 3 wins over Prototype 2 and Prototype 1.
- Prototype 2 can clarify Prototype 3 only when it does not contradict or
  over-specify the current design.
- Prototype 1 can inspire implementation only when it does not replace the
  current architecture with the older runtime path.
- If Prototype 3 is silent and Prototype 2 is specific, mark the detail as
  inherited or proposed, not current.
- If Prototype 3 is silent and only Prototype 1 is specific, mark the detail as
  historical or optional.
- If older material introduces a capability that Prototype 3 delays, treat the
  capability as unresolved or future work.
- If older material makes a broader claim than Prototype 3, use the narrower
  current claim.
- If current docs adopt an older detail, cite it as adopted current guidance
  and explain the adoption scope.

The default should be conservative:

```text
current if confirmed by Prototype 3
inherited if useful from Prototype 2
historical or optional if only present in Prototype 1
unresolved if required for implementation but not specified by Prototype 3
```

## Older Details That Should Not Automatically Become Current

Do not automatically promote:

- Prototype 2's 26-phase cognitive tick as the mandatory first-build loop.
- Prototype 2's full cognitive data model as final schema.
- Prototype 2's complete developmental ladder as the current implementation
  roadmap.
- Prototype 2's original-alignment scorecard as a required release process.
- Prototype 1's V0-V9 sequence as the required current build path.
- Prototype 1's CLI command set as the required user interface.
- Prototype 1's bounded runtime root as the required project layout.
- Prototype 1's task system as a current core primitive.
- Prototype 1's structured command channel as the required human interface.
- Any older external interface, file operation, or command mechanism as an
  admitted current capability.

These older details may be valuable. They become current only through explicit
adoption under the Prototype 3 precedence rule.

## How Future Docs Should Use Older Generations

Future technical documentation should:

- Start from Prototype 3 root sources.
- Cite Prototype 2 only after the current concept is established.
- Label Prototype 2 material as inherited, supporting, optional, proposed, or
  unresolved.
- Cite Prototype 1 only for historical lineage, implementation inspiration, or
  comparison.
- Avoid wording that treats all three generations as one merged canon.
- Avoid using A-series or V-series detail as mandatory unless current docs have
  adopted it.
- Preserve the difference between current architecture and historical build
  paths.
- Call out unresolved areas instead of filling them silently from older docs.
- Prefer current Prototype 3 terms where available: bounded predictive machine,
  machine body, boundary, signal, prediction, interpretation, evidence quality,
  belief update, action or no-action, outcome, memory, uncertainty, safety
  shell.

A good citation pattern is:

```text
Current requirement:
Prototype 3 defines signal as not truth.

Inherited support:
Prototype 2's SignalEnvelope can guide future schema design.

Historical lineage:
Prototype 1's trace-first runtime shows one possible way to persist evidence.
```

## Documentation Status Labels

Use these labels consistently:

- `Current`: confirmed by Prototype 3 or adopted by current technical docs.
- `Inherited`: useful detail from Prototype 2 that supports current concepts.
- `Historical`: Prototype 1 or older lineage material.
- `Optional`: possible implementation choice not required by current design.
- `Proposed`: recommended by current technical docs but not final schema or
  runtime contract.
- `Unresolved`: needed for implementation but not specified enough by
  Prototype 3.

These labels should appear wherever older material could be mistaken for a
current requirement.

## Implementation Implications

For the first build:

- Build one Prototype 3 loop first.
- Keep machine body, boundary, trace, viability, prediction, signal,
  interpretation, evidence quality, belief update, action/no-action, outcome,
  memory, and uncertainty visible.
- Use Prototype 2's data model and tick as design support, not mandatory scope.
- Use Prototype 1's bounded runtime and trace lineage as inspiration, not the
  required runtime path.
- Delay broad tools, web access, external interfaces, task systems, goal
  structures, and long-term memory until the current loop is proven.

The first build should be boring, inspectable, and aligned. A small loop that
preserves source precedence is better than a powerful implementation that
collapses into generic agent behavior.

## Open Questions

This section preserves local context. Use `docs/technical/12-open-questions.md`
as the consolidated decision tracker.

- Which Prototype 2 object names should be promoted into current schemas?
- Should the current docs standardize on `LoopRecord` or `TickRecord`?
- Which Prototype 1 trace/runtime ideas should be retained in the first
  implementation?
- Does Prototype 3 intend to preserve any part of the V0-V9 version sequence as
  an official roadmap?
- How much of Prototype 2's developmental ladder should become current project
  governance?
- Should original-alignment reporting become a required documentation or
  release practice?
- What exact process should be used to adopt an older detail into current
  architecture?
- How should future docs mark areas where Prototype 3 is silent but Prototype 2
  gives strong implementation guidance?
- Which older safety or interface mechanisms should remain permanently
  historical rather than eligible for adoption?
