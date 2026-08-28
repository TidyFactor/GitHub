# Command: repo

Runtime entry point for repository factory scaffolding, portfolio health analysis, and lifecycle tracking.

## Dispatch steps

1. Load `../workflows/scaffold-repository.md` — repository creation and baseline scaffolding workflow.
2. Load `../memory/maturity-model.md` — maturity levels.
3. Load `../../assets/blueprints/repository.blueprint.yml` — baseline repo structure.
4. If generating a new repository, scaffold all standard files (`README`, `LICENSE`, `CHANGELOG`, `.github/`).

## Do not

- Do not delete or archive repositories without explicit confirmation gate.
- Do not create empty folders without valid files inside them.
