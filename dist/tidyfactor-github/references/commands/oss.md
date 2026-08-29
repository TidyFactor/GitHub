# Command: oss

Runtime entry point for Open Source Readiness Audits, Launch Checklists, and Project Diagnostics (`oss-doctor`).

## Dispatch steps

1. Load `../workflows/run-oss-audit.md` — comprehensive 10-axis readiness audit.
2. Load `../memory/oss-readiness-rubric.md` — scoring dimensions and evaluation rubric.
3. Load `../memory/positioning-framework.md` — archetype and boundary rules.
4. Execute `tools/oss_audit.py` to calculate the 10-axis readiness score and generate diagnostic treatment.

## Modes

- `/oss audit`: Run 10-axis readiness inspection and output the maturity scorecard.
- `/oss launch`: Execute pre-launch verification checklist across all 10 dimensions.
- `/oss doctor`: Perform in-depth project diagnosis and generate prioritized treatment backlog.

## Do not

- Do not evaluate personal contributor performance; focus strictly on repository artifacts, governance, and sustainability.
- Do not apply structural mutations in `AUDIT` mode.
