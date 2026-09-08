# Way of Working

This repository is the authoritative methodology for model-based development of
software-intensive systems by people and AI agents. It adapts a systems
engineering lifecycle to software without making a programming language or an
external project authoritative.

## Methodology layers

| Layer | Meaning |
| --- | --- |
| [`core/`](core/README.md) | Mandatory rules. Projects must not override them. |
| [`starter/`](starter/README.md) | Defaults that accelerate setup. Exploration and Concept may be tailored with recorded rationale. |
| [`project-definition/`](project-definition/README.md) | Decisions every adopting project must supply. They must not be inferred as approved facts. |

Stage-local instructions and skills live in [`stages/`](stages/README.md).
Language and product profiles may add realization rules, but cannot redefine the
core, stage authority, or lifecycle.

A pull request is one work package. Its commits complete ordered, role-scoped
process outcomes while leaving the repository consistent. Agents load only the
context and skills applicable to their assigned role and outcome; tollgates and
human authorities remain separate from repository merge mechanics.

## Lifecycle

1. Exploration
2. Concept
3. Development
4. Production and Transition
5. Utilization
6. Support and Evolution
7. Retirement

Stages may overlap, iterate, or apply to different versions and system elements.
An agent assesses tollgate maturity; only the project-defined human authority
decides whether to change stage.

## Using the methodology

- New project: complete the project definition, select starter content, then
  begin in the applicable stage.
- Existing project: use [`workflows/adopt-existing-project.md`](workflows/adopt-existing-project.md)
  to inventory evidence, reconstruct the system, and introduce missing artifacts
  incrementally.
- All persistent changes: use the fixed pull-request workflow in
  [`core/change-workflow.md`](core/change-workflow.md).
- Process learning: use [`workflows/methodology-retrospective.md`](workflows/methodology-retrospective.md)
  to improve the project locally and propose evidence-backed changes upstream.

Keep agent output crisp, structured, and condensed. Lead with decisions,
blockers, and outcomes; link to detailed evidence instead of repeating it.
