# Workflow: apply-blueprint

One outcome: a verified gap analysis report and automated alignment of a repository to standard Blueprints.

## Steps

1. Load `assets/blueprints/repository.blueprint.yml` or `assets/blueprints/organization.blueprint.yml`.
2. Compare target repository against Blueprint specifications:
   - Presence of baseline files (`README`, `LICENSE`, `SECURITY`, `CHANGELOG`, `CODEOWNERS`).
   - Ruleset configuration and branch protection.
   - GitHub Actions workflow invariants (SHA pinning, permissions, caching).
   - Issue Forms and PR templates.
3. In `PLAN` mode:
   - Output detailed Gap Analysis table listing Compliant, Missing, and Drifting items.
4. In `APPLY` mode:
   - Scaffold missing files and propose API updates with explicit confirmation gate for any destructive changes.

## Validation checklist

- [ ] Gap analysis itemizes all differences between target and blueprint
- [ ] Safe scaffolding applied without overwriting custom repository code
- [ ] Explicit confirmation gate required before applying destructive changes
