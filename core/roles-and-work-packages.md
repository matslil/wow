---
id: WOW-CORE-ROLES
classification: core
customization: prohibited
---

# Roles, Work Packages, and Context

A pull request is one work package. Before implementation, its description must
state the authorized objective, baseline, affected model scope, planned process
outcomes and commit order, assigned roles, completion criteria, and decisions
reserved for a human. Each commit completes one work-package stage: an internally
consistent process outcome in that package. A work-package stage is not a
lifecycle stage; lifecycle maturity is assessed separately at a tollgate.

An agent operates in exactly one engineering role for a process outcome. A role
is a constrained viewpoint, not an authority. Use these roles as applicable:

| Role | Accountable outcome | Boundary |
| --- | --- | --- |
| Work-package lead | Scope, sequence, coordination, and PR-level consistency | Does not approve stage, intent, release, retirement, or risk |
| Mission and stakeholder analyst | Mission, context, stakeholders, needs, intended use, and measures of effectiveness | Does not select architecture or approve inferred needs |
| Requirements engineer | Quality-controlled requirements and acceptance measures traced to approved needs | Does not implement or silently change stakeholder intent |
| System architect | Architecture, allocation, interfaces, behavior, trade studies, and technical budgets | Escalates changes to approved upstream intent |
| Realization engineer | Design and implementation of allocated system elements | Does not change requirements merely to make realization pass |
| Integration engineer | Integrated elements, interface evidence, compatibility, and reproducibility | Does not treat component tests as system verification |
| Verification engineer | Objective conformance cases, results, and evidence | Does not conceal failure by changing the item under verification |
| Validation engineer | Suitability evidence against needs and intended use | Does not equate conformance with suitability |
| Transition and configuration manager | Configuration status, baselines, release, deployment, migration, rollback, and provenance | Does not equate merge with baseline or release approval |
| Operations and sustainment engineer | Operational evidence, supportability, compatibility, and change triggers | Does not accept operational risk |
| Retirement engineer | Withdrawal, migration, archive, disposition, and residual-obligation evidence | Performs no unapproved destruction |
| Independent assurance reviewer | Independent findings on model, evidence, process, safety, security, and readiness | Does not approve its own authored outcome |

Risk, decision, measurement, information, configuration, safety, security, and
quality assurance are cross-cutting process skills. A project may assign
dedicated roles when consequence, scale, regulation, or required independence
justifies them. One person or agent platform may perform several roles, but each
agent invocation has one role. Use a fresh context for independent verification,
validation, or assurance when the required degree of independence demands it.

## Minimal context

Start a role invocation with a generated or manually assembled context package
containing only:

- work-package identifier, lifecycle stage, role, process outcome, baseline,
  permitted actions, and completion criteria;
- applicable project authority, approved tailoring, decisions, and constraints;
- allocated needs, requirements, elements, interfaces, risks, and evidence;
- the directly affected upstream and downstream trace neighborhood;
- relevant source, tests, tools, and explicit exclusions;
- unresolved items, escalation conditions, and required result format.

Do not load the complete model, every stage, unrelated subsystems, or all
available skills by default. Expand context only for a discovered dependency and
record why it became applicable. Record the baseline and context-package identity
with the process result so evidence can be invalidated when an input changes.

## Role-associated skills

Load one role-entry skill first. It defines purpose, permitted decisions,
forbidden actions, required inputs, output types, and escalation conditions.
Then load only the process, artifact, profile, and assurance skills required for
the assigned outcome. Detailed conditional material belongs in skill references
and is read only when its condition applies.

Every role or process skill must state:

- applicable roles, stages, and activation conditions;
- required inputs and the trace relations used to select context;
- allowed outputs and repository scope;
- required checks, evidence, and explicit verdict vocabulary;
- reserved human decisions and conditions for returning upstream.

Skills guide judgment; deterministic controls enforce syntax, identifiers,
permitted trace relations, coverage, cycles, stale evidence, configuration
status, and role/output compatibility. Use `pass`, `fail`, `inconclusive`,
`not-applicable`, or `pending-human` for check results. An agent must not change
its work-package objective or completion criteria merely to make its result pass.
