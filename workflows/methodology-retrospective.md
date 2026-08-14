---
id: WOW-WORKFLOW-RETROSPECTIVE
classification: core
customization: prohibited
---

# Methodology Retrospective

Run a retrospective at each stage tollgate and after a larger delivery, serious
incident, retirement, or repeated process problem. A retrospective evaluates the
methodology, not individual performance, and must not pause otherwise useful
authorized work.

1. Identify the project baseline, methodology version, lifecycle stage, scope,
   and trigger.
2. Compare expected and observed outcomes using PRs, decisions, model history,
   defects, rework, delays, verification results, incidents, and human feedback.
3. Record what helped, what failed, unnecessary work, missing guidance, context
   load, automation opportunities, and unintended incentives.
4. Find the cause and classify it as project definition, local execution,
   selected profile, starter content, or immutable core.
5. Implement project-local corrections through normal PRs. A local rule may be
   stricter than the core but may not weaken or override it.
6. For a generalizable methodology issue, prepare
   [`../templates/methodology-proposal.md`](../templates/methodology-proposal.md).
   Include evidence, affected projects or contexts, proposed wording, tradeoffs,
   compatibility, migration, and validation.
7. Obtain the project's designated human approval before submitting the proposal
   to its `methodology_feedback_repository` as an issue or PR.
8. Keep the proposal status `proposed` until accepted upstream. Do not present it
   as core or alter the recorded methodology version prematurely.
9. Trace the upstream decision back to the retrospective. If accepted, adopt the
   released methodology through a separate project PR.

Upstream maintainers assess whether a proposal is general, preserves core
invariants, remains concise, and has adequate evidence. They may accept, revise,
defer, redirect to starter/profile content, or reject it with rationale.
