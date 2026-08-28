# Command: org

Runtime entry point for GitHub Organization architecture, team hierarchies, and permission audits.

## Dispatch steps

1. Load `../workflows/setup-org-hierarchy.md` — organization team and permission configuration workflow.
2. Load `../memory/permission-matrix.md` — the least privilege model and team roles.
3. Load `../rules/gov-rules.md` — governance invariants.
4. Execute audit of existing teams, members, and outside collaborators; output permission matrix and recommendations.

## Do not

- Do not assign individual members direct repository admin rights.
- Do not execute destructive membership removals without explicit confirmation gate in `APPLY` mode.
