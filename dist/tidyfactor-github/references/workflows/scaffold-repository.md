# Workflow: scaffold-repository

One outcome: a completely initialized and governed repository skeleton ready for development.

## Steps

1. Load `references/memory/decision-points.md` and read `.tidyfactor/github-brief.md` (or run discovery).
2. Generate baseline root files:
   - `README.md` (and `README.ar.md` if bilingual mode enabled).
   - `LICENSE` (Apache-2.0, MIT, or proprietary).
   - `CHANGELOG.md` (Keep a Changelog v1.0.0 format).
   - `.gitignore` tailored to primary stack.
3. Scaffold `.github/` folder:
   - `.github/workflows/ci.yml` (with SHA-pinned actions and `permissions: contents: read`).
   - `.github/ISSUE_TEMPLATE/` (YAML Issue Forms).
   - `.github/PULL_REQUEST_TEMPLATE.md`.
   - `.github/CODEOWNERS`.
   - `.github/SECURITY.md` and `.github/CONTRIBUTING.md`.

## Validation checklist

- [ ] All standard root files exist and contain non-empty content
- [ ] CI workflow has top-level `permissions: contents: read`
- [ ] No empty directories created
- [ ] Version and metadata synchronized across files
