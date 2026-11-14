# Output Quality and Organization

Write for the audience and context. Be concise without losing meaning,
readability, evidence, or correctness. Use descriptive names and entry-point
indexes; keep one authoritative home and link rather than duplicate.

## Modules

Organize by directory, file, then sections. A module should have one purpose
expressible in one sentence. Minimize hard dependencies first, then softer
coupling; avoid fragmenting a coherent topic merely to make files small.

- General skills live in root `skills/`; scoped skills in `<scope>/skills/`.
- General knowledge lives in root `knowledge/`; scoped knowledge in
  `<scope>/knowledge/`. Source indexes and supporting decisions belong there.
- Requirements belong to their system directory, including the project root for
  the main system. Use `<system>/knowledge/requirements.md` or an indexed directory;
  system scope stops at directories, never functions.
- Code decomposes from directories to files, classes/interfaces where useful,
  then functions. Load language profiles only where applicable.
- For mixed work, share a module tree when artifacts serve one cohesive system;
  separate work-type trees when ownership and dependencies differ. Record the
  choice and cross-links in the project definition.

Aim for manageable files, often 200–2000 lines when content warrants it. This is
neither a minimum nor a hard maximum. Short indexes and skills beat padding.
Split at meaningful boundaries, considering context, memory, and navigation.

## Assurance

Every output type needs appropriate verification and/or validation: prose,
knowledge, skills, plans, scripts, implementation, and communication. Small
communication needs accuracy and clarity review, not a test harness. Use
[verify-output](../skills/verify-output/SKILL.md).

If no adequate method exists, research practices and propose an applicable skill
addition. Apply the justified check to the current task; persistent skill changes
still need human acceptance. A checklist alone is not assurance evidence.

After a pass, ask what new behavior/content the checks could not detect and
whether new cases suffice or assurance needs redesign. After a failure, check
the oracle and assumptions before changing the result or test. Never weaken an
expectation merely to obtain a pass.

## Temporary artifacts and binaries

Put unversioned scratch files, downloads, logs, caches, and temporary scripts in
root `tmp/`, excluded by root `.gitignore`. Configure tool temporary/cache paths
there where possible; do not default to `/tmp` or another possibly RAM-backed
filesystem. Check storage before large jobs. Document unavoidable tool exceptions.

A versioned short-lived artifact records owner, purpose, removal trigger, and
durable evidence to retain. Add cleanup to the relevant completion checklist or
consuming skill so it will be read at the right time. Remove it at the trigger;
retain necessary decisions and evidence separately.

Do not commit binaries without explicit human request or acknowledgement.
Generated images, archives, executables, and binary test fixtures are included.

## AI usage promise

Root `AI-USAGE.md` states the project's promise about authorship and AI involvement,
not a history of how content was produced. Use [the template](../templates/AI-USAGE.md)
to define scope, required authorship, and permitted assistance before producing
versioned output. Distinguish human-authored, collaborative, and AI-generated
content, including validation-only or grammar/spelling assistance where permitted.
Permission to use AI is not a promise that AI will author the content.

Before each commit, verify all added or changed output against the applicable
promise, including copied or moved content. Check both directions: AI-generated
content cannot satisfy a human-authored promise, and human-authored content cannot
satisfy an AI-generated promise. Human review alone does not change authorship.
Use contribution evidence and human confirmation where needed, not stylistic
guesses or an AI detector. Record evidence and verdicts in the PR or verification
record, separately from the promise.

A mismatch fails verification. Missing, ambiguous, or unsupported authorship is
inconclusive; resolve it before committing affected output. Correct the output or
seek an explicit human decision on the promise. Never silently relabel content or
rewrite the promise to make a check pass. Promise changes require human acceptance;
ordinary output changes verify against the existing promise without rewriting it.
