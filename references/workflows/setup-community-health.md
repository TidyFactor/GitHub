# Workflow: setup-community-health

One outcome: verified community health files created in `.github/` or repository root.

## Steps

1. Check if organization `.github` defaults already provide community files.
2. If repo-level overrides are needed or this is a standalone repo:
   - Scaffold `.github/CONTRIBUTING.md` with development setup, branching, and PR workflow.
   - Scaffold `.github/CODE_OF_CONDUCT.md` (Contributor Covenant v2.1).
   - Scaffold `.github/SUPPORT.md` directing to Discussions or documentation.
   - Optionally scaffold `.github/FUNDING.yml`.

## Validation checklist

- [ ] `CONTRIBUTING.md` contains reproducible local build and test commands
- [ ] `CODE_OF_CONDUCT.md` has maintainer contact email specified
- [ ] `SUPPORT.md` lists active support channels
