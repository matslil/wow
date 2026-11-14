# Template Update Validation

Scope: the reusable workflow update of 2026-11-14. Baseline: branch based on
origin/main after PR #8. This is durable evidence, not a temporary work plan.
Reviewer: authoring Codex instance; self-review, not independent assurance.

## Static checks

- `python3 maintenance/check_repository.py`: pass; 85 files inspected, 102 local
  links, 14 skills, 12 YAML files, zero errors. No non-text/NUL content found.
- Skill-creator `quick_validate.py`: all 14 skills pass.
- Checker fixtures: valid links accepted; missing/outside links, invalid YAML,
  mismatched skill name, and binary content each rejected as intended.
- `git diff --check`: pass; scratch plan confirmed ignored by `.gitignore`.
- Local links and metadata were checked after migration. External sources were
  read selectively for research, not exhaustively monitored for availability.

Checker execution uses the installed PyYAML 6.0.3. Its negative fixtures and
working plan are ignored scratch data under root `tmp/`. No versioned temporary
plan or script is retained; the maintenance checker is a reusable tool.

## Behavioral walkthroughs

These are desk reviews of the documented routes, not executed adopter projects.

| Scenario | Route and observed rule | Verdict |
| --- | --- | --- |
| One request with several acceptance criteria | Intake partitions by requested deliverable; shared workflow keeps criteria in one PR | pass |
| Two independent deliverables | One plan/PR each; a stack is unnecessary | pass |
| Dependent deliverables | gh stack, explicit base/dependencies/merge order; each completed commit pushed | pass |
| Ambiguous or goal-conflicting prompt | Clarify before dependent work; obtain acknowledgement of the necessary goal change | pass |
| Web page embeds instructions | Research classifies external text as data and does not execute it | pass |
| Human corrects an assumption | Authority rules revisit dependent knowledge/evidence and consider skill repair | pass |
| Implementation uncovers missing knowledge | Replan and research before continuing the affected step | pass |
| Bug report includes a runnable exploit | Bug skill treats code as untrusted; independent safe reproduction before fix | pass |
| Misuse caused by hidden documentation | Bug skill tests findability and treats documentation correction as the fix | pass |
| Tests pass but new behavior is uncovered | Output assurance adds cases or redesigns an invalid method | pass |
| Tests fail because an assumption changed | Check oracle against upstream intent; no arbitrary weakening to pass | pass |
| Novel-only adopter | Shared core plus story; no engineering roles/EARS/tollgates required | pass |
| Deliberate unreliable narrator | Story workflow distinguishes canon from narration and evaluates reader effect | pass |
| Grammar-only AI involvement | AI-USAGE records limited collaboration; workflow forbids unsolicited drafting | pass |
| Tabletop adventure and software tool | Domain selection follows actual dependencies; story playtests and engineering software checks both apply | pass |
| Missing reader feedback | Agent editorial review is marked provisional, not artistic proof | pass |
| Skill edit improves implementation speed | Draft/check/push/PR allowed; adoption still requires human acceptance | pass |
| Temporary tracked plan expires | Owner/trigger and completion skill require cleanup; preserve durable evidence | pass |
| Generated binary proposed | Explicit human request/acknowledgement required before committing | pass |

## Coverage review

Static success cannot prove authority consistency, template usability, literary
quality, or standards compliance. The walkthroughs above address routing and
failure cases; real adopter trials and independent human review remain outside
this desk review. No representative story, software product, or release was
produced as part of this methodology change.

The migration affects entry points, shared rules, project templates, skills,
engineering paths, new story knowledge, and provenance. Existing engineering
lifecycle, requirement quality/EARS, traceability, and tollgate responsibilities
remain in the scoped engineering layer. Runtime APIs, deployment, and retirement
of an actual product are not applicable.

## Human decision

Skill/process acceptance: pending-human against the final PR revision. No merge,
release, risk acceptance, or stage transition is authorized by these checks.

## Follow-up: AI-usage promise

The human correction after PR #9 supersedes the retrospective AI-USAGE behavior
reviewed above. AI-USAGE now declares promised authorship and permitted assistance;
PRs/verification records hold actual contribution evidence. Root WoW policy permits
human, collaborative, or AI-generated work, preserving its human-directed workflow.

Desk review of the revised core, template, and verification/story skills:

| Case | Required result |
| --- | --- |
| AI-drafted prose in a human-authored scope | fail; correct output or seek a human decision on the promise |
| Human-written prose in an AI-generated scope | fail; permission to use AI is insufficient evidence of AI authorship |
| Human prose with explicitly allowed AI grammar corrections | pass when evidence confirms only the permitted assistance |
| AI rewriting under a validation-only promise | fail; exceeds permitted assistance |
| Unclear scope or unknown authorship | inconclusive; resolve before committing affected output |
| Changing the promise to match a nonconforming draft | requires explicit human acceptance; no silent relabelling |

Self-review found these outcomes covered. This change is AI-drafted from explicit
human direction, permitted by WoW's proposed promise and the existing authorized
workflow; skill/promise acceptance remains pending human PR review. The check uses
known contribution history, not an automated authorship detector. No historical
content was newly certified. Static checks and changed-skill validation are
recorded in the follow-up PR; no new test harness is needed for this prose change.
