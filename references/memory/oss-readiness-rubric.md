# Open Source Readiness Rubric (10-Axis Evaluation)

<!-- last-verified: 2026-08-29 -->

Comprehensive 10-Axis framework to evaluate repository maturity from "code repository" to "sustainable open-source project".

---

## 📊 10 Evaluation Dimensions

| # | Dimension | Weight | Target Criteria | Key Artifacts |
|---|---|:---:|---|---|
| **1** | **Project Identity** | 10% | Clear archetype, tagline, keywords, crisp logo/banner, social preview | `README.md`, `brand.json`, Topics |
| **2** | **Documentation Architecture** | 10% | Diataxis framework (Tutorials, How-To, Reference, Explanation) | `README.md`, `/docs`, `mkdocs.yml` |
| **3** | **Contributor Experience (CX)** | 15% | Onboarding < 30m, friction points resolved, zero hidden prerequisites | `CONTRIBUTING.md`, `README.md` |
| **4** | **Good First Issue Engine** | 10% | Isolated scope, difficulty labels, reproduction steps, no arch locks | Issue tracker, Labels |
| **5** | **Community & Discussions** | 10% | Issue forms, PR templates, Code of Conduct, GitHub Discussions | `.github/ISSUE_TEMPLATE/`, `CODE_OF_CONDUCT.md` |
| **6** | **Governance & Decisions** | 10% | Explicit decision model, RFC/ADR pipeline, team roles | `GOVERNANCE.md`, `docs/rfcs/`, `docs/adrs/` |
| **7** | **Maintainer Sustainability** | 10% | Bus factor > 1, triage automation, PR backlog health, review SLAs | `CODEOWNERS`, Dependabot, Workflows |
| **8** | **Supply Chain Security** | 10% | Private vulnerability intake, SHA-pinned CI actions, SLSA baseline | `SECURITY.md`, `.github/workflows/` |
| **9** | **Release Engineering** | 10% | SemVer adherence, Keep a Changelog, Migration guides, matrix | `CHANGELOG.md`, Releases, Package tags |
| **10**| **Developer Discoverability** | 5% | "Why Not?" boundary section, crisp use-cases, anti-marketing clarity | `README.md` positioning |

---

## 🎯 Scoring & Maturity Tiers

```text
Score Range     Maturity Tier        Action Plan
──────────────────────────────────────────────────────────────────────
90 – 100        Enterprise OSS       Exemplary community benchmark
75 – 89         Production OSS       Minor polish on CX or Bus Factor
50 – 74         Emerging OSS         Needs Governance, CX & Issue forms
 0 – 49         Code Dump            Requires complete OSS overhaul
```
