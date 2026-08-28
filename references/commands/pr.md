# Command: pr

Runtime entry point for Pull Request templates, CODEOWNERS mapping, and review workflows.

## Dispatch steps

1. Load `../workflows/setup-pr-template.md` — PR template generator workflow.
2. Load `../memory/permission-matrix.md` — team routing for CODEOWNERS.
3. Load `../rules/gov-rules.md` — review requirements and linear history.
4. Scaffold `.github/PULL_REQUEST_TEMPLATE.md` tailored to project stack.

## Do not

- Do not use generic one-line PR templates.
- Do not leave sensitive infrastructure or database paths without designated CODEOWNERS.
