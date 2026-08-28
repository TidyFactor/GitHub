# Command: community

Runtime entry point for community health files, open-source launch readiness, and maintainer workflows.

## Dispatch steps

1. Load `../workflows/setup-community-health.md` — community files scaffolding workflow.
2. Load `../memory/maturity-model.md` — maturity requirements for public projects.
3. Scaffold `.github/CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, and `FUNDING.yml`.

## Do not

- Do not leave empty placeholder sections in contribution guidelines.
- Do not duplicate org-level community defaults into individual repos when org `.github` is present.
