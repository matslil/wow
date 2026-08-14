---
id: WOW-CORE-CHANGE
classification: core
customization: prohibited
---

# Pull-Request Change Workflow

All persistent repository changes use pull requests. A PR represents one
coherent engineering outcome and identifies its stage, intent, model and
traceability impact, evidence, uncertainty, decisions, and follow-on work.

Use a focused PR for a small independent outcome. Use a larger PR with multiple
commits when its parts are required for one coherent outcome. Every commit must:

- leave source, model, documentation, and generated artifacts consistent;
- pass checks applicable to that commit;
- provide a meaningful, reviewable engineering increment;
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
implement verified commits, open or update the PR, record evidence, then begin
the next unblocked outcome. Waiting for review is not a reason to pause.

Use [`../templates/pull-request.md`](../templates/pull-request.md). A PR may be
stacked when dependencies are explicit and every commit remains valid.
