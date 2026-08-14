---
id: WOW-CORE-AUTHORITY
classification: core
customization: prohibited
---

# Authority and Tollgates

Agents assess maturity and recommend `proceed`, `proceed-with-conditions`,
`remain`, `return`, `pause`, or `stop`. Only the human authority named in the
project definition approves a stage transition. Passing checks, merging a PR,
or completing a checklist does not imply approval.

Every tollgate assessment states its scope and baseline, maturity by criterion,
blocking and non-blocking findings, uncertainties, recommendation, rationale,
and the exact human decision required. Use `absent`, `initial`, `partial`,
`sufficient`, `strong`, or `not-applicable`; never hide a critical weakness in
an aggregate score.

After recording a tollgate assessment, run the methodology retrospective in
[`../workflows/methodology-retrospective.md`](../workflows/methodology-retrospective.md).
The retrospective does not authorize the stage transition and must not delay a
human decision when sufficient tollgate evidence already exists.

Ask a non-blocking question and continue independent work. Pause only when an
answer is required from a human and no useful authorized work remains. Valid
questions include stage authorization, materially different concept choices,
scope or intent, risk acceptance, conflicting stakeholder priorities, and
destructive transition or retirement actions.
