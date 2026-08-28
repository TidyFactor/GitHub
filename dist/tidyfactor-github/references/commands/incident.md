# Command: incident

Runtime entry point for production incident triage, regression analysis, rollback guidance, and postmortem generation.

## Dispatch steps

1. Load `../workflows/handle-incident.md` — incident response workflow.
2. Load `../memory/security-baseline.md` — severity classification.
3. Identify suspect commits, failing workflow runs, and recent PRs; output remediation diff and postmortem draft.

## Do not

- Do not perform destructive rollbacks without explicit confirmation gate.
- Do not omit root-cause analysis in postmortem documentation.
