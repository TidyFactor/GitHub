# Command: action

Runtime entry point for GitHub Actions CI/CD workflows, supply chain auditing, and SHA pinning.

## Dispatch steps

1. Load `../workflows/audit-actions-ci.md` — workflow audit and hardening workflow.
2. Load `../rules/ci-rules.md` — caching, timeouts, and concurrency rules.
3. Load `../rules/sec-rules.md` — SHA pinning and top-level permissions invariants.
4. Audit existing `.github/workflows/*.yml` or scaffold optimized CI/CD workflows.

## Do not

- Do not emit workflows without `permissions: contents: read` minimum baseline.
- Do not use mutable tags (`@v4`, `@main`) for third-party actions.
