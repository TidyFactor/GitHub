# Workflow: setup-org-hierarchy

One outcome: a verified team hierarchy and permission mapping configuration for a GitHub Organization.

## Steps

1. Load `references/memory/permission-matrix.md`.
2. Define core functional teams:
   - `@engineering` (with child teams: `@frontend`, `@backend`, `@platform-core`)
   - `@devops-infra`
   - `@security-leads`
   - `@documentation`
   - `@maintainers-triage`
3. Map repository access according to the Least Privilege matrix.
4. Output proposed `gh api` commands or Terraform/Blueprint configuration for review.

## Validation checklist

- [ ] Every repository has at least one designated owning team
- [ ] No individual user is assigned direct admin access
- [ ] Nested team structure reflects functional domain boundaries
- [ ] Confirmation gate required before executing team permission mutations
