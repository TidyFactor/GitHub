# Workflow: triage-good-first-issues

One outcome: a curated, high-clarity backlog of `good first issue` candidates with difficulty scores, required skills, and explicit file pointers.

## Steps

1. Load `references/memory/cx-framework.md` and `references/rules/content-rules.md`.
2. Inspect open issues via `tools/gfi_finder.py` or `gh issue list`.
3. Filter issues against the 4 qualification criteria:
   - File scope: 1 to 3 files modified.
   - Architectural isolation: No state machines, public API redesigns, or database schema migrations.
   - Verification clarity: Step-by-step reproduction and verification steps available.
   - Skills declared: Target languages (e.g. TypeScript, Python) and estimated effort (1-3 hours).
4. In `PLAN` mode, output rewritten issue drafts with difficulty tags; in `APPLY` mode, update issue body and apply `good first issue` label via `gh issue edit`.

## Validation checklist

- [ ] All selected issues have isolated file scope (≤ 3 files)
- [ ] Required skills and estimated effort explicitly stated
- [ ] Verification and local testing commands provided in issue body
- [ ] Label `good first issue` applied with user confirmation
