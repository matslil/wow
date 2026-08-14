---
id: WOW-STAGE-DEVELOPMENT
classification: core
customization: prohibited
---

# Development

Refine needs into requirements, architecture, behavior, interfaces, and
verification cases. Realize small traced increments, integrate them, and verify
each through PRs whose commits remain valid. Validate representative behavior
against intended stakeholder outcomes.

## Zig-zag co-evolution

Development is progressive but not one-way. Move repeatedly between needs,
requirements, architecture, design, implementation, integration, verification,
and validation. Later work is evidence about earlier work. When it exposes an
incorrect assumption, missing need, poor requirement, unsuitable architecture,
or weak verification case, propagate the insight back to the earliest affected
authoritative item, then analyze and update every downstream relation.

Do not preserve a defective upstream statement by compensating silently in code
or tests. Record the finding, revise it within project authority, retain decision
history, and re-verify affected results. If the insight changes stakeholder
intent, system boundary, concept, accepted risk, or another reserved decision,
ask the designated human and continue independent work.

Assess every requirement and the complete set using
[`../../core/assurance.md`](../../core/assurance.md). Match requirements to
verification cases, express textual requirements using EARS, and validate them
against needs and representative use.

The tollgate assesses model completeness, traceability, implementation,
integration, verification, validation, unresolved defects, operational
readiness, and risk. A human authorizes Production and Transition.
Use [`tollgate.md`](tollgate.md).
