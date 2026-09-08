# Agent Instructions

This repository is authoritative for its methodology. Do not derive normative
rules from external projects. Keep technology-specific guidance separate from
the core.

## Load only applicable context

1. Read `core/README.md` and the core documents it requires.
2. In an adopting project, read its project-definition manifest and tailoring record.
3. Identify the current lifecycle stage, role, and scope.
4. Read the role and work-package rules, then only that stage's `README.md`,
   tollgate, role-entry skill, and applicable process or artifact skills.
5. Read selected starter items and profiles only when applicable.

Precedence is: core, completed project definition, approved tailoring, selected
starter content, selected profiles, stage/role skill, task-specific direction.
A lower layer cannot weaken a higher one.

## Operate continuously

Deliver every persistent repository change through a pull request. Continue
with useful authorized work, including the next PR, unless a material question
requires a human answer and no independent work remains. A pending review,
failure, missing documentation, or difficult task is not by itself a reason to
pause.

Treat a pull request as one work package and each commit as one completed
role-scoped work-package stage. A work-package stage is a process outcome, not a
lifecycle stage; a merge is not approval. Operate in one role per process
outcome and load only its bounded context and applicable skills.

When a body of work requires a series of related pull requests, publish them as
a pull request stack with explicit dependencies, base branches, and merge order
so the human can review and merge the series efficiently. Create and manage the
stack with the `gh stack` extension. When using the GitHub CLI, ensure this
extension is installed before starting the stacked pull request workflow.

Agents recommend tollgate outcomes. Only the human authority named by the
project may approve a stage transition, risk acceptance, release, or retirement.

## Communicate concisely

Lead with the outcome or question. Then include only decisive evidence, required
human action, and the next step. Separate blockers from advice. Do not restate
the request, narrate routine tool use, reproduce long logs, or bury decisions in
background text. Put detail in repository artifacts and link to it.

Native agents updating this repository must finish through a non-default branch,
verified commits, a push, and a pull request. Report the PR URL or the blocker.
