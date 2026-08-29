# Workflow: setup-governance-model

One outcome: an authoritative, transparent `GOVERNANCE.md` establishing decision authorities, maintainer nomination paths, and team permissions.

## Steps

1. Load `references/memory/oss-governance-models.md` and `references/rules/gov-rules.md`.
2. Select target governance model:
   - `Benevolent Dictator` for founder-led early-stage tools.
   - `Core Team` for collaborative multi-maintainer libraries.
   - `Maintainer Council` for modular monorepos and ecosystems.
3. Define role matrices (Owner, Maintainer, Reviewer, Contributor) and map to GitHub Teams.
4. Scaffold `GOVERNANCE.md` using `assets/templates/GOVERNANCE.md`.
5. Define voting thresholds, maintainer nomination criteria, and dispute resolution paths.

## Validation checklist

- [ ] Decision-making authority and voting rules explicitly documented
- [ ] Maintainer onboarding and offboarding criteria defined
- [ ] Conflict escalation path established
- [ ] Code of Conduct incident handler team identified
