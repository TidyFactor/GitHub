# Command: readme

Runtime entry point for the README Experience Engine and Anti-Slop content generation.

## Dispatch steps

1. Load `../workflows/craft-readme.md` — README authoring and polishing workflow.
2. Load `../memory/readme-architecture.md` — 8-stage reading progression.
3. Load `../rules/content-rules.md` — anti-slop rules and badge limits.
4. Output structured, scannable, developer-first `README.md` and optional `README.ar.md`.

## Do not

- Do not use marketing fluff, hype words, or exaggerated claims.
- Do not create badge walls exceeding 5 badges.
