# Workflow: configure-rulesets

One outcome: a verified GitHub Ruleset JSON configuration for default branches and release tags.

## Steps

1. Load `references/memory/ruleset-profiles.md` and `references/rules/gov-rules.md`.
2. Select target profile based on scope:
   - `production-strict` for production apps and critical services.
   - `public-oss-standard` for open-source community libraries.
   - `tag-protection` for immutable SemVer release tags.
3. Validate ruleset JSON parameters:
   - Force push blocked (`non_fast_forward`).
   - Branch deletion blocked (`deletion`).
   - Pull request required with approving review count.
   - Required status checks specified.
4. In `PLAN` mode, output the JSON profile; in `APPLY` mode, apply via `gh api` with user authorization.

## Validation checklist

- [ ] Ruleset JSON complies with GitHub REST API schema
- [ ] Direct push and force push are disabled for default branch
- [ ] Minimum 1 PR approval is required
- [ ] Explicit confirmation gate passed before remote API application
