# Rust Way of Working

This directory contains process instructions for repositories whose primary
development language is Rust.

Agents should use `AGENT.md` when setting up or validating Rust repository
process files, engineering documentation, CI expectations, and verification
evidence.

## Human Responsibilities For AI-Assisted Work

AI-generated code, tests, documentation, and review comments should be treated
as proposals that require normal engineering verification. AI agents can speed
up discovery, implementation, refactoring, and review preparation, but they do
not replace the project owner, maintainer, or responsible reviewer.

Humans using AI agents for Rust development should decide:

- which data, repositories, credentials, prompts, and retrieved context are
  approved for the agent runtime;
- which tools, network access, filesystem access, dependency changes, CI
  permissions, and release actions an agent may use without additional review;
- which changes require human review, threat review, dependency audit, fuzzing,
  property tests, targeted negative tests, or other independent verification;
- whether AI-assisted changes must be disclosed in commits, pull requests,
  changelogs, release notes, or audit records;
- how conflicting findings from several agents are resolved before a change is
  accepted.

Do not approve AI-generated work solely because another agent reviewed it.
Require repeatable evidence that the change satisfies the requirement and does
not introduce unreviewed security, privacy, supply-chain, or operational risk.
