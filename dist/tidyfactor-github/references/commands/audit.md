# Command: audit

Runtime entry point for 9-dimensional repository and organization health audits.

## Dispatch steps

1. Determine target scope: Repository level or Organization level.
2. If repository scope, load `../workflows/run-repo-audit.md` + `../memory/maturity-model.md` + `../rules/sec-rules.md` + `../rules/gov-rules.md`.
3. If organization scope, load `../workflows/run-org-audit.md` + `../memory/permission-matrix.md` + `../memory/maturity-model.md`.
4. Operate strictly in `AUDIT` mode (read-only): output the 9-dimensional scorecard and prioritized remediation items.

## Do not

- Do not modify files or make mutations during audit execution.
- Do not hide critical security violations behind generic warnings.
