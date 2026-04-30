# Project Instructions

* Work only inside this repository.
* Keep changes small and focused.
* Do not edit .env files.
* Ask before adding dependencies.
* Ask before deleting files.
* Ask before using network access.
* Do not commit unless I explicitly ask.
* Summarize what changed after every task.



\## Documentation Task Rules



\- Treat `source-docs/` as reference material.

\- Do not edit files inside `source-docs/` unless I explicitly ask.

\- Create new technical documentation inside `docs/technical/`.

\- Preserve the original meaning of the source documents.

\- If something is unclear, list the uncertainty instead of inventing details.

\- Prefer clear technical structure: overview, architecture, concepts, data model, lifecycle, safety model, implementation plan.

\- When summarizing, mention which source files were used.

## Source Hierarchy

The source documents are organized by design generation:

- `Source Documents/V0 - V9/` = Prototype 1 / original design.
- `Source Documents/1-17/` = Prototype 2 design.
- Root files directly inside `Source Documents/` = Prototype 3 / current design.

When creating technical documentation:

- Treat Prototype 3 as the current source of truth.
- Treat Prototype 2 as important supporting architecture and prior prototype context.
- Treat Prototype 1 as original design lineage and historical runtime context.
- Do not flatten all generations into one canon.
- If generations conflict, identify the conflict instead of silently merging them.
- Prefer current Prototype 3 wording unless the user says otherwise.

## Source Hierarchy

The source documents are organized by design generation:

- Root files directly inside `Source Documents/` = Prototype 3 / current design.
- `Source Documents/1-17/` = Prototype 2 design.
- `Source Documents/V0 - V9/` = Prototype 1 / original design.

When creating technical documentation:

- Treat Prototype 3 as the current source of truth.
- Treat Prototype 2 as supporting prior design detail.
- Treat Prototype 1 as original/historical implementation lineage.
- Do not flatten all generations into one current canon.
- If generations conflict, prefer Prototype 3.
- If an older detail is useful but not confirmed by Prototype 3, label it as historical, inherited, optional, or unresolved.

