# Command: branch

Runtime entry point for branch strategy selection, naming conventions, and lifecycle flow.

## Dispatch steps

1. Load `../workflows/configure-rulesets.md` — branch protection setup.
2. Load `../memory/branch-strategies.md` — Trunk-Based, GitHub Flow, and naming taxonomy.
3. Recommend or enforce the appropriate branch strategy for the repository's maturity level.

## Do not

- Do not recommend complex GitFlow models for lightweight libraries or single-maintainer apps.
- Do not force push to remote branches without explicit confirmation.
