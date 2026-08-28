# Changelog

All notable changes to the `tidyfactor-github` skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-29

### Added
- Initial public release of `tidyfactor-github` (GitHub Platform Operations, Governance, Content, Experience & Intelligence Engine).
- 5-Layer Engine architecture: Operations, Governance, Content, Styling, and Ecosystem Intelligence.
- 3 Strict Execution Modes: `AUDIT` (read-only scorecard), `PLAN` (dry-run & gap analysis), and `APPLY` (safe execution with explicit confirmation gates).
- Contextual Decision Layer (CDL) with `/brief` command and `.tidyfactor/github-brief.md` cache.
- 17 specialized runtime commands and 17 single-outcome workflows with validation checklists.
- 4 Prioritized Rule Catalogs: Security (`sec-rules.md`), Governance (`gov-rules.md`), Content Anti-Slop (`content-rules.md`), and CI/CD (`ci-rules.md`).
- Repository and Organization Blueprints with JSON Schema validation (`audit-report.schema.json`, `blueprint.schema.json`, `permission-matrix.schema.json`).
- Deterministic native tooling: `tools/repo_audit.py`, `tools/org_audit.py`, `tools/readme_linter.py`, `tools/validate_skill.py`, and `tools/build-skill.js`.
