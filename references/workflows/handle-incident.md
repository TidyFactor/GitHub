# Workflow: handle-incident

One outcome: production incident triage, regression commit isolation, rollback action plan, and postmortem documentation.

## Steps

1. Collect failure indicators:
   - Failing GitHub Actions workflow runs or failed deployments.
   - Recent merged pull requests and commits on default branch.
2. Isolate suspect regression:
   - Run `git log -n 10 --oneline` and `git diff` against previous stable tag.
   - Map affected files to CODEOWNERS.
3. Formulate immediate remediation:
   - Prepare hotfix branch (`hotfix/*`) or revert PR (`git revert <sha>`).
4. Generate Postmortem Document under `docs/incidents/YYYY-MM-DD-<incident-title>.md`:
   - Incident Summary & Impact Duration.
   - Root Cause Analysis (5 Whys).
   - Resolution & Preventative Action Items.

## Validation checklist

- [ ] Suspect commit or regression diff explicitly identified
- [ ] Safe revert PR prepared without destructive force push to main
- [ ] Postmortem document includes root cause and preventative actions
