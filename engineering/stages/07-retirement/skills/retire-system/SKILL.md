---
name: retire-system
description: Plan and execute withdrawal, archival, reuse classification, recycling, or disposal of a software system or version. Use during Retirement and archive-readiness work.
---

# Retire a System

Read the core, project definition, this stage's `README.md`, and applicable
retention, legal, security, and product profiles.

1. Confirm human-authorized scope, consumers, dependencies, obligations, and dates.
2. Plan communication, migration, data disposition, access revocation,
   infrastructure removal, rollback, and withdrawal verification.
3. Archive the model, source, history, decisions, requirements, build and release
   inputs, tests, evidence, dependencies, licenses, provenance, and restoration steps.
4. Classify each reusable asset and record constraints and confidence.
5. Deliver retirement changes through coherent PRs with valid tested commits.
6. Verify withdrawal and archive restoration, then assess residual obligations.
7. Ask the named human to accept retirement completion.

Never perform an unapproved destructive action. Continue non-destructive archive
and analysis work before pausing for a required human decision. Report concisely.

## Evidence contract

Apply the assigned role from `engineering/core/roles-and-work-packages.md`; use
the stage inputs and affected model traces to bound context and outputs. Record
checks and baseline with `pass`, `fail`, `inconclusive`, `not-applicable`, or
`pending-human`. Follow `core/change-workflow.md`: one PR per requested item,
push every verified commit, open the PR after completing the plan. Summarize
knowledge changes and leave skill acceptance and reserved decisions to humans.
