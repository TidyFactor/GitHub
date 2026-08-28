# Command: ruleset

Runtime entry point for GitHub Rulesets and branch protection governance.

## Dispatch steps

1. Load `../workflows/configure-rulesets.md` — ruleset authoring and enforcement workflow.
2. Load `../memory/ruleset-profiles.md` — standard JSON ruleset profiles.
3. Load `../rules/gov-rules.md` — governance invariants.
4. Output or apply the corresponding JSON ruleset definition for default branches and tags.

## Do not

- Do not leave default production branches without force-push and deletion protection.
- Do not disable existing rulesets in `APPLY` mode without explicit confirmation gate.
