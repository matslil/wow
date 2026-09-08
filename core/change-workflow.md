---
id: WOW-CORE-CHANGE
classification: core
customization: prohibited
---

# Pull-Request Change Workflow

All persistent repository changes use pull requests. A PR represents one
completed work package and identifies its stage, intent, baseline, model and
traceability impact, roles, planned process outcomes, evidence, uncertainty,
decisions, and follow-on work.

Define a non-trivial work package before implementation as required by
[`roles-and-work-packages.md`](roles-and-work-packages.md). Use a focused PR for
a small independent outcome. Use a larger PR with multiple commits when several
process outcomes are required to complete one work package. Every commit must:

- leave source, model, documentation, and generated artifacts consistent;
- pass checks applicable to that commit;
- complete a named, reviewable process outcome assigned to one role;
- avoid relying on a later commit to repair deliberate breakage.

A larger change requires a holistic consistency review before its PR is ready.
Treat a change as larger when it affects architecture, public or operational
behavior, multiple requirements or components, an interface, data compatibility,
migration, lifecycle obligations, or several authoritative artifacts. Review the
whole affected chain rather than only changed files: needs, requirements, model,
analysis, decisions, risks, interfaces, implementation, verification, validation,
documentation, operations, support, and retirement. Record affected, unaffected,
not-applicable, and unresolved areas in the PR.

The normal loop is: select the next authorized outcome, create a branch,
define the work package, open or update its PR, execute role-scoped process
outcomes as verified commits, perform the required independent review, record
evidence, then begin the next unblocked outcome. Waiting for review is not a
reason to pause.

Merging updates the repository. It does not by itself approve a model baseline,
lifecycle transition, release, retirement, or risk acceptance.

Use [`../templates/pull-request.md`](../templates/pull-request.md). A PR may be
stacked when dependencies are explicit and every commit remains valid.
