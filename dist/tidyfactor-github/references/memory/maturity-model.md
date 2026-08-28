# Repository Maturity Model & 9-Dimension Health Scorecard

<!-- last-verified: 2026-08-29 -->

Deterministic classification model and scoring framework for GitHub repositories and organizations.

---

## 1. The 7 Maturity Levels

| Level | Name | Criteria |
|---|---|---|
| **Level 0** | *Raw* | Bare Git repo, no README, no license, direct commits to main. |
| **Level 1** | *Basic* | Basic README, LICENSE, gitignore present. No CI or branch protection. |
| **Level 2** | *Organized* | Structured README, standard branch naming, manual PR merges, basic issue tracker. |
| **Level 3** | *Maintained* | CI actions (lint + test), protected default branch, Dependabot enabled, CONTRIBUTING file. |
| **Level 4** | *Production* | Branch rulesets enforced, CODEOWNERS, automated releases with SemVer, issue forms, secret scanning. |
| **Level 5** | *Mature OSS* | Full community health files, discussion categories, SHA-pinned actions, RDO topics, bilingual docs, zero slop. |
| **Level 6** | *Enterprise* | Strict organization RBAC, team-only permissions, signed commits, SBOM attestation, incident runbooks, drift detection. |

---

## 2. The 9 Health Dimensions (0-100 Score)

```text
Score Calculation:
Total Score = Sum(Dimension Weight * Score) / 100
```

| Dimension | Weight | Key Verification Checkpoints |
|---|---|---|
| **1. Identity & Discoverability** | 10% | Description ($\le 120$ chars), website URL, 8-12 accurate topics, clean repo name. |
| **2. Documentation & README UX** | 15% | Above-the-fold clarity, quick start code, architecture diagram, license, bilingual RTL. |
| **3. Developer Experience (DX)** | 10% | One-command setup, mock fixtures, pre-commit hooks, strict error diagnostics. |
| **4. Community Health** | 10% | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `SECURITY.md`, `FUNDING.yml`. |
| **5. Security & Supply Chain** | 15% | Dependabot active, push protection on, 0 exposed secrets, SHA-pinned actions. |
| **6. CI/CD & Automation** | 15% | Automated test/lint on PR, concurrency cancel, job timeouts, package caching. |
| **7. Governance & Rulesets** | 10% | Protected main branch, min 1 approval, CODEOWNERS coverage, linear history. |
| **8. Issue & PR Engineering** | 10% | Issue Forms (`.yml`) with required fields, PR review checklist, clean label taxonomy. |
| **9. Visual Presentation** | 5% | Badges $\le 5$, custom social preview card (1280x640), consistent table layouts. |
