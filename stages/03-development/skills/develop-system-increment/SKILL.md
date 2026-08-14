---
name: develop-system-increment
description: Define, implement, integrate, verify, and validate a traced software system increment through coherent pull requests. Use for all changes in the Development stage.
---

# Develop a System Increment

Read the core, project definition, this stage's `README.md`, and selected
profiles.

1. Select one authorized engineering outcome and its traced needs, requirements,
   risks, and decisions.
2. Assess affected requirements individually and as a set using
   `core/assurance.md`; express each textual requirement using the applicable
   EARS pattern and define appropriate verification and validation evidence.
3. Zig-zag between needs, requirements, architecture, behavior, interfaces,
   analysis, realization, integration, verification, and validation. Propagate a
   later insight back to the earliest affected item, then update and re-check its
   downstream relations.
4. Implement in a coherent PR. Use multiple commits for a larger outcome; make
   every commit internally consistent and pass its applicable checks.
5. Integrate, verify conformance, validate intended use, and record evidence for
   requirements, information, implementation, and other affected artifacts.
6. For a larger change, review the entire affected engineering chain for
   consistency and record the coverage in the PR.
7. Update model relations, risks, decisions, limitations, and follow-on work.
8. Complete the PR, then immediately select the next unblocked outcome.
9. Assess the Development tollgate when its scope is mature.

Do not pause for a pending review, failed check, missing document, or difficult
task. Pause only when a human answer is required and no independent work remains.
Only the designated human authorizes transition.
