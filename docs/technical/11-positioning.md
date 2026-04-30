# Positioning

## Purpose

This document positions the current Prototype 3 design relative to nearby
technical categories: transformer models, ChatGPT-style products, ordinary AI
agents, tool orchestration systems, memory systems, safety wrappers,
predictive processing, active inference, control systems, cognitive
architectures, and event-sourced systems.

The purpose is not to overclaim novelty. It is to describe the level at which
the architecture operates and to prevent category mistakes.

## Source Precedence

Use this precedence when source generations differ:

1. Prototype 3 current design: root files directly inside `Source Documents/`.
2. Prototype 2 supporting design detail: `Source Documents/1-17/`.
3. Prototype 1 original implementation lineage: `Source Documents/V0 - V9/`.

Prototype 3 is the source of truth for this document. Prototype 2 and Prototype
1 are supporting or historical context only.

## Sources Used

Primary Prototype 3 sources:

- `Source Documents/0. White Paper.md`
- `Source Documents/0. Human brain and biology.md`
- `Source Documents/1. The Big Idea.md`
- `Source Documents/2. Why This Is Not Just an AI Agent.md`

Supporting context:

- Prototype 2 cognitive-core documents in `Source Documents/1-17/`
- Prototype 1 V0-V9 runtime lineage in `Source Documents/V0 - V9/`

## Current Positioning Summary

Prototype 3 is best described as:

```text
a bounded predictive cognitive runtime architecture
```

or more fully:

```text
a safety-governed predictive cognitive runtime architecture for bounded
machine cognition
```

It operates at the runtime-architecture level. It is not a model architecture,
not a transformer variant, not an LLM, not a chatbot product, not a human brain
model, not a consciousness architecture, and not an ordinary agent framework.

Its core concern is:

```text
How should a bounded machine runtime receive signals, predict, interpret
evidence, update belief, choose action or no-action, observe outcome,
reconstruct memory, monitor uncertainty, and remain inside a safety shell?
```

That is different from asking how a neural network predicts tokens, how a chat
product responds to users, or how an agent completes tasks.

## Level of Architecture

The design operates above individual model architecture and below product
experience.

It is not concerned with:

- Attention heads.
- Embedding layers.
- Transformer blocks.
- Model pretraining.
- Token probability distributions.
- Chat UI behavior.
- Tool-call formatting.

It is concerned with:

- Machine body.
- Boundary.
- Signal discipline.
- Prediction.
- Interpretation.
- Evidence quality.
- Belief update.
- Action and no-action.
- Outcome observation.
- Reconstructive memory.
- Uncertainty.
- Safety-shell governance.
- First-build records.

A transformer or LLM could later be admitted as a component inside this
architecture. It might help propose interpretations, summarize traces, draft
responses, or render explanations. It must not become the owner of belief,
action authorization, memory truth, safety policy, or runtime control.

## GPT and Transformer Models

GPT-style systems are transformer-based language models. Their architecture is
primarily a model architecture: it defines how a trained model processes token
or multimodal inputs and produces outputs.

The bounded predictive machine is not a transformer model.

Similarities:

- Both involve prediction in some form.
- Both may process language.
- A transformer could be used as a component inside the runtime.

Differences:

- GPT predicts token continuations; this architecture governs a runtime loop.
- GPT's core substrate is learned model parameters; this architecture's core
  substrate is explicit state, signals, records, boundaries, and safety checks.
- GPT output is not automatically belief, memory, truth, or action authority in
  this architecture.
- The bounded predictive machine requires traceable belief update and action
  governance outside the model.

Correct relationship:

```text
Transformer model:
model-level sequence prediction

Bounded predictive machine:
runtime-level predictive cognition governance
```

## ChatGPT-Style Products

ChatGPT-style products are interactive applications built around language model
interaction. They usually emphasize conversation: user input, model response,
tool use, memory, and product behavior.

The bounded predictive machine is not a ChatGPT-style product.

Similarities:

- It may eventually expose a human-facing interface.
- It may use language as one kind of signal.
- It may use an LLM for limited assistance.

Differences:

- Human text is signal, not direct command.
- The system begins with body and boundary, not conversation.
- The first build should prove a loop, not a chat experience.
- A response is one possible action, not the definition of the system.

Correct relationship:

```text
Chat product:
conversation interface over one or more models and tools

Bounded predictive machine:
governed runtime that may eventually include a conversation interface
```

## Ordinary AI Agents

Ordinary AI agents usually begin with a task or goal, plan steps, use tools,
observe results, and continue until the task is complete.

Prototype 3 is explicitly pre-agent. It defines what should exist before
agent-like behavior is trusted.

Similarities:

- It can consider actions.
- It may eventually support bounded tasks.
- It may eventually use tools as admitted capabilities.

Differences:

- It begins with machine body, boundary, signal, prediction, and evidence.
- It does not treat task completion as the primary measure of success.
- It does not treat user command as direct authority.
- It preserves no-action as valid.
- Action requires expected effect, permission, boundary, traceability,
  viability, and safety-shell review.

Correct relationship:

```text
Ordinary agent:
goal or task -> plan -> tool/action -> observation

Bounded predictive machine:
body -> prediction -> signal -> interpretation -> evidence quality ->
belief update -> action or no-action under safety shell
```

The architecture may support agent-like behavior later, but agenthood is not
the starting assumption.

## Tool Orchestration Systems

Tool orchestration systems coordinate calls to tools, APIs, functions, browsers,
files, or external services.

The bounded predictive machine is not a tool orchestration system.

Similarities:

- It may eventually call tools.
- It needs action records and outcome observation.
- It may route capabilities through registries or policy checks.

Differences:

- Tools are not primitive.
- Tool availability is not permission.
- Tool use is one kind of action, and action must have expected effect.
- Capability must be admitted, scoped, traceable, monitored, and revocable.
- The system should not add tools to compensate for missing signal, prediction,
  belief, memory, or safety structure.

Correct relationship:

```text
Tool orchestration:
coordinate tool execution

Bounded predictive machine:
govern whether action, including tool use, is justified and allowed
```

## Memory Systems

Memory systems store, retrieve, summarize, embed, or index past information.

The bounded predictive machine is not a memory system.

Similarities:

- It requires memory.
- It may store records.
- It may later use retrieval or summaries.

Differences:

- Memory is reconstructive, not storage alone.
- Memory must remain connected to prediction, signal, interpretation,
  evidence quality, belief update, action, outcome, and uncertainty.
- A memory summary is not source evidence.
- A retrieved memory does not automatically become belief.

Correct relationship:

```text
Memory system:
stores and retrieves information

Bounded predictive machine:
reconstructs cognitive history from source-linked records
```

## Safety Wrappers

Safety wrappers constrain or filter behavior around an existing model, agent,
or tool system.

Prototype 3 includes a safety shell, but it is not merely a safety wrapper.

Similarities:

- It has boundary checks.
- It has permission and capability controls.
- It requires traceability, viability, recovery, and human review where needed.

Differences:

- Safety is part of the architecture from the beginning.
- Safety governs a cognitive loop; it does not simply filter outputs.
- The cognitive core still matters: prediction, interpretation, evidence
  quality, belief update, action, memory, and uncertainty.
- A safety-only runtime would be incomplete because it would lack the bounded
  predictive cognitive core.

Correct relationship:

```text
Safety wrapper:
external guard around a model or agent

Bounded predictive machine:
cognitive core inside a safety shell
```

## Predictive Processing

Predictive processing and predictive coding theories describe cognition as a
process of maintaining internal models, predicting sensory input, comparing
prediction with signal, and updating from prediction error.

Prototype 3 is strongly aligned with predictive processing at the conceptual
logic level.

Similarities:

- Prediction precedes evaluation.
- Signal is interpreted against a model.
- Mismatch or error can drive model update.
- Precision or evidence quality affects update strength.
- Perception-like interpretation is not passive receipt of truth.

Differences:

- Prototype 3 is not a biological brain theory.
- It does not claim to implement cortical layers, neurons, synapses, dopamine,
  biological interoception, emotion, or consciousness.
- It translates predictive-processing ideas into machine runtime architecture.
- It adds explicit boundary, trace, capability admission, viability, recovery,
  and safety-shell governance.

Correct relationship:

```text
Predictive processing:
conceptual inspiration for prediction, error, precision, and update

Bounded predictive machine:
machine-runtime architecture using predictive discipline under safety governance
```

## Active Inference

Active inference extends predictive-processing ideas by treating action as a
way to affect future signals and reduce future error or uncertainty.

Prototype 3 is related to active inference, especially in its treatment of
action.

Similarities:

- Action is not obedience.
- Action has expected future effect.
- Action can reduce uncertainty, improve viability, test a model, or affect
  future evidence.
- Outcome matters because action learning depends on observed effect.

Differences:

- Prototype 3 does not adopt the full mathematical framework of active
  inference.
- It does not define free-energy equations as current implementation
  requirements.
- It adds explicit permission, boundary, capability admission, traceability,
  recoverability, and safety-shell checks.

Correct relationship:

```text
Active inference:
action and perception as prediction-error regulation

Bounded predictive machine:
bounded action through expected effect, outcome observation, and safety checks
```

## Control Systems

Control systems monitor state, compare observed state with desired or expected
state, and apply actions to reduce deviation.

Prototype 3 has control-system-like elements.

Similarities:

- It compares expected and observed conditions.
- It tracks state and viability.
- It may choose actions based on mismatch.
- It observes outcomes.

Differences:

- It handles semantic signals and human text, not only predefined measured
  variables.
- It requires interpretation before update.
- It uses reconstructive memory and uncertainty tracking.
- It distinguishes signal, belief, memory, action, outcome, and safety.
- It does not begin with an optimization target or goal-maximizing controller.

Correct relationship:

```text
Control system:
feedback control over defined state variables

Bounded predictive machine:
cognitive runtime with feedback, interpretation, belief update, memory, and
safety governance
```

## Cognitive Architectures

Cognitive architectures define structured systems for perception, memory,
reasoning, action, and learning.

Prototype 3 is closest to this category, but with a machine-runtime and safety
governance emphasis.

Similarities:

- It defines a cognitive loop.
- It separates signal, interpretation, belief, action, memory, and uncertainty.
- It is concerned with how a system maintains and updates a working model.

Differences:

- It is not trying to simulate human cognition.
- It avoids claims about consciousness, emotion, personality, or human-like
  selfhood.
- It begins with a machine body and boundary.
- It treats safety shell, capability admission, traceability, and viability as
  foundational.
- It is pre-agent and capability-conservative.

Correct relationship:

```text
Cognitive architecture:
structured architecture for cognition-like processes

Bounded predictive machine:
machine-native cognitive runtime architecture with predictive loop and safety shell
```

## Event-Sourced Systems

Event-sourced systems preserve state changes as events so current state can be
reconstructed from history.

Prototype 3 has a strong event-sourcing affinity because trace and memory must
preserve evidence.

Similarities:

- Records matter.
- State should be reconstructable from event history.
- Auditability and lineage are important.
- Summaries should not replace source events.

Differences:

- Prototype 3 records are cognitive evidence, not only application events.
- Memory reconstructs prediction, signal, interpretation, update, action,
  outcome, and uncertainty.
- Belief update depends on interpreted evidence quality, not only event
  occurrence.
- Safety and capability governance are architectural requirements, not merely
  operational concerns.

Correct relationship:

```text
Event-sourced system:
application state reconstructed from event history

Bounded predictive machine:
cognitive state and memory reconstructed from traceable evidence chains
```

## What the Architecture Is Not

Prototype 3 should not be described as:

- A transformer.
- An LLM.
- A ChatGPT competitor.
- A chatbot.
- An ordinary AI agent.
- A tool-use framework.
- A memory database.
- A safety wrapper alone.
- A human brain model.
- A consciousness architecture.
- A personality framework.
- A goal optimizer.
- A full active-inference implementation.
- A general theory of biological cognition.

These labels either operate at the wrong level or imply claims Prototype 3 does
not make.

## What the Architecture Is Similar To

The architecture is similar to:

- Predictive processing at the level of prediction, signal, mismatch,
  precision, and model update.
- Active inference at the level of action as expected future effect.
- Control systems at the level of feedback and outcome observation.
- Cognitive architectures at the level of structured signal, belief, action,
  memory, and uncertainty.
- Event-sourced systems at the level of traceability and reconstruction.
- Safety-governed runtimes at the level of boundary, capability admission,
  viability, recovery, and audit.

It is a synthesis of these influences into a bounded machine-runtime design.
That synthesis may be useful and distinctive, but this document should not
claim that every component is novel.

## Responsible Claim

A responsible current claim is:

```text
Prototype 3 defines a bounded predictive cognitive runtime architecture:
a safety-governed machine-runtime design that structures signal handling,
prediction, interpretation, evidence quality, belief update, action,
outcome observation, reconstructive memory, uncertainty, and capability
governance.
```

Avoid stronger claims such as:

- This is a new neural model.
- This is a transformer alternative.
- This is a brain implementation.
- This is consciousness.
- This is a complete agent framework.
- This solves autonomy.
- This proves intelligence.

The first build should prove only that one bounded predictive loop can run and
be reconstructed from records.

## Open Questions

- What term should be standardized for the architecture: bounded predictive
  machine, bounded predictive cognitive runtime, or safety-governed predictive
  cognitive runtime?
- Which comparison should be emphasized for technical audiences: cognitive
  runtime architecture, event-sourced cognitive runtime, or predictive
  processing-inspired runtime?
- How should future docs cite predictive processing and active inference
  without implying biological or mathematical equivalence?
- What role may an LLM play in the first implementation, if any?
- Which parts of Prototype 2's cognitive architecture vocabulary should be
  promoted into current positioning language?
- How should the project distinguish later agent-like behavior from current
  pre-agent architecture?
- What evaluation should prevent tool orchestration, memory storage, or safety
  wrapper designs from being mistaken for the full architecture?
- How should novelty be stated conservatively once implementation exists?
