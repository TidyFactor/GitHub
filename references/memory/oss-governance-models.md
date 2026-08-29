# Open Source Governance Models & Team Structures

<!-- last-verified: 2026-08-29 -->

Formal governance archetypes and decision frameworks for open-source repositories.

---

## 🏛️ 1. Governance Archetypes

| Model | Decision Maker | Best Suited For | Risk |
|---|---|---|---|
| **Benevolent Dictator (BDFL)** | Single project founder / lead | Early-stage, fast-moving tools, indie OSS | High bus factor, founder burnout |
| **Core Team** | 3-7 trusted engineers with equal vote | Maturing libraries, multi-tenant frameworks | Decision deadlock if even-numbered |
| **Maintainer Council** | Elected representatives across sub-repos | Multi-package monorepos, foundations | Governance overhead |
| **Consensus / Working Groups** | Domain-specific working groups (Security, Docs, Engine) | Large enterprise ecosystems | Slower pace of change |

---

## 👥 2. Standard Role & Permission Mapping

```text
Role               GitHub Permission     Responsibilities
─────────────────────────────────────────────────────────────────────────────
Owner / Lead       Admin                 Repository settings, security keys, releases
Maintainer         Write                 Triage, PR reviews, merge to main, milestones
Reviewer / Member  Triage                Issue sorting, labels, PR reviews (no merge)
Contributor        Read (Fork)           Submitting PRs, issue reports, RFC drafts
```

---

## 📜 3. Mandatory Governance Elements (`GOVERNANCE.md`)

1. **Mission Statement**: Core purpose and long-term vision of the project.
2. **Decision-Making Process**: How technical proposals (RFCs) are evaluated, debated, and voted on.
3. **Maintainer Nominations**: Transparent criteria for onboarding new maintainers.
4. **Conflict Resolution**: Escalation path when maintainers cannot reach consensus.
5. **Code of Conduct Enforcement**: Explicit team designated to handle incident reports.
