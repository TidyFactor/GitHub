# Command: release

Runtime entry point for SemVer release automation, tags, assets, and CHANGELOG synchronization.

## Dispatch steps

1. Load `../workflows/automate-release.md` — release execution workflow.
2. Load `../memory/maturity-model.md` — release criteria.
3. Validate atomic version synchronization across `package.json`, `.tidyfactor`, `brand.json`, and `CHANGELOG.md`.

## Do not

- Do not tag or publish releases with unrecorded changes in `CHANGELOG.md`.
- Do not make breaking changes on minor or patch version bumps.
