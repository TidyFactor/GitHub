# Workflow: setup-issue-forms

One outcome: production YAML Issue Forms scaffolding in `.github/ISSUE_TEMPLATE/`.

## Steps

1. Load `references/memory/issue-taxonomy.md`.
2. Create `.github/ISSUE_TEMPLATE/` directory.
3. Write `bug_report.yml` with:
   - Reproduction steps (textarea, required).
   - Expected vs actual behavior.
   - Environment / version dropdowns.
4. Write `feature_request.yml` with problem statement and proposed solution.
5. Write `config.yml` disabling blank issues and directing questions to Discussions or Support.

## Validation checklist

- [ ] All issue forms are valid YAML (`.yml`) files
- [ ] Required fields (`validations: required: true`) are set on critical reproduction inputs
- [ ] `config.yml` contains `blank_issues_enabled: false`
- [ ] Issue forms match the repository's primary language and archetype
