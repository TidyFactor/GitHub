---
name: tidyfactor-github
description: "GitHub Platform Operations, Governance, Content, Experience & Intelligence Engine with Contextual Decision Layer (CDL). Inspect, govern, secure, automate, style, and manage repositories, organizations, rulesets, actions, issues, PRs, and README UX. Trigger on commands 'brief', 'audit', 'org', 'repo', 'branch', 'ruleset', 'issue', 'pr', 'action', 'security', 'community', 'readme', 'style', 'release', 'project', 'discover', 'incident', 'blueprint', or requests for GitHub repository management, repo audit, ruleset governance, GitHub Actions CI, or README optimization."
---

# TidyFactor GitHub

A command dispatcher for GitHub Platform Operations, Governance, Content, Experience & Ecosystem Intelligence. This router declares commands and workflows without performing execution directly.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| Strategic Discovery & Baseline Architecture | `references/commands/brief.md` | `workflows/brief-discovery.md` + `memory/decision-points.md` |
| 9-Dimension Repository & Org Health Audit | `references/commands/audit.md` | `workflows/run-repo-audit.md` + `workflows/run-org-audit.md` + `memory/maturity-model.md` |
| Org Architecture, Teams & Permission Matrix | `references/commands/org.md` | `workflows/setup-org-hierarchy.md` + `memory/permission-matrix.md` |
| Repository Lifecycle & Factory Scaffolding | `references/commands/repo.md` | `workflows/scaffold-repository.md` + `memory/maturity-model.md` |
| Branch Strategies, Naming & Flow Models | `references/commands/branch.md` | `workflows/configure-rulesets.md` + `memory/branch-strategies.md` |
| GitHub Rulesets & Branch Governance | `references/commands/ruleset.md` | `workflows/configure-rulesets.md` + `memory/ruleset-profiles.md` + `rules/gov-rules.md` |
| Issue Forms, Templates & Taxonomy | `references/commands/issue.md` | `workflows/setup-issue-forms.md` + `memory/issue-taxonomy.md` |
| PR Templates, CODEOWNERS & Review Engine | `references/commands/pr.md` | `workflows/setup-pr-template.md` + `memory/permission-matrix.md` + `rules/gov-rules.md` |
| Actions CI/CD, SHA Pinning & Supply Chain | `references/commands/action.md` | `workflows/audit-actions-ci.md` + `rules/ci-rules.md` + `rules/sec-rules.md` |
| Security Hardening, Dependabot & Secrets | `references/commands/security.md` | `workflows/harden-security.md` + `memory/security-baseline.md` + `rules/sec-rules.md` |
| Community Health Files & OSS Maintainer Mode | `references/commands/community.md` | `workflows/setup-community-health.md` + `memory/maturity-model.md` |
| README Experience Engine & Anti-Slop | `references/commands/readme.md` | `workflows/craft-readme.md` + `memory/readme-architecture.md` + `rules/content-rules.md` |
| Visual Styling, Badges & Social Preview | `references/commands/style.md` | `workflows/design-social-preview.md` + `memory/repo-design-tokens.md` + `rules/content-rules.md` |
| Release Automation, SemVer & Changelog | `references/commands/release.md` | `workflows/automate-release.md` + `memory/maturity-model.md` |
| Projects (v2), Fields, Roadmaps & Views | `references/commands/project.md` | `workflows/manage-projects.md` + `memory/maturity-model.md` |
| Discoverability Optimization (RDO) & SEO | `references/commands/discover.md` | `workflows/optimize-discoverability.md` + `memory/rdo-matrix.md` |
| Emergency Incident Triage & Postmortem | `references/commands/incident.md` | `workflows/handle-incident.md` + `memory/security-baseline.md` |
| Blueprint Gap Analysis & Transformation | `references/commands/blueprint.md` | `workflows/apply-blueprint.md` + `memory/decision-points.md` |

Read only the command file that matches the request. Do not load all commands simultaneously.

## Non-Negotiable Invariants

1. **Contextual Decision Layer (CDL)**: Resolve repository baselines via `/brief` or `.tidyfactor/github-brief.md` before generating files.
2. **Triple Execution Modes**: Default to `AUDIT` (read-only) or `PLAN` (dry-run). `APPLY` requires explicit confirmation for destructive actions (repo deletion, force pushes, admin grants, visibility switches).
3. **Least Privilege by Default**: Never assign direct admin rights to individuals; enforce team-based RBAC and fine-grained repository access.
4. **Supply Chain Security**: All GitHub Actions references MUST be pinned to full commit SHAs (`action@sha256`) with `permissions: contents: read` minimum baseline.
5. **Anti-Slop Content Engine**: Reject marketing fluff, generic AI claims, and badge walls. Deliver scannable, developer-first documentation.
6. **7-Axis Pre-Emit Critique**: All generated configs and workflows must satisfy `/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`.

## Tool Permission Declaration (Rule 10)

- **Languages**: Python, Node.js, Shell (GitHub CLI `gh`, `git`)
- **Mutations**: Local repository configuration, template scaffolding, workflows, and documentation
- **Network**: GitHub API via `gh` CLI when explicitly authorized by the user in `APPLY` mode

## Skill vs MCP Boundary (Rule 12)

- **Inside Skill**: Static architecture rules, decision matrices, scorecards, linters, issue forms, blueprints, and workflow templates.
- **MCP / CLI Layer**: Live API querying, remote mutations, and authentication delegated strictly to `gh` CLI or GitHub MCP server.
