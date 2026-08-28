# Command: issue

Runtime entry point for Issue Forms authoring, label taxonomy, and issue triage.

## Dispatch steps

1. Load `../workflows/setup-issue-forms.md` — issue form scaffolding workflow.
2. Load `../memory/issue-taxonomy.md` — label prefixes and schema definitions.
3. Generate structured `.github/ISSUE_TEMPLATE/*.yml` forms (bug report, feature request, config).

## Do not

- Do not use free-form unvalidated markdown templates when YAML forms are supported.
- Do not create un-prefixed, ambiguous labels.
