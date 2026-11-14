---
name: evaluate-system-use
description: Evaluate an operating software system against intended stakeholder outcomes and feed evidence into support, evolution, or renewed exploration. Use during Utilization.
---

# Evaluate System Use

Read the core, project definition, and this stage's `README.md`.

1. Confirm the utilized version, context, intended outcomes, and measures.
2. Gather approved operational, incident, quality, and stakeholder evidence.
3. Compare observed behavior and outcomes with the authoritative model.
4. Trace discrepancies to correction, evolution, Exploration, or Concept work.
5. Deliver durable model, documentation, or automation changes through verified PRs.
6. Assess utilization maturity and recommend continued use, restriction,
   evolution, renewed concept work, or retirement.

Do not accept operational risk or authorize a lifecycle change. Continue useful
work while non-blocking questions remain; pause only for a required human answer.

## Evidence contract

Apply the assigned role from `engineering/core/roles-and-work-packages.md`; use
the stage inputs and affected model traces to bound context and outputs. Record
checks and baseline with `pass`, `fail`, `inconclusive`, `not-applicable`, or
`pending-human`. Follow `core/change-workflow.md`: one PR per requested item,
push every verified commit, open the PR after completing the plan. Summarize
knowledge changes and leave skill acceptance and reserved decisions to humans.
