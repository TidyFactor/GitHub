# Contextual Decision Layer (CDL): Decision Points & Brief Schema

<!-- last-verified: 2026-08-29 -->

Protocol for arbitrating repository baselines during `/brief` and reading `.tidyfactor/github-brief.md` cache.

---

## 1. Discovery Decision Points

| Parameter | Options | Default Fallback | Impact |
|---|---|---|---|
| `project_type` | `library`, `saas-app`, `cli-tool`, `monorepo`, `docs-portal`, `micro-module` | `library` | Scaffolding structure, PR workflow, CI matrix |
| `scope_tier` | `personal-public`, `personal-private`, `org-public-oss`, `org-private-enterprise` | `org-public-oss` | Ruleset strictness, CODEOWNERS, 2FA enforcement |
| `governance_level` | `lenient` (1 dev), `standard` (team 3-10), `strict` (enterprise 10+) | `standard` | Approvals count, linear history, status checks |
| `primary_language` | `typescript`, `python`, `php`, `go`, `rust`, `polyglot` | `typescript` | CI actions, linters, dependency caching |
| `bilingual_mode` | `en-only`, `bilingual-ar-en`, `ar-first` | `bilingual-ar-en` | Generation of `README.ar.md`, issue forms localization |

---

## 2. Brief Cache Schema (`.tidyfactor/github-brief.md`)

```markdown
# TidyFactor GitHub Baseline Brief

- **Project Type**: library
- **Scope Tier**: org-public-oss
- **Governance Level**: standard
- **Primary Language**: typescript
- **Bilingual Mode**: bilingual-ar-en
- **Default Branch**: main
- **CI Runner**: ubuntu-latest
- **Signed Commits Required**: false
- **Min PR Approvals**: 1
- **Last Verified**: 2026-08-29
```

---

## 3. Downstream Execution Invariant

Any downstream command (`/audit`, `/ruleset`, `/action`, `/readme`, `/pr`, `/issue`) must first check if `.tidyfactor/github-brief.md` exists. If present, load its settings silently and execute without asking repetitive questions.
