<div align="center">

# TidyFactor GitHub

**GitHub Platform Operations, Governance, Content, Experience & Intelligence Engine for AI Coding Agents**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[English](README.md) • [العربية](README.ar.md)

</div>

---

## Overview

`tidyfactor-github` is an enterprise-grade AI Coding Agent Skill that turns GitHub from a passive Git remote into a governed, secure, automated, beautifully styled, and high-converting software project hub.

It operates across the entire GitHub platform hierarchy:
**Account** ➔ **Organization** ➔ **Repository** ➔ **Code** ➔ **Collaboration** ➔ **Security** ➔ **Developer Experience**.

---

## Core Capabilities & 5-Layer Engine

```text
                               ┌─────────────────────────────────────────┐
                               │            TIDYFACTOR GITHUB            │
                               │  GitHub Platform Operations & Intel     │
                               └────────────────────┬────────────────────┘
                                                    │
        ┌───────────────────┬───────────────────────┼───────────────────────┬───────────────────┐
        │                   │                       │                       │                   │
  ┌─────▼───────┐     ┌─────▼─────────┐       ┌─────▼─────────┐       ┌─────▼─────────┐   ┌─────▼─────────┐
  │ OPERATIONS  │     │  GOVERNANCE   │       │    CONTENT    │       │    STYLING    │   │ INTELLIGENCE  │
  ├─────────────┤     ├───────────────┤       ├───────────────┤       ├───────────────┤   ├───────────────┤
  │• Org & Repos│     │• Rulesets     │       │• README UX    │       │• Visual Lang  │   │• State Memory │
  │• Members/Team│    │• CODEOWNERS   │       │• Issue Forms  │       │• Badge Matrix │   │• ADR Memory   │
  │• Branches   │     │• Security/2FA │       │• PR Workflows │       │• Typography   │   │• Drift Detect │
  │• Actions/CI │     │• LeastPrivileg│       │• Docsify/Wiki │       │• Social Banner│   │• Blueprint Gap│
  │• Releases/Pkg│    │• Policies     │       │• Changelogs   │       │• Scannability │   │• Incident Tria│
  └─────────────┘     └───────────────┘       └───────────────┘       └───────────────┘   └───────────────┘
```

1. **Operations Layer**: Repository lifecycle, organizational hierarchy, teams, branches, releases, and packages.
2. **Governance Layer**: GitHub Rulesets, branch protection, CODEOWNERS, permission matrix, and organization policies.
3. **Content Layer**: README Experience Engine, interactive Issue Forms (`.yml`), stack-tailored PR templates, and bilingual documentation.
4. **Styling Layer**: Repository visual hierarchy, curated badge density, social preview cards, and scannable technical structure.
5. **Intelligence Layer**: Contextual decision memory, ADR tracking, blueprint gap analysis, and emergency incident postmortems.

---

## Triple Execution Modes & Safety Gate

| Mode | Behavior | Safety Gate |
|---|---|---|
| **`AUDIT`** *(Default)* | Inspects repositories and organizations, calculates 9-dimensional health scorecards (0-100), and flags anomalies with zero writes. | Read-Only |
| **`PLAN`** *(Dry-Run)* | Computes drift from `repository.blueprint.yml`, produces file diffs, and prepares proposed `gh` CLI commands. | Simulation |
| **`APPLY`** *(Governed)* | Applies approved configuration files and automation. Destructive actions (repo deletion, force pushes, admin elevation, visibility changes) require explicit interactive confirmation. | Gated Execution |

---

## Command Dispatcher Matrix

| Command | Purpose | Loaded Workflows & Memory |
|---|---|---|
| `/brief` | Strategic discovery & baseline configuration (CDL) | `brief-discovery.md` + `decision-points.md` |
| `/audit` | 9-Dimensional Repository & Organization Scorecards | `run-repo-audit.md` + `maturity-model.md` |
| `/org` | Organization architecture, teams & permission matrix | `setup-org-hierarchy.md` + `permission-matrix.md` |
| `/repo` | Repository factory, lifecycle & portfolio health | `scaffold-repository.md` + `maturity-model.md` |
| `/branch` | Branching strategies, GitFlow, Trunk & naming | `configure-rulesets.md` + `branch-strategies.md` |
| `/ruleset` | Organization & repo-level GitHub Rulesets | `configure-rulesets.md` + `gov-rules.md` |
| `/issue` | Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) | `setup-issue-forms.md` + `issue-taxonomy.md` |
| `/pr` | PR templates, CODEOWNERS & review workflows | `setup-pr-template.md` + `permission-matrix.md` |
| `/action` | CI/CD actions, SHA pinning & supply chain audits | `audit-actions-ci.md` + `ci-rules.md` + `sec-rules.md` |
| `/security` | Hardening, Dependabot, 2FA & secret scanning | `harden-security.md` + `sec-rules.md` |
| `/community` | Community health files (`CONTRIBUTING`, `SECURITY`) | `setup-community-health.md` + `maturity-model.md` |
| `/readme` | README UX Engine & Anti-Slop content polishing | `craft-readme.md` + `content-rules.md` |
| `/style` | Repository visual tokens, badges & social preview | `design-social-preview.md` + `content-rules.md` |
| `/release` | SemVer release automation, tags & CHANGELOG SSOT | `automate-release.md` + `maturity-model.md` |
| `/project` | GitHub Projects (v2), fields, views & roadmaps | `manage-projects.md` + `maturity-model.md` |
| `/discover` | Repository Discoverability Optimization (RDO) | `optimize-discoverability.md` + `rdo-matrix.md` |
| `/incident` | Emergency triage, commit diffs, rollback & postmortem | `handle-incident.md` + `security-baseline.md` |
| `/blueprint` | Blueprint gap analysis & automated alignment | `apply-blueprint.md` + `decision-points.md` |

---

## Prioritized Rule Catalogs

The skill enforces four prioritized rule catalogs ranking violations from `CRITICAL` down to `LOW`:
- **Security (`sec-rules.md`)**: SHA pinning for actions, minimal job permissions, secret push protection, Dependabot.
- **Governance (`gov-rules.md`)**: Default branch protection, linear history, CODEOWNERS coverage, conversation resolution.
- **Content (`content-rules.md`)**: Anti-slop banned marketing phrases, above-the-fold value clarity, badge density limit ($\le 5$).
- **CI/CD (`ci-rules.md`)**: Outdated run concurrency cancellation, explicit timeouts, native dependency caching.

---

## Installation & Injection

### Quick Injection (Local Project)
```bash
npx @alwkala/tidyfactor-github
```

### Manual Workspace Injection
Clone or copy into your agent's customization root:
```bash
.agents/skills/tidyfactor-github/
```

---

## License

Apache-2.0 © [TidyFactor](https://github.com/TidyFactor) & [Alwkala](https://alwkala.com)
