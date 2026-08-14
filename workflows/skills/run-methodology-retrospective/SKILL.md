---
name: run-methodology-retrospective
description: Evaluate evidence from a project using the Way of Working methodology, improve local execution, and prepare a human-approved upstream methodology proposal. Use at stage tollgates, after larger deliveries, incidents or retirement, and for repeated process friction.
---

# Run a Methodology Retrospective

Read `core/README.md`, the project definition, and
`workflows/methodology-retrospective.md`.

1. Establish the project and methodology baselines, stage, scope, and trigger.
2. Gather concise evidence from engineering outcomes, PRs, model history,
   verification, incidents, rework, delays, and prior decisions.
3. Separate observed fact from inference and individual performance from process.
4. Identify what helped, hindered, was missing, was excessive, or caused rework.
5. Classify the cause as project definition, execution, profile, starter, or core.
6. Deliver local corrections through a normal project PR without weakening core.
7. When the issue generalizes, prepare `templates/methodology-proposal.md` with
   evidence, exact proposed change, tradeoffs, compatibility, migration, and
   validation.
8. Ask the designated human whether to submit it upstream. Continue independent
   local improvement work before pausing.
9. Keep unaccepted proposals distinct from the active core and trace the upstream
   decision back to the retrospective.

Report only the outcome, important evidence, classification, local action,
upstream decision requested, and next step.
