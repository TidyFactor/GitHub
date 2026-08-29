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

### Direct GitHub CLI Automation

To apply the ruleset directly to a remote repository:
```bash
gh api --method POST repos/{owner}/{repo}/rulesets --input <(cat << 'EOF'
{
  "name": "Main Branch Protection",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["~DEFAULT_BRANCH"],
      "exclude": []
    }
  },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": true
      }
    }
  ]
}
EOF
)
```

## Validation checklist

- [ ] Ruleset JSON complies with GitHub REST API schema
- [ ] Direct push and force push are disabled for default branch
- [ ] Pull request and thread resolution are enforced
- [ ] Explicit confirmation gate passed before remote API application

