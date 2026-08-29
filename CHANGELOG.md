# Changelog

All notable changes to the `tidyfactor-github` skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-08-29

### Added - Open Source & Community Governance Engine
- **Open Source Project Readiness (10-Axis Audit)**: Standardized health audit evaluating Identity, Documentation, Onboarding (CX), Contribution, Community, Governance, Security, Releases, Maintainability, and Sustainability (0-100 score).
- **Contributor Experience (CX) & Onboarding Engine**:
  - First-time contributor journey analyzer calculating onboarding friction time (Discovery → Install → First PR).
  - Intelligent *Good First Issue* discovery engine with change-scope isolation, prerequisites check, and effort estimation.
  - 6-Tier *Contributor Ladder* framework (`Observer` → `User` → `First-time Contributor` → `Contributor` → `Maintainer` → `Core Maintainer`).
  - Community Recognition System with automatic `CONTRIBUTORS.md`, release credits, and hall of fame generators.
- **Maintainer Experience (MX) & Project Sustainability**:
  - Maintainer workload and PR/Issue review bottleneck analyzer.
  - Bus Factor, critical path redundancy, and knowledge concentration risk evaluator.
  - Community SLA and Time-to-First-Response benchmark tracker.
- **Open Source Governance & Architectural Decisions**:
  - Multi-tier `GOVERNANCE.md` generator supporting Benevolent Dictator, Core Team, Maintainer Council, and Consensus models.
  - RFC / Proposal lifecycle engine (`docs/rfcs/` workflow with formal problem, motivation, migration, and alternatives schemas).
  - Architecture Decision Records (ADR) pipeline linking decisions to Issues, PRs, and Releases.
- **Roadmap Engineering & Release Discipline**:
  - Multi-horizon public roadmap architecture (`Now`, `Next`, `Later`, `Exploring`) linked to GitHub Milestones and Projects.
  - Deprecation lifecycle and Breaking Change Migration Guide generator.
  - Compatibility matrix generator across runtimes, OS, frameworks, and databases.
- **Developer Discoverability, Positioning & Anti-Marketing**:
  - Developer-first Open Source SEO and use-case discoverability optimizer.
  - Exact project positioning engine (Library vs Tool vs Framework vs CLI vs SDK).
  - "Why Not?" & Boundary criterion builder to establish transparent use-case suitability.
  - Community FAQ extractor converting recurring discussion patterns into structured docs.
- **Supply Chain Security & Responsible Disclosure**:
  - Private security disclosure intake and vulnerability triage workflow.
  - Security Policy UX and CVE/Advisory preparation tooling.
  - OpenSSF Scorecard and SLSA supply chain readiness checks.
- **Open Source Operating Lifecycle (17 Modes)**: Complete lifecycle matrix covering `oss-init`, `oss-audit`, `oss-launch`, `oss-onboard`, `oss-maintain`, `oss-triage`, `oss-govern`, `oss-release`, `oss-secure`, `oss-document`, `oss-community`, `oss-roadmap`, `oss-rfc`, `oss-deprecate`, `oss-migrate`, `oss-sustain`, and `oss-archive`.

## [1.0.0] - 2026-08-29

### Added
- Initial public release of `tidyfactor-github` (GitHub Platform Operations, Governance, Content, Experience & Intelligence Engine).
- 5-Layer Engine architecture: Operations, Governance, Content, Styling, and Ecosystem Intelligence.
- 3 Strict Execution Modes: `AUDIT` (read-only scorecard), `PLAN` (dry-run & gap analysis), and `APPLY` (safe execution with explicit confirmation gates).
- Contextual Decision Layer (CDL) with `/brief` command and `.tidyfactor/github-brief.md` cache.
- 17 specialized runtime commands and 17 single-outcome workflows with validation checklists.
- 4 Prioritized Rule Catalogs: Security (`sec-rules.md`), Governance (`gov-rules.md`), Content Anti-Slop (`content-rules.md`), and CI/CD (`ci-rules.md`).
- Repository and Organization Blueprints with JSON Schema validation (`audit-report.schema.json`, `blueprint.schema.json`, `permission-matrix.schema.json`).
- Deterministic native tooling: `tools/repo_audit.py`, `tools/org_audit.py`, `tools/readme_linter.py`, `tools/validate_skill.py`, and `tools/build-skill.js`.
