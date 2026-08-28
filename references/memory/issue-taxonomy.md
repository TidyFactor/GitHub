# Issue Taxonomy, Standard Labels & Issue Forms Schema

<!-- last-verified: 2026-08-29 -->

Structured classification system for GitHub issues and pull requests.

---

## 1. Structured Label Taxonomy (`prefix:name`)

```text
type:bug              # Confirmed software defect or regression
type:feature          # New capability, command, or workflow
type:refactor         # Code cleanup with zero functional change
type:docs             # Documentation, README, or translation update
type:security         # Vulnerability patch or security hardening
type:perf             # Performance optimization and bundle reduction

area:core             # Platform core or kernel abstractions
area:governance       # Rulesets, permissions, or CODEOWNERS
area:ci-cd            # GitHub Actions, workflows, or deployments
area:ui-styling       # Design tokens, badges, or visual layouts

priority:p0-critical  # Production outage / security vulnerability (SLA: 24h)
priority:p1-high      # Major feature defect / blocking workflow (SLA: 7d)
priority:p2-medium    # Standard defect or planned improvement
priority:p3-low       # Minor aesthetic polish or backlog item

status:triage         # Awaiting initial maintainer review
status:blocked        # Blocked on external dependency or user feedback
status:in-progress    # Actively worked on
status:needs-review   # Ready for review / test
```

---

## 2. Issue Form vs Markdown Template Decision

- **Public Repositories**: Always use YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) with input validations and dropdowns to eliminate incomplete bug reports.
- **Private Minimal Repositories**: Markdown templates (`.md`) are permissible if rapid free-form communication is preferred.
