# Engineering Work

Use this scope for software-intensive engineering, including vibe coding. Shared
[core](../core/README.md) and human prompts govern it. Story-only projects do not
inherit engineering roles, EARS requirements, or tollgates.

Follow the systems-engineering approach retained from WoW: lifecycle outcomes,
iterative needs/requirements/design work, traceability, verification and validation,
and explicit human transition decisions. The basis is the INCOSE Systems Engineering
Handbook and its ISO/IEC/IEEE 15288 process framework; see
[scope and limitations](knowledge/standards-basis.md). This is a tailored workflow,
not a claim of certification or exhaustive standards conformance.

## Load applicable context

1. Read [lifecycle](core/lifecycle.md), [roles](core/roles-and-work-packages.md),
   [authority](core/authority-and-tollgates.md), [model](core/model-and-evidence.md),
   and [assurance](core/assurance.md) for engineering work.
2. Read only the active [stage](stages/README.md), its tollgate and entry skill.
   Use the assigned role's boundary from the role table; load an additional
   role-entry skill only if the project defines one. Do not require missing skills.
3. Load selected [starter](starter/README.md) and language profiles only as needed.
   Rust guidance is [here](profiles/languages/rust/README.md).

Keep project context at the project root (`context.md` or `knowledge/context.md`).
Put requirements in the owning system's `knowledge/requirements.md` or directory;
the main system's knowledge is at root. Subsystems correspond to directories,
not functions. Link needs, architecture, interfaces, implementation, and evidence.

Human prompts enter through [handle-request](../skills/handle-request/SKILL.md).
Bug reports use [fix-bug](skills/fix-bug/SKILL.md). Both follow one PR per requested
item and verify output against root `AI-USAGE.md`. Use
[requirement](templates/requirement.md) and
[tollgate](templates/tollgate.yaml) templates only when applicable.
