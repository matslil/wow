---
name: develop-system-increment
description: Coordinate role-scoped definition, realization, integration, verification, and validation outcomes for a traced Development work package. Use when planning or advancing a system increment in Development.
---

# Develop a System Increment

Read the core, project definition, this stage's `README.md`, and selected
profiles. Confirm the assigned role before loading role-specific context.

1. Define one work-package PR with ordered process outcomes, completion criteria,
   role assignments, reserved decisions, and required independence.
2. For the current process outcome, load only its role-entry skill, affected
   trace neighborhood, applicable profiles, and required process or artifact
   skills.
3. Requirements work assesses affected requirements individually and as a set
   using `core/assurance.md`, applies the applicable EARS pattern, and defines
   verification and validation evidence before realization relies on it.
4. Zig-zag across role outcomes as evidence develops. Propagate a later insight
   to the earliest affected item, assign the revision to the appropriate role,
   then update and re-check downstream relations.
5. Complete each role-scoped process outcome as an internally consistent commit
   that passes its applicable checks and records its evidence and verdicts.
6. Use separate integration, verification, validation, and assurance role
   invocations where required; give each only its bounded context package.
7. Review the entire affected engineering chain for consistency, update model
   relations, risks, decisions, limitations, and follow-on work, then complete
   the work-package PR.
8. Assess the Development tollgate when its scope is mature.

Do not pause for a pending review, failed check, missing document, or difficult
task. Pause only when a human answer is required and no independent work remains.
Do not change the work-package contract merely to make an outcome pass. Only the
designated human authorizes transition.
