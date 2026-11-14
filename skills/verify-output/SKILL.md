---
name: verify-output
description: Verify and validate any output with evidence appropriate to its audience and risk, and reassess both passing coverage and failing check assumptions.
---

# Verify Output

Applies to author/checker roles in any stage. Read the requested outcome, affected
artifacts and dependencies, current checks, and required independence. Do not load
unrelated suites by default. Output evidence alongside the work package or in its
scoped knowledge; report `pass`, `fail`, `inconclusive`, `not-applicable`, or
`pending-human` with baseline, method, result, and limitations.

| Output | Verification | Validation |
| --- | --- | --- |
| Code/configuration/scripts | Relevant static checks, tests, compatibility/security/resource checks | Representative intended-use scenarios |
| Knowledge/requirements/design | Sources, consistency, traceability, assumptions, measurable claims | Adequacy for decisions and stakeholder needs |
| Skills/process/template | Links, syntax, authority, scope, no contradictory instructions | Walk realistic success, failure, and exception cases |
| Stories | Continuity, language, provenance, stated constraints | Intended reader experience; editorial review/playtest |
| Plans/prompts/communication | Fidelity, omissions, accurate status and links | Audience can identify outcome, decisions, and next step |
| Other output | Research suitable methods before relying on it | Define evidence of suitability and remaining uncertainty |

1. Define success from the request and upstream evidence, not from implementation.
   For an uncovered output type, research practices, devise suitable checks, and
   propose the method in the applicable skill for human acceptance.
2. Run checks appropriate to the changed baseline and affected dependencies.
   Preserve required reviewer independence. Self-review is not independent review.
3. On failure, examine the check's oracle, environment, and assumptions. If they
   remain valid, fix the output. If changed intent invalidates them, trace the reason,
   obtain any required approval, update checks, and rerun affected evidence.
4. On success, inspect what changed beyond the checks' design. Add cases for an
   isolated gap; redesign the method if its model, oracle, or environment no longer
   represents intended use. Then rerun affected checks. Do not report broad quality
   claims from a narrowly passing suite.
5. Review the affected chain holistically: intent, knowledge, result, assurance,
   documentation, provenance, and relevant operation/support obligations. Record
   unaffected/not-applicable areas briefly; do not manufacture checklist volume.
6. Check audience clarity, knowledge-change summary, skill approval status,
   binary authorization, and cleanup triggers. Remove expired temporary artifacts,
   retaining durable evidence. Confirm all commits were pushed before PR delivery.

Human suitability judgments or required approvals still pending must remain
visible. Passing automated checks cannot authorize goals, skills, release, risk,
or lifecycle transitions. Broaden tests only for a concrete coverage concern.
