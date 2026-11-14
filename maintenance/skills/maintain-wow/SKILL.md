---
name: maintain-wow
description: Maintain this WoW methodology repository, separating reusable template rules from WoW-only records and validating adoption paths. Do not apply to adopting projects.
---

# Maintain WoW

Role: methodology maintainer; activity: evolution of repository content. Read
[the local definition](../../knowledge/project.md), shared core, and only affected
domain guidance. Root project-definition files are templates, not approved WoW facts.

1. Plan the requested item and research gaps; preserve useful existing content.
2. Put reusable rules in shared/scoped skills and process documents, reusable
   evidence in scoped knowledge, and WoW-specific facts under maintenance.
3. Treat normative changes as skill proposals requiring human review, even when
   their files are named README or templates. Never self-accept the proposal.
4. Run `python3 maintenance/check_repository.py` (Python 3.9+ and PyYAML).
   Validate representative adopter/maintainer scenarios as well.
   Check a story-only adopter does not need engineering context; inspect security,
   goal-conflict, failed-check, and temporary-cleanup paths. Run any changed scripts.
5. Record durable results and limits in maintenance knowledge. Remove versioned
   temporary plans/scripts when their completion trigger occurs, after retaining
   evidence. Scratch work stays in ignored root tmp/.
6. Complete verified commits on a non-default branch, push each, then open the PR.
   Report its URL and required human acceptance. No automatic merge or release.

Output scope: affected methodology and maintenance artifacts. Use `pass`, `fail`,
`inconclusive`, `not-applicable`, or `pending-human`. Escalate unclear goals or
external authority; continue independent authorized work. Self-review is not
independent assurance and must not be represented as such.
