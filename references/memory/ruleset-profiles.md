# GitHub Ruleset Profiles & Governance Configurations

<!-- last-verified: 2026-08-29 -->

Standard GitHub Ruleset definitions for repository and organization levels.

---

## 1. Profile: `production-strict` (Production & Main Branches)

```json
{
  "name": "Production Main Protection",
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
        "required_approving_review_count": 1,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": true,
        "require_last_push_approval": true,
        "required_review_thread_resolution": true
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": true,
        "required_status_checks": [
          { "context": "test" },
          { "context": "lint" },
          { "context": "typecheck" }
        ]
      }
    },
    { "type": "required_linear_history" }
  ]
}
```

---

## 2. Profile: `public-oss-standard` (Public Open-Source)

```json
{
  "name": "Public OSS Standard Protection",
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
        "required_approving_review_count": 1,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "required_review_thread_resolution": true
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": true,
        "required_status_checks": [{ "context": "CI" }]
      }
    }
  ]
}
```

---

## 3. Profile: `tag-protection` (Release Tags `v*`)

```json
{
  "name": "Release Tag Protection",
  "target": "tag",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/tags/v*"],
      "exclude": []
    }
  },
  "rules": [
    { "type": "deletion" },
    { "type": "update" }
  ]
}
```

---

## 4. CLI Enforcement Command

Apply ruleset directly to any repository using the standard JSON payload:
```bash
gh api --method POST repos/{owner}/{repo}/rulesets --input ruleset_payload.json
```
