# Maintaining WoW — Not Template Content

This directory applies only to this methodology repository. Exclude it when
adopting the template; also exclude WoW's methodology issue template in `.github/`.
Shared workflows still apply here. Because the deliverable is itself a workflow,
changes to core, skills, templates, and normative domain guidance need human review.

- [Project definition](knowledge/project.md)
- [Migration and rationale](knowledge/template-update.md)
- [Validation evidence](knowledge/validation.md)
- [Maintenance skill](skills/maintain-wow/SKILL.md)

Use root `tmp/` for working plans and scratch scripts. This directory holds durable
rationale and assurance evidence, not completed temporary plans. The root
project-definition files are blank adopting-project templates, not WoW's manifest.

Run `python3 maintenance/check_repository.py` from root with Python 3.9+ and
PyYAML installed. It checks inline local Markdown link targets, YAML/frontmatter,
skill names/descriptions, and UTF-8/NUL content. It excludes `.git/`, `tmp/`, and
Python caches. It does not check web availability, anchors, or policy semantics;
use scenario review for those limits. This checker is WoW-only maintenance tooling.
