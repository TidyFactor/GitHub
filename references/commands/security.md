# Command: security

Runtime entry point for security hardening, Dependabot configuration, and secret protection.

## Dispatch steps

1. Load `../workflows/harden-security.md` — security hardening workflow.
2. Load `../memory/security-baseline.md` — Dependabot, CodeQL, and SECURITY.md schemas.
3. Load `../rules/sec-rules.md` — prioritized security catalog.
4. Scaffold `.github/dependabot.yml`, `SECURITY.md`, and verify secret scanning status.

## Do not

- Do not expose credentials or tokens in workflow logs or sample files.
- Do not skip vulnerability reporting SLAs in `SECURITY.md`.
