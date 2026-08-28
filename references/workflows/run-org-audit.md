# Workflow: run-org-audit

One outcome: a structured organization governance, team hierarchy, and permission audit report.

## Steps

1. Inspect organization configuration and metadata:
   - Check member count, outside collaborators, and 2FA enforcement status.
   - Inspect team hierarchy and repository access mappings.
   - Check organization `.github` repository for shared defaults.
2. Evaluate against Least Privilege invariants (`memory/permission-matrix.md`):
   - Flag members with direct individual repository access.
   - Flag teams with excessive Admin privileges.
   - Check organization-level Rulesets and base repository permissions.
3. Output the Organization Scorecard and Action Plan.

## Validation checklist

- [ ] Audit reports 2FA enforcement status across all members
- [ ] Direct individual repository permissions are flagged as anomalies
- [ ] Team hierarchy is mapped against functional responsibilities
- [ ] Safe recommendations provided without automated destructive member removals
