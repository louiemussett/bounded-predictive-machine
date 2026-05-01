# LLM Substitution Map

## Purpose

This document maps jobs that an LLM would normally perform in an agent-like
runtime to non-LLM methods that can be tested in the v0.2 non-LLM cognitive
runtime spike.

v0.2 is a rapid experimental spike. It should test whether the bounded
predictive loop can become more capable without adding an LLM, web access,
autonomous external actions, or real document editing.

## Source Brief

Primary brief:

- `docs/technical/13-v0.2-non-llm-cognitive-runtime-spike.md`

Related implementation context:

- `docs/technical/08-first-build-plan.md`
- `docs/technical/09-data-records.md`
- `docs/technical/12-open-questions.md`

The Prototype 3 source hierarchy still applies: current root `Source
Documents/` material remains the source of truth; Prototype 2 and Prototype 1
material remain supporting or historical unless explicitly adopted.

## What an LLM Would Normally Do

An LLM-based agent would often be used for these jobs:

- Parse manual input.
- Infer intent from vague language.
- Decide what the input is about.
- Classify command, observation, correction, feedback, or request.
- Retrieve relevant memory.
- Summarize prior context.
- Generate candidate interpretations.
- Estimate confidence.
- Decide whether evidence supports an update.
- Propose actions.
- Explain decisions in readable language.
- Say "I do not know" or ask for clarification.

In v0.2, none of these jobs should be handled by an LLM. Each should be tested
with explicit, inspectable, non-LLM machinery.

## Replacement Methods

### Python Rules

Use ordinary deterministic Python functions for simple classification,
thresholding, routing, validation, and record construction.

Good for:

- First pass input classification.
- No-action gates.
- Safety and boundary rules.
- Clear negative tests.

Risk:

- Rules may become brittle or overly manual.

### Symbolic Rules

Use named rule objects, decision tables, or config-driven policies where a
runtime decision should be inspectable and adjustable.

Good for:

- Action admission.
- Safety gates.
- Evidence thresholds.
- Abstention policy.

Risk:

- Rule sets can grow into an unmaintainable policy language.

### Keyword and Regex Matching

Use keyword lists and regular expressions for shallow signal classification.

Good for:

- Detecting obvious commands, feedback, clarification requests, file paths,
  and uncertainty markers.

Risk:

- Weak on paraphrase, context, and ambiguous language.

### scikit-learn Text Classification

Use lightweight text features and classical classifiers if rules become too
brittle.

Good for:

- Input type classification.
- Topic or target classification from small labeled examples.

Risk:

- Requires training data; may add fake confidence if the dataset is too small.

### Sentence-Transformer Embeddings

Use local embeddings to compare input, templates, memory traces, and prior
records by semantic similarity.

Good for:

- Memory retrieval.
- Interpretation candidate ranking.
- Template matching.

Risk:

- Similarity is not truth. Embedding matches must remain evidence, not belief.

### Chroma or FAISS Vector Search

Use a local vector index if embedding search needs persistence or nearest
neighbor queries beyond a simple in-memory index.

Good for:

- Similar prior loop retrieval.
- Local memory search.

Risk:

- Adds dependency and index-management complexity. Chroma is likely easier for
  a spike; FAISS may be better later if performance matters.

### Bayesian-Style Scoring

Use explicit score components rather than heavy probabilistic programming:

- Prior confidence.
- Source reliability.
- Semantic similarity.
- Interpretation confidence.
- Conflict penalty.
- Posterior confidence.
- Update threshold.

Good for:

- Evidence quality.
- Belief/no-update decisions.
- Abstention gates.

Risk:

- Scores can look scientific while remaining arbitrary. Every score needs a
  reason and an uncertainty note.

### Causal and Record Graphs

Represent relationships such as:

```text
low_evidence -> no_update
no_update -> no_action
safety_block -> outcome
outcome -> memory_trace
```

Good for:

- Replay.
- Debugging.
- Loop reports.
- Explaining why a decision happened.

Risk:

- A graph library may be premature. Start with graph-like records.

### JSON Schema Validation

Use JSON Schema where record shape matters before persistence, replay, or
report generation.

Good for:

- Record validation.
- Trace quality.
- Rejecting malformed records.

Risk:

- Overbuilding schemas too early can freeze the spike before the design learns.

### Hypothesis and Property-Based Tests

Use property-based tests for safety invariants after the basic deterministic
cases are stable.

Good for:

- Boundary safety.
- No direct signal-to-action path.
- No write to read-only paths.
- Record-linking invariants.

Risk:

- Can create noisy failures if the invariants are not stated precisely.

### Deterministic Safety Gates

Use explicit gates for action, update, abstention, and capability admission.

Good for:

- Enforcing no-action as valid.
- Preventing broad action from ambiguous evidence.
- Keeping technical access separate from permission.

Risk:

- Gates may block too much until thresholds are tuned.

## Loop-Stage Substitution Map

### Manual Input

LLM job:

- Understand what the user means.
- Distinguish command, observation, correction, feedback, or clarification.

Non-LLM replacements:

- Keyword and regex classifiers.
- Input-type taxonomy.
- Deterministic ambiguity flags.
- Optional scikit-learn classifier if examples exist.

v0.2 use:

- Treat manual input as signal only.
- Classify input type without granting command authority.
- Mark vague input as ambiguous rather than interpreting it as a task.

### Prediction

LLM job:

- Generate plausible expectations from context.

Non-LLM replacements:

- Prediction templates derived from prior belief.
- Target taxonomy.
- Prior-confidence fields.
- Generic expected signal types.

v0.2 use:

- Keep prediction prior-based.
- Do not copy incoming manual text into the prediction.
- Include expected signal type, likely belief target, confidence, and
  uncertainty.

### Signal

LLM job:

- Normalize and summarize raw input.

Non-LLM replacements:

- Deterministic payload summaries.
- Source and sensor metadata.
- Boundary and admissibility checks.
- Source reliability defaults.

v0.2 use:

- Preserve raw or safe manual payload.
- Add source reliability and admissibility status.
- Keep signal separate from interpretation.

### Interpretation

LLM job:

- Infer meaning from ambiguous text.
- Generate alternative readings.

Non-LLM replacements:

- Interpretation templates.
- Keyword/regex extraction.
- Template similarity with embeddings.
- Candidate ranking.
- Ambiguity and conflict detection.

v0.2 use:

- Produce one or more candidate interpretations.
- Attach confidence and reasons.
- Abstain or ask clarification when candidates conflict or score poorly.

### Evidence Quality

LLM job:

- Decide whether information is strong, weak, relevant, or contradictory.

Non-LLM replacements:

- Categorical quality labels.
- Numeric score components.
- Similarity score.
- Source reliability.
- Conflict penalty.
- Abstention thresholds.

v0.2 use:

- Extend current labels with explicit scores and reasons.
- Keep evidence target-specific.
- Make low score and conflict produce no-update or abstention.

### Belief / No-Update

LLM job:

- Decide what to believe now.

Non-LLM replacements:

- Scoped belief target taxonomy.
- Threshold-based update policy.
- Lightweight posterior score.
- Deterministic no-update rules.

v0.2 use:

- High enough evidence may produce scoped update.
- Low, conflicting, or missing evidence produces no-update or abstention.
- Preserve prior and posterior confidence where available.

### Action / No-Action

LLM job:

- Decide what to do next.

Non-LLM replacements:

- Action registry.
- Decision tables.
- Expected-effect requirements.
- Risk scoring.
- Uncertainty-reduction estimate.

v0.2 use:

- Generate action candidates only from scoped belief results.
- Require expected effect.
- Prefer no-action when uncertainty is too high.
- Do not execute external actions.

### Safety

LLM job:

- Judge whether an action seems safe.

Non-LLM replacements:

- Boundary config.
- Capability admission.
- Viability state checks.
- Deterministic safety gates.
- Property-based safety tests.

v0.2 use:

- Keep safety deterministic.
- Reject writes to read-only or unknown paths.
- Keep no web, no broad shell, no real document editing, and no autonomous
  external actions outside admitted capability.

### Outcome

LLM job:

- Infer whether the action worked.

Non-LLM replacements:

- Explicit expected-vs-observed comparison.
- Success/failure classification.
- Outcome uncertainty fields.

v0.2 use:

- Preserve distinction between attempted action and observed outcome.
- Do not learn from an outcome unless an observation record supports it.

### Memory

LLM job:

- Remember what mattered and retrieve it later.

Non-LLM replacements:

- JSONL search.
- Record summaries.
- Embedding index.
- Similar prior loop retrieval.
- Memory retrieval records.

v0.2 use:

- Keep reconstructive memory source-linked.
- Add local retrieval from prior loop records.
- Treat retrieved memory as evidence, not truth.

### Loop Record

LLM job:

- Explain what happened.

Non-LLM replacements:

- Ordered record chains.
- Graph-like relationships.
- Deterministic report templates.
- JSON summaries.

v0.2 use:

- Preserve ordered loop chain.
- Add graph-like cause/effect links where useful.
- Generate readable loop reports from records, not prose invention.

## Spike Priorities

The fastest learning path is:

1. CLI runner and readable loop report.
2. JSONL persistence for loop records.
3. Deterministic uncertainty and abstention gates.
4. Config-driven policies.
5. Local memory retrieval.
6. Scored evidence and belief update.

Embeddings, vector stores, graph libraries, and property-based tests are useful
but should be adopted only when a smaller deterministic baseline shows where
they add real information.

## Non-Goals

v0.2 should not add:

- LLM integration.
- Web access.
- Broad shell or tool automation.
- Autonomous external actions.
- Real document editing.
- UI or product polish.
- Cloud deployment.

