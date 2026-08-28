# Prioritized Rule Catalog: Governance & Rulesets (`gov-`)

<!-- last-verified: 2026-08-29 -->

Deterministic rules for branch protection, rulesets, CODEOWNERS, merge strategies, and team permissions.

---

## 🔴 CRITICAL Impact

### `gov-01-protect-default-branch`
- **Rule ID**: `gov-01`
- **Impact Tier**: `CRITICAL`
- **Rationale**: Direct pushes and unreviewed merges to `main` or default production branches lead to broken builds and untracked defects.
- **Invariants**:
  - Direct push blocked.
  - Force push blocked (`allow_force_pushes: false`).
  - Branch deletion blocked (`allow_deletions: false`).
  - Pull Request required before merging (`required_pull_request_reviews: min 1 approval`).

### `gov-02-least-privilege-rbac`
- **Rule ID**: `gov-02`
- **Impact Tier**: `CRITICAL`
- **Rationale**: Direct individual permissions on repositories create security blind spots and orphaned access when members leave. Access must be mapped through functional teams (`@org/team`).
- **Policy**:
  - `Admin`: Restricted to Platform / DevOps leads (max 2-3 owners).
  - `Maintain`: Core maintainers of the specific repository.
  - `Write`: Active domain engineers for everyday feature PRs.
  - `Triage` / `Read`: General members and documentation contributors.

---

## 🟠 HIGH Impact

### `gov-03-enforce-codeowners`
- **Rule ID**: `gov-03`
- **Impact Tier**: `HIGH`
- **Rationale**: Critical infrastructure, security policies, and database schemas should never be merged without the explicit approval of domain owners.
- **Correct (`.github/CODEOWNERS`)**:
  ```text
  # Global fallback
  *                   @org/engineering

  # Security and Workflows
  /.github/workflows/ @org/devops @org/security
  /SECURITY.md        @org/security

  # Infrastructure & Database
  /infra/             @org/devops
  /db/migrations/     @org/backend-leads
  ```

### `gov-04-require-status-checks`
- **Rule ID**: `gov-04`
- **Impact Tier**: `HIGH`
- **Rationale**: Branches must pass all automated CI checks (lint, test, build, typecheck) and be up-to-date with the base branch before merge.

---

## 🟡 MEDIUM Impact

### `gov-05-require-linear-history`
- **Rule ID**: `gov-05`
- **Impact Tier**: `MEDIUM`
- **Rationale**: Complex merge commits pollute Git history and make bisecting regressions difficult. Enforce linear history via Squash & Merge or Rebase & Merge.

### `gov-06-resolve-all-conversations`
- **Rule ID**: `gov-06`
- **Impact Tier**: `MEDIUM`
- **Rationale**: Pull requests must not be merged while review discussions remain unresolved.

---

## 🟢 LOW Impact

### `gov-07-standard-branch-naming`
- **Rule ID**: `gov-07`
- **Impact Tier**: `LOW`
- **Rationale**: Branches must adhere to standard prefixes: `feature/*`, `fix/*`, `docs/*`, `refactor/*`, `release/*`, `hotfix/*`.
