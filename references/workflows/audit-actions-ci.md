# Workflow: audit-actions-ci

One outcome: a hardened, SHA-pinned GitHub Actions CI/CD workflow configuration.

## Steps

1. Inspect all files in `.github/workflows/*.yml`.
2. Check for security invariants (`references/rules/sec-rules.md`):
   - Replace mutable tags (`@v4`, `@main`) with full commit SHAs.
   - Enforce top-level `permissions: contents: read`.
3. Check for performance and resource rules (`references/rules/ci-rules.md`):
   - Add `concurrency` with `cancel-in-progress: true`.
   - Add explicit `timeout-minutes: 15` to each job.
   - Add native dependency caching (`cache: 'npm'`, `cache: 'pip'`).
4. Output diff in `PLAN` mode or write updated workflow files in `APPLY` mode.

## Validation checklist

- [ ] Every third-party action has a full 40-character commit SHA with version comment
- [ ] Top-level permissions block is present and locked to read-only baseline
- [ ] Concurrency block prevents redundant builds on pull requests
- [ ] Job timeouts are explicitly defined
