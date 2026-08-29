# Workflow: run-oss-audit

One outcome: a comprehensive Open Source Readiness Audit report evaluating the repository across 10 dimensions with a prioritized treatment plan.

## Steps

1. Load `references/memory/oss-readiness-rubric.md` and `references/rules/gov-rules.md`.
2. Inspect repository files: `README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `GOVERNANCE.md`, `.github/workflows/`, and issue forms.
3. Run `tools/oss_audit.py` to calculate score (0-100) across the 10 dimensions:
   - Project Identity, Documentation, Onboarding (CX), Good First Issues, Community, Governance, Sustainability, Security, Releases, Discoverability.
4. Generate diagnosis and treatment plan identifying top 3 bottlenecks (e.g. Missing `GOVERNANCE.md`, high setup friction, unpinned actions).
5. Output structured report following `schemas/oss-audit-report.schema.json`.

## Validation checklist

- [ ] All 10 evaluation dimensions scored objectively
- [ ] Overall score (0-100) and maturity tier calculated
- [ ] Top friction bottlenecks and treatment plan prioritized
- [ ] Report adheres to schema `schemas/oss-audit-report.schema.json`
