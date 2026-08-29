# Workflow: optimize-cx-onboarding

One outcome: an optimized Contributor Experience (CX) reducing first-time contributor setup time to under 30 minutes.

## Steps

1. Load `references/memory/cx-framework.md` and `references/rules/content-rules.md`.
2. Audit local development setup steps from `README.md` and `CONTRIBUTING.md`.
3. Check for the 4 friction points:
   - Missing prerequisites or implicit dependencies.
   - Broken setup commands or outdated package versions.
   - Missing `.env.example` file.
   - Inability to run tests locally with a single command.
4. Scaffold or refine `CONTRIBUTING.md` and `assets/templates/CONTRIBUTORS.md`.
5. Document the 6-tier Contributor Ladder (`Observer` → `Core Maintainer`).

## Validation checklist

- [ ] Local setup steps execute deterministically in < 30 minutes
- [ ] Single test command declared (e.g. `npm test` or `python -m pytest`)
- [ ] CONTRIBUTING.md contains clear branch, commit, and PR conventions
- [ ] Contributor recognition mechanism defined in README or CONTRIBUTORS.md
