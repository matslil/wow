---
id: WOW-CORE-ASSURANCE
classification: core
customization: prohibited
---

# Assurance

Verification determines whether an information item, model element,
implementation, integration, release, operation, or retirement result conforms
to its specified characteristics. Validation determines whether it is suitable
and sufficient for its intended use and upstream intent. Apply both throughout
the lifecycle using evidence appropriate to the item and risk.

## Requirement quality

Every individual requirement must be:

- **necessary**: traces to a need or obligation and is essential;
- **appropriate**: belongs at its stated abstraction level without unnecessary
  implementation detail;
- **unambiguous**: has one defensible interpretation in the shared terminology;
- **complete**: states the subject, outcome, applicable conditions, and measurable
  bounds needed to understand it;
- **singular**: expresses one obligation;
- **feasible**: can be realized within known technical, cost, schedule, legal,
  ethical, resource, and risk constraints;
- **verifiable**: admits objective evidence with stated success criteria;
- **correct**: accurately represents its source and intended outcome; and
- **conforming**: follows the project's requirement syntax, attributes, units,
  and terminology.

The requirements set must be complete, consistent, feasible, comprehensible,
able to be validated, and correct. Assess both each statement and the set; good
individual statements can still omit behavior, conflict, or express the wrong
system.

## EARS syntax

Express every textual requirement using the Easy Approach to Requirements Syntax
(EARS). Select the pattern that matches the semantics:

```text
Ubiquitous:       The <system> shall <response>.
Event-driven:     When <trigger>, the <system> shall <response>.
State-driven:     While <state>, the <system> shall <response>.
Optional feature: Where <feature is included>, the <system> shall <response>.
Unwanted behavior: If <unwanted condition>, then the <system> shall <response>.
Complex:          While <state>, when <trigger>, the <system> shall <response>.
```

Combine patterns only when their conditions jointly govern one response. Keep
clauses in temporal order: optional feature or precondition, state, trigger,
system, response. Use `shall` for the obligation. Name the system element at the
correct abstraction level, and define triggers, states, features, responses,
units, and bounds precisely.

EARS constrains a requirement statement; it does not replace its identifier,
source, rationale, attributes, traceability, verification case, or the quality
assessment above. If an EARS response contains more than one obligation, split
it to preserve singularity. Do not force needs, rationale, design decisions,
tasks, or verification procedures into requirement syntax merely because they
are stored near requirements.

EARS pattern reference: [Easy Approach to Requirements Syntax](https://alistairmavin.com/ears/).

## Verification and validation coverage

Trace each requirement to one or more verification cases with an appropriate
method: inspection, analysis, demonstration, or test. State the level, conditions,
success criteria, required evidence, and responsible verification case. Use
multiple methods when one cannot provide adequate confidence. Validate the
requirements against needs and representative use before relying on downstream
verification alone.

Apply appropriate verification and validation to all authoritative information
and realized artifacts, not only requirements. This includes needs, assumptions,
models, analyses, architecture, interfaces, decisions, risks, source,
configuration, data, automation, documentation, integrations, releases,
operations, migrations, archives, and reuse claims. The method and independence
must be proportional to consequence, novelty, and uncertainty.
