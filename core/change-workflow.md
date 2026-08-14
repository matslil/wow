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

The normal loop is: select the next authorized outcome, create a branch,
implement verified commits, open or update the PR, record evidence, then begin
the next unblocked outcome. Waiting for review is not a reason to pause.

Use [`../templates/pull-request.md`](../templates/pull-request.md). A PR may be
stacked when dependencies are explicit and every commit remains valid.
