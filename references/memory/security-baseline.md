# Security Baseline & Supply Chain Integrity

<!-- last-verified: 2026-08-29 -->

Mandatory security configurations, automated scanning tools, and incident response matrices.

---

## 1. Automated Security Matrix

| Tool / Feature | Scope | Requirement | Configuration Path |
|---|---|---|---|
| **Secret Scanning** | Repository / Org | Mandatory on all repos | Repository Settings / Security |
| **Push Protection** | Repository / Org | Mandatory on all repos | Blocks commits with exposed API keys |
| **Dependabot Alerts** | Repository | Mandatory on all public & private repos | Security & Analysis |
| **Dependabot Updates** | Manifests | Weekly / Monthly schedule | `.github/dependabot.yml` |
| **CodeQL Scanning** | Codebase | Recommended on compiled & web repos | `.github/workflows/codeql.yml` |
| **Dependency Review** | Pull Requests | Recommended on PRs modifying lockfiles | `.github/workflows/dependency-review.yml` |

---

## 2. Standard `SECURITY.md` Template Structure

```markdown
# Security Policy

## Supported Versions
| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability
Do NOT open public GitHub Issues for security vulnerabilities.
1. Email: `security@tidyfactor.com` or use [GitHub Private Vulnerability Reporting].
2. Response SLA: Initial triage within 48 hours.
3. Fix & Advisory: Coordinated disclosure after release patch.
```

---

## 3. Dependency Pinning & SHA Verification

All GitHub Actions in `.github/workflows/*.yml` must specify the full commit SHA alongside the version comment:
```text
actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
actions/setup-node@39370e3970a6d050c480ffad4ff0ed4d3fdee5af # v4.1.0
actions/setup-python@0b93645e9fea7318ecaed2b359559ac225c90a2b # v5.3.0
```
