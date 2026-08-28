# Workflow: craft-readme

One outcome: a polished, scannable, developer-first `README.md` (and optional `README.ar.md`) complying with Anti-Slop invariants.

## Steps

1. Load `references/memory/readme-architecture.md` and `references/rules/content-rules.md`.
2. Extract project capabilities, architecture, and installation commands from source code.
3. Structure the document:
   - Header with title, one-line positioning, and max 5 badges.
   - 3-command Quick Start block.
   - Architecture & Core Capabilities table.
   - Usage examples and configuration options.
   - Testing, Governance, and License sections.
4. Pass content through the Anti-Slop filter (`tools/readme_linter.py`) to eliminate buzzwords.
5. If bilingual mode is active, generate parallel `README.ar.md` with RTL support.

## Validation checklist

- [ ] README has $\le 5$ curated badges
- [ ] First code block appears above the fold (within first 30 lines)
- [ ] Passes anti-slop check with zero banned marketing phrases
- [ ] If `README.ar.md` exists, contains `<div align="center" dir="rtl">` wrapper
