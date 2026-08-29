<div align="center">

# 🐙 TidyFactor GitHub `v1.3.0`
### GitHub Platform Operations, Governance, Content, Experience & Intelligence Engine for AI Coding Agents

Give **Google Antigravity, Claude Code, Cursor, OpenAI Codex, or Windsurf** a comprehensive platform intelligence layer to govern, audit, secure, style, and operate GitHub organizations and repositories.

[![npm version](https://img.shields.io/npm/v/@tidyfactor/github.svg?style=for-the-badge&color=0284C7&logo=npm)](https://www.npmjs.com/package/@tidyfactor/github)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg?style=for-the-badge)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=for-the-badge)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=for-the-badge)](SKILL.md)
[![RTL Native Arabic](https://img.shields.io/badge/RTL-Native%20Arabic-emerald.svg?style=for-the-badge)](README.ar.md)
[![Architect Score](https://img.shields.io/badge/Architect%20Score-13%2F13%20Pass%20(100%25)-green.svg?style=for-the-badge)](#-governance--quality-bar)
[![AI Agents Compatible](https://img.shields.io/badge/AI%20Agents-Universal%20Compatibility-4285F4.svg?style=for-the-badge)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

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
npx @tidyfactor/cli-github
```

### Manual Workspace Injection
Clone or copy into your agent's customization root:
```bash
.agents/skills/tidyfactor-github/
```

---

## 👨‍💻 Organization & Support

- 🌐 **Official Website:** [https://tidyfactor.com/](https://tidyfactor.com/)
- 📚 **Official Documentation:** [https://tidyfactor.com/documentation](https://tidyfactor.com/documentation)
- 🤝 **Official Partner Website:** [Alwkala Digital Agency](https://alwkala.com/)
- 🐙 **GitHub Organization:** [github.com/TidyFactor](https://github.com/TidyFactor)
- 📧 **Business Inquiries:** [hello@tidyfactor.com](mailto:hello@tidyfactor.com)
- 📱 **WhatsApp:** [+20 101 665 6899](https://wa.me/201016656899)
- 📞 **Phone:** +20 101 665 6899
- 📍 **Location:** Cairo, Egypt

---

## 📜 License

Licensed under the **Apache License 2.0**. Copyright (c) 2026 [TidyFactor](https://tidyfactor.com) & [Alwkala](https://alwkala.com).
