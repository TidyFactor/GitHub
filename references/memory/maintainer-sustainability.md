# Maintainer Sustainability & Workload Intelligence

<!-- last-verified: 2026-08-29 -->

Operational rules to protect maintainers against burnout, evaluate project Bus Factor, and maintain community SLA benchmarks.

---

## ⚖️ 1. Maintainer Load Dimensions

```text
Load Dimension      Risk Indicator               Mitigation Strategy
─────────────────────────────────────────────────────────────────────────────
PR Backlog          > 15 unreviewed PRs          Stricter PR template, AI pre-review
Issue Triage        > 30 untriaged issues        GitHub Issue Forms, auto-labeling
Release Burden      Manual multi-step packaging  GitHub Actions CI/CD automation
Security Ingestion  Public issues for vulns      GitHub Private Vulnerability Reporting
Knowledge Lock      1 person knows subsystem     Architecture Decision Records (ADR)
```

---

## 🚌 2. Bus Factor Evaluation Matrix

```text
Bus Factor Score    Redundancy Status            Risk Level
─────────────────────────────────────────────────────────────────────────────
1 Person            Critical single-point-failure Extreme (Red)
2 Persons           Minimum viable redundancy    Moderate (Yellow)
3+ Persons          Healthy distributed team     Low (Green)
```

### Redundancy Checklist
- [ ] Multiple maintainers have NPM/PyPI publishing permissions or secret rotation keys.
- [ ] At least 2 team members have GitHub Org Owner or Repository Admin roles.
- [ ] CI/CD release secrets are stored in organization secrets, not individual accounts.
- [ ] Deployment and emergency rollback playbooks are documented in `references/workflows/`.

---

## ⏱️ 3. Standard Community Response SLAs

```text
Category               Target Response Time    Max Acceptable Time
─────────────────────────────────────────────────────────────────────────────
Security Vulnerability < 24 hours              < 48 hours
Critical CI/Release Bug< 48 hours              < 72 hours
First-time PR Review   < 3 days                < 7 days
General Issue / Question < 4 days              < 10 days
```
