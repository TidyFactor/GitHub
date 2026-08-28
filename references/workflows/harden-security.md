# Workflow: harden-security

One outcome: complete repository security hardening configuration including Dependabot, Secret Protection, and `SECURITY.md`.

## Steps

1. Load `references/memory/security-baseline.md` and `references/rules/sec-rules.md`.
2. Scaffold `.github/dependabot.yml` configured for the repository's package ecosystem.
3. Scaffold `.github/SECURITY.md` declaring supported versions and private vulnerability reporting instructions.
4. Verify repository secret scanning and push protection settings via `gh api` recommendations.

## Validation checklist

- [ ] `.github/dependabot.yml` is valid YAML with weekly/monthly update schedule
- [ ] `.github/SECURITY.md` defines supported versions table and contact email
- [ ] No plaintext secrets exist in any repository config or test fixture
