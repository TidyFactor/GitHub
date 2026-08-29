# Workflow: manage-breaking-changes

One outcome: a verified breaking change lifecycle including deprecation notices, compatibility matrix, and migration guides.

## Steps

1. Load `references/memory/positioning-framework.md` and `references/rules/ci-rules.md`.
2. Evaluate proposed breaking changes against SemVer rules (requires `MAJOR` bump).
3. Generate compatibility matrix across supported runtime versions, OS, and dependencies.
4. Author comprehensive Migration Guide under `docs/migrations/vX-to-vY.md` with side-by-side code diffs.
5. Ensure `CHANGELOG.md` contains a dedicated `### Breaking Changes` section with linked migration guide.

## Validation checklist

- [ ] Major SemVer bump planned and documented in CHANGELOG.md
- [ ] Compatibility matrix updated across runtimes and frameworks
- [ ] Step-by-step migration guide authored with code examples
- [ ] Deprecation warning emitted in previous minor release
