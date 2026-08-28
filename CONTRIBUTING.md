# Contributing to TidyFactor GitHub

Thank you for contributing to the `tidyfactor-github` ecosystem.

## Development Workflow

1. Clone repository and inspect single source of truth in `SKILL.md` and `references/`.
2. Run validation script:
   ```bash
   python tools/validate_skill.py
   ```
3. Run README linter:
   ```bash
   python tools/readme_linter.py
   ```
4. Build distribution bundle:
   ```bash
   node tools/build-skill.js
   ```
5. Submit PR with detailed description and tests.
