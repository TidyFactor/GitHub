# Command: gfi

Runtime entry point for Good First Issue (GFI) discovery, complexity scoping, and rewriting.

## Dispatch steps

1. Load `../workflows/triage-good-first-issues.md` — GFI triage and authoring workflow.
2. Run `tools/gfi_finder.py` to inspect open issues and evaluate complexity.
3. Check candidate issues against the 4 isolation criteria:
   - Scope limited to 1-3 files.
   - Zero architectural lock-in or deep refactoring.
   - Deterministic local test/verification command available.
   - Prerequisites clearly declared.
4. Output structured issue enhancement proposals with difficulty score and estimated effort.

## Do not

- Do not apply `good first issue` label to issues with ambiguous acceptance criteria or broad architecture scope.
