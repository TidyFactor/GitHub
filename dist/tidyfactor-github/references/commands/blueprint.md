# Command: blueprint

Runtime entry point for repository and organization Blueprint alignment and gap analysis.

## Dispatch steps

1. Load `../workflows/apply-blueprint.md` — blueprint gap analysis and alignment workflow.
2. Load `../memory/decision-points.md` — decision baselines.
3. Compare target repository or organization with `assets/blueprints/*.blueprint.yml`.
4. In `PLAN` mode, output the detailed Gap Analysis and diffs; in `APPLY` mode, apply missing configurations safely.

## Do not

- Do not apply destructive modifications without explicit confirmation gate.
- Do not override custom repository exceptions documented in memory.
