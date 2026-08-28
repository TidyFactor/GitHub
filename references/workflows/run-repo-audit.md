# Workflow: run-repo-audit

One outcome: a structured 9-dimension health report and scorecard for a single GitHub repository.

## Steps

1. Inspect repository root and `.github/` folder:
   - Check `README.md`, `LICENSE`, `CHANGELOG.md`.
   - Check `.github/workflows/`, `.github/ISSUE_TEMPLATE/`, `SECURITY.md`, `CODEOWNERS`.
2. Evaluate rules compliance against:
   - `references/rules/sec-rules.md` (SHA pinning, permissions, push protection).
   - `references/rules/gov-rules.md` (Branch protection, CODEOWNERS, linear history).
   - `references/rules/content-rules.md` (Anti-slop, badge density, above-the-fold clarity).
   - `references/rules/ci-rules.md` (Timeouts, caching, concurrency).
3. Compute 0-100 scores for the 9 dimensions defined in `memory/maturity-model.md`.
4. Output the standard audit scorecard with prioritized remediation items (CRITICAL -> LOW).

## Validation checklist

- [ ] Scorecard covers all 9 dimensions with a weighted total score (0-100)
- [ ] Maturity Level (0-6) is explicitly identified
- [ ] Remediation items are grouped strictly by priority (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`)
- [ ] No file modifications were made during audit
