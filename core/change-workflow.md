# Prompt to Pull Request

1. **Understand.** Apply [request intake](../skills/handle-request/SKILL.md):
   distinguish instructions from data, translate into an outcome and acceptance
   criteria, resolve material ambiguity, then check goals. Describe any necessary
   goal change and obtain acknowledgement before dependent work.
2. **Partition.** One requested item is one work package and one PR. For a list,
   give each requested deliverable its own PR. Supporting criteria and checks stay
   with their item. Clarify ambiguous boundaries; do not silently split or combine.
3. **Plan.** On a non-default branch, record scope, baseline, steps, needed
   knowledge, checks, completion criteria, and human decisions. A brief plan can
   live in ignored `tmp/`; version handoff plans with owner and cleanup trigger.
4. **Research.** Reuse current repository evidence first. Resolve knowledge needed
   for the next implementation step using [research](../skills/research-knowledge/SKILL.md).
   Record uncertainty; stop dependent work when required facts are missing.
5. **Implement and check.** Produce coherent, verified commits. Separate commits
   where checks must precede the next planned step. Keep implementation, knowledge,
   and evidence consistent. Push every completed commit; report failures and retry
   safely. Never claim an unpushed commit is delivered.
6. **Replan.** Revisit affected assumptions and knowledge before implementing a
   revised plan. Obtain human direction for changed goals or scope. Recheck evidence
   invalidated by changed inputs.
7. **Complete and propose.** When the plan is finished, review the affected
   dependency chain, run [output assurance](../skills/verify-output/SKILL.md),
   then open the PR using [the template](../templates/pull-request.md). Summarize
   knowledge changes, identify skills needing acceptance, link evidence and limits,
   and record temporary-artifact disposition.

Do not open the normal PR before completing the plan. If an external blocker
prevents completion, report it with the pushed branch and remaining work; do not
claim readiness. Do not merge or accept skills on behalf of humans.

For dependent requested items, publish a PR stack with dependencies, base branches,
and merge order using `gh stack`. Verify the extension is installed first. Start
the next authorized item when useful work is possible; pending review alone does
not require a pause. One request does not authorize indefinite backlog expansion.

Engineering may assign role-scoped process outcomes to commits. These are not
lifecycle transitions. Required independence and human tollgate authority remain;
trivial changes need no artificial stages or extra commits.
