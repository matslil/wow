# Rust Profile Instructions

Apply these rules only while realizing or verifying Rust system elements.

- Declare the Rust edition, supported toolchain or MSRV, platforms, features,
  dependencies, licensing, and compatibility policy.
- Prefer workspaces for related crates and keep package boundaries aligned with
  documented responsibilities and interfaces.
- Keep unsafe code local, document its invariants, and verify those obligations.
- Define public API, ownership, concurrency, errors, persistence, protocols,
  generated code, build scripts, FFI, and platform assumptions where applicable.
- Keep builds and generated artifacts reproducible.
- Verify applicable feature and platform combinations.

Default checks, tailored only when the project records why a check is
inapplicable or covered elsewhere:

```text
cargo fmt --all --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-targets
cargo test --workspace --doc
cargo build --workspace --all-targets
```

Record the executed evidence in the PR. Do not use this profile to weaken core
commit validity, traceability, or stage tollgates.
