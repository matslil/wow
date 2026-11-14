# Template Update Rationale and Migration

Source: human request of 2026-11-14; this is a durable WoW decision record.

## Request interpretation

One deliverable: update the repository as a reusable agentic-project template.
The numbered goals and workflow steps are acceptance criteria, not separate
requested deliverables. One PR therefore contains the coherent migration.

## Improvements applied to the prompt's design

- Combine duplicate intake lists into one ordered procedure: classify, clarify,
  check goals, partition, plan, research. The empty input step 3 adds no requirement.
- Treat ambiguity as material when it changes intent, scope, evidence, or authority;
  otherwise allow stated routine choices to avoid unnecessary interruptions.
- Treat knowledge notification separately from approval of reserved decisions.
- Cover normative rules outside SKILL.md with the same human acceptance requirement;
  otherwise moving a rule between files could bypass skill governance.
- Keep brief files brief; 200–2000 lines is guidance, never padding or a hard limit.
- Bound research by evidence needed for the next decision; retain uncertainty.
- Validate craft exceptions against intended reader experience instead of scores.
- Distinguish standards alignment from an unverified conformance claim.

## Preserved and moved

| Previous home | New home | Reason |
| --- | --- | --- |
| core lifecycle, roles, authority, model, assurance | engineering/core/ | Retain detailed systems guidance without burdening other work |
| stages/, starter/, profiles/ | engineering/ equivalents | Scope engineering-only instructions |
| requirement and tollgate templates | engineering/templates/ | Keep engineering artifacts local |
| workflows/skills/run-methodology-retrospective/ | skills/run-methodology-retrospective/ | General skill discoverability |

The root core is now domain-neutral. Internal links and skill references are
updated; consumers with pinned old paths must update them deliberately. Select
only applicable domains, then verify their indexes after copying. No source,
external handbook, or adopting project's requirements were imported as authority.

## Review and limits

The PR must obtain human acceptance for the proposed processes. Story research
adds sourced advisory knowledge, applicability, counterexamples, and reuse limits.
INCOSE reference research confirms the handbook framework but is not a full
standards audit. No engineering release, stage transition, or new license is
being approved by this update.
