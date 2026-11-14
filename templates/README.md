# Use This Repository as a Template

1. Copy the shared `AGENTS.md`, `core/`, `skills/`, `knowledge/`, `workflows/`,
   `project-definition/`, `templates/`, and root `.gitignore`. Retain the source
   license notice and choose/document the adopting project's license explicitly.
2. Copy `engineering/` and/or `story/` only if selected. Keep their internal paths
   stable. Remove optional-domain links from indexes when omitting a domain, then
   check navigation. Do not leave broken routing to unselected content.
3. Replace root README with a short project purpose and navigation. Establish root
   context, a completed project definition, and human authorities. Use existing
   artifacts when adopting rather than creating duplicate knowledge.
4. Create root `AI-USAGE.md` from [this template](AI-USAGE.md). Do not copy WoW's
   authorship claims as claims about your project. Preserve provenance for reused
   methodology separately from new deliverables.
5. Keep general knowledge/skills at root and scoped equivalents with their owning
   system or narrative module. Decide shared versus separate work-type trees from
   actual dependencies. Do not force a directory per work type.
6. Validate one realistic task through intake, research, implementation, checking,
   cleanup, commit/push, and PR review. Human acceptance of workflow is explicit;
   copying template files does not confer approval.

Exclude `maintenance/` and WoW's `.github/ISSUE_TEMPLATE/methodology-improvement.yml`
from adopting projects. Remove the WoW-only maintenance routes from copied indexes
and agent instructions. Maintenance scripts/evidence and this repository's work
history are not project requirements. Do not copy `.git/`, `tmp/`, or machine-local
instructions. Templates contain placeholders, never approved project facts.

## Artifact templates

- [PR](pull-request.md)
- [Knowledge record](knowledge-record.md)
- [AI usage](AI-USAGE.md)
- [Retrospective](retrospective.md) and [methodology proposal](methodology-proposal.md)
- Engineering: [requirement](../engineering/templates/requirement.md) and
  [tollgate](../engineering/templates/tollgate.yaml), when that domain is selected.
