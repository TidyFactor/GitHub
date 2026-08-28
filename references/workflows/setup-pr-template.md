# Workflow: setup-pr-template

One outcome: a tailored Pull Request template written to `.github/PULL_REQUEST_TEMPLATE.md`.

## Steps

1. Inspect project type and framework from `.tidyfactor/github-brief.md` or repository files.
2. Structure sections:
   - Summary of Changes (`## What Changed?`).
   - Problem / Motivation (`## Why?`).
   - Architectural / Implementation Details (`## Implementation Notes`).
   - Testing & Verification Checklist (`## Verification Checklist`).
   - Breaking Changes declaration (`## Breaking Changes`).
3. Write file to `.github/PULL_REQUEST_TEMPLATE.md` (or `.github/pull_request_template.md`).

## Validation checklist

- [ ] PR template contains explicit verification checklist
- [ ] Breaking changes warning section included
- [ ] File contains zero generic marketing filler
