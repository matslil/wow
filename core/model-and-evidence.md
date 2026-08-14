---
id: WOW-CORE-MODEL
classification: core
customization: prohibited
---

# Model and Evidence

The project maintains an authoritative system model covering the system of
interest, context, stakeholders, needs, requirements, structure, behavior,
interfaces, analysis, verification, operation, and lifecycle disposition as
applicable. SysML is the default starter representation; equivalent structured,
version-controlled representations are allowed when declared by the project.

Model elements have stable identifiers. Trace at least:

```text
need -> requirement -> realizing element -> verification -> result
decision -> affected model baseline
risk -> mitigation -> evidence
operational observation -> change need
retired element -> archive, reuse, recycle, or disposal disposition
```

Trace verification cases to their method, conditions, success criteria, result,
and evidence. Trace validation to the upstream need and intended-use scenario.
Absence of a trace is a gap; a trace without adequate evidence is not closure.

Classify knowledge as `explicit`, `evidenced`, `inferred`, `unknown`, or
`conflicting`. An inference is never silently promoted to an approved need,
requirement, or decision. Generated views must not compete with the authoritative
model.
