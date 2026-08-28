# Branch Strategies & Workflow Flow Models

<!-- last-verified: 2026-08-29 -->

Deterministic branch taxonomies, lifecycle models, and merge conventions.

---

## 1. Branch Strategy Models

### A. Trunk-Based Development (Recommended for SaaS & Microservices)
- **Production Branch**: `main`
- **Short-Lived Branches**: `feat/*`, `fix/*`, `chore/*` (Lifespan $\le 48$ hours)
- **Merge Strategy**: Squash & Merge
- **Release Trigger**: Automated tag on every merge to `main`.

### B. GitHub Flow (Recommended for Libraries & Developer Tools)
- **Production Branch**: `main`
- **Feature Branches**: `feature/<short-desc>`, `fix/<issue-id>-<desc>`
- **Release Branches**: `release/vX.Y.Z`
- **Merge Strategy**: Rebase & Merge or Squash & Merge.

### C. GitFlow (Legacy / Complex Enterprise Releases)
- **Branches**: `main` (Production), `develop` (Integration), `feature/*`, `release/*`, `hotfix/*`.

---

## 2. Standard Branch Naming Taxonomy

| Prefix | Usage | Example |
|---|---|---|
| `feature/` | New functionality or major capability expansion | `feature/issue-forms-v2` |
| `fix/` | Bug fixes or defect repairs | `fix/action-caching-leak` |
| `refactor/` | Code structure improvements without functional change | `refactor/ruleset-loader` |
| `docs/` | Documentation additions or translations | `docs/arabic-readme-sync` |
| `perf/` | Performance optimizations and bundle reductions | `perf/tree-shaking-bundle` |
| `sec/` | Security patches and vulnerability fixes | `sec/pin-action-sha` |
| `release/` | Pre-release staging and version bumps | `release/v1.1.0` |
| `hotfix/` | Urgent production fixes targeting release tags | `hotfix/v1.0.1-auth-panic` |
