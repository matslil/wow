# Rust Development Process Instructions

These instructions apply to repositories whose primary development language is Rust.
They are written for agents that either set up a Rust repository process or validate
that an existing Rust repository still follows the intended way of working.

The process uses a simplified INCOSE-style systems engineering flow:

1. Define the need and operating context.
2. Allocate requirements to code, tests, documentation, and automation.
3. Design the solution with explicit interfaces and constraints.
4. Implement in small, reviewable increments.
5. Verify each requirement with repeatable evidence.
6. Validate that the delivered behavior still solves the original need.
7. Record decisions, risks, limitations, and release impact.

## Repository Baseline

A Rust repository should make the intended system visible from the root:

- `README.md` explains the project purpose, supported platforms, quick start,
  prerequisites, examples, and current limitations.
- `Cargo.toml` declares package or workspace metadata, supported Rust edition,
  `rust-version` when MSRV matters, features, dependencies, and license.
- `Cargo.lock` is committed for applications, tools, examples, CI-pinned
  workspaces, and any repository where reproducible validation matters.
- `LICENSE`, `CHANGELOG.md`, and release notes exist when the repository is
  published or consumed outside the immediate team.
- `.github/workflows` or equivalent CI validates formatting, linting, build,
  test, documentation, and supported platform matrix.
- `rustfmt.toml` is present only when the project intentionally differs from
  default formatting.
- `docs/`, `examples/`, `tests/`, and benchmark or fixture directories are added
  when they provide useful engineering evidence.

For multi-crate systems, prefer a Cargo workspace. A workspace lets common
commands run across members, shares one lockfile and target directory, and keeps
metadata, dependency overrides, profiles, and lint configuration centralized in
the root manifest. Use explicit `members`, `exclude`, and `default-members`
when the repository has generated crates, experiments, or examples that should
not always participate in default checks.

## Requirements

Represent requirements as plain, testable statements. Each requirement should
include:

- a stable identifier, such as `REQ-RUST-001`;
- the actor or system boundary;
- the required behavior or quality attribute;
- any platform, feature, performance, safety, or compatibility constraint;
- the verification method: inspection, analysis, test, demonstration, or review.

Keep requirements close to the repository in `docs/requirements.md` or an
equivalent process file. Avoid requirements that merely restate implementation
tasks. A useful Rust requirement can usually be verified by one or more of:

- `cargo check --workspace --all-targets`;
- `cargo test --workspace --all-targets`;
- `cargo test --workspace --doc`;
- feature matrix checks such as default features, `--no-default-features`, and
  `--all-features`;
- platform or external dependency checks in CI;
- examples that compile and run in documented configurations.

## Architecture And Design

Document architecture at the level needed to make reviews and future changes
safe. The design documentation should cover:

- crate boundaries and why each crate exists;
- public APIs, traits, data types, ownership model, and error model;
- feature flags and optional dependencies;
- unsafe code boundaries, invariants, and safety obligations;
- FFI, build scripts, generated bindings, or native library discovery;
- concurrency, async runtime choice, blocking behavior, and cancellation model;
- persistence, serialization formats, or wire protocols;
- performance-sensitive paths and benchmark expectations;
- compatibility promises, including MSRV and SemVer surface.

Use Rust API Guidelines for public APIs. In particular, validate naming,
conversion traits, common trait implementations, error types, examples,
`Send`/`Sync` expectations, `Debug` implementations, and future-proofing of
public structs and traits.

## Implementation Rules

Agents should prefer idiomatic Rust and the repository's existing style.

- Keep unsafe Rust rare, local, documented, and covered by tests. Every unsafe
  block or unsafe function must state the invariant it relies on.
- Prefer type-safe APIs over boolean flags, stringly typed modes, or unchecked
  integer states.
- Prefer `Result` with meaningful error types for recoverable failures.
- Do not use `unwrap`, `expect`, or panic in library code except where an
  invariant has already been proven and the reason is documented.
- Use feature flags deliberately. Default features are part of the public
  compatibility surface and are hard to remove without a SemVer break.
- Keep generated code reproducible. Document the generator, version, inputs,
  and command used to refresh it.
- Keep build scripts deterministic and clear about external tools, environment
  variables, and fallback behavior.
- Public crates should include crate-level docs, examples, and documented
  error, panic, and safety behavior.

## Verification

The default verification set for a Rust repository is:

```text
cargo fmt --all --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-targets
cargo test --workspace --doc
cargo build --workspace --all-targets
```

Adjust this set when the repository has platform-specific dependencies,
long-running integration tests, external services, MPI runtimes, GPUs, embedded
targets, or optional features that cannot all run everywhere. When a check is
skipped, document why and where it is covered instead.

For libraries, verify at least:

- unit tests near the implementation;
- integration tests under `tests/` for public behavior;
- doctests for examples in public docs;
- compile checks for examples;
- feature combinations that the project promises to support;
- SemVer impact for public API changes.

For applications and tools, also verify:

- command-line behavior and exit codes;
- configuration loading and defaults;
- error messages for common operator mistakes;
- upgrade and migration behavior when persistent state is used.

## CI Expectations

CI should provide repeatable evidence, not just compile success. A normal Rust
CI pipeline should include:

- stable toolchain validation and any promised beta, nightly, or MSRV checks;
- Linux, macOS, and Windows jobs when the project claims cross-platform support;
- dependency cache use that does not hide lockfile or feature problems;
- separate jobs for formatting, linting, tests, docs, and platform-specific
  integration checks when that makes failures easier to diagnose;
- `--locked` checks when reproducibility matters;
- artifact collection for generated docs, coverage, benchmark output, or test
  logs when useful for review.

## Review Checklist

Before approving a Rust change, verify:

- the change maps to a requirement, issue, or explicit user need;
- new or changed behavior has tests or a justified verification alternative;
- the public API remains idiomatic and compatible, or the breaking change is
  intentional and documented;
- feature flags, optional dependencies, and platform gates are tested;
- unsafe code and FFI boundaries have explicit invariants;
- errors are actionable and do not discard useful context;
- documentation, examples, and changelog entries are updated when users need
  to know about the change;
- CI covers the affected workspace members and targets.

## Pattern From `mpi-rs`

Use `mpi-rs` as a model for Rust repositories that bind to external systems or
native libraries:

- The repository is organized as a workspace-like multi-crate system with the
  root crate, an FFI/sys crate, a derive crate, examples, integration tests, and
  dedicated CI workflows.
- The README makes external requirements explicit: supported MPI
  implementations, tested versions, environment variables, native discovery
  mechanisms, and platform-specific setup.
- Build setup probes the native environment instead of assuming one layout.
  It supports `pkg-config`, compiler wrappers such as `mpicc`, and documented
  Windows variables for MS-MPI or Intel MPI.
- Low-level bindings are isolated behind generated FFI and a thin native shim
  where the external C API is underspecified.
- Optional features expose additional capabilities, such as derives or user
  operations, without forcing every user to compile every dependency.
- Examples demonstrate real usage with initialization, communication, and
  assertions rather than only toy syntax.
- CI separates general checks from workflows that require MPI-specific setup.

Apply this pattern whenever a Rust repository depends on native libraries,
generated bindings, distributed runtimes, or specialized platform tooling.
Document the discovery order, required tools, supported versions, and how an
agent can reproduce the CI environment locally.

## Agent Validation Procedure

When validating a foreign Rust repository:

1. Identify whether it is an application, library, workspace, FFI binding,
   embedded project, or mixed system.
2. Read the root manifest, workspace manifest, CI configuration, README,
   changelog, and process documentation.
3. Build a requirement-to-verification trace table from existing docs and tests.
4. Run or inspect the default Rust verification set.
5. Check feature flags, external requirements, generated code, and unsafe/FFI
   boundaries.
6. Compare public API and documentation against Rust API Guidelines.
7. Report gaps as process findings with concrete files, commands, and missing
   evidence.

If setting up a new Rust repository, create the smallest useful version of this
process first, then expand it as requirements, crates, platforms, and release
obligations become real.

## Reference Sources

- Rust API Guidelines: https://rust-lang.github.io/api-guidelines/checklist.html
- Cargo workspaces: https://doc.rust-lang.org/cargo/reference/workspaces.html
- Cargo features: https://doc.rust-lang.org/cargo/reference/features.html
- Cargo test: https://doc.rust-lang.org/cargo/commands/cargo-test.html
- Cargo clippy: https://doc.rust-lang.org/cargo/commands/cargo-clippy.html
- Cargo fmt: https://doc.rust-lang.org/cargo/commands/cargo-fmt.html
- mpi-rs repository: https://github.com/rsmpi/rsmpi
