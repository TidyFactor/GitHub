# Prioritized Rule Catalog: Security & Supply Chain (`sec-`)

<!-- last-verified: 2026-08-29 -->

Deterministic security invariants for GitHub repositories, organizations, workflows, and secret management.

---

## 🔴 CRITICAL Impact

### `sec-01-pin-actions-sha`
- **Rule ID**: `sec-01`
- **Impact Tier**: `CRITICAL`
- **Rationale**: Using mutable tags (e.g. `@v4`, `@main`, `@master`) in third-party GitHub Actions allows attackers who compromise upstream repositories to inject malicious code directly into CI/CD pipelines.
- **Incorrect (❌)**:
  ```yaml
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
  ```
- **Correct (✅)**:
  ```yaml
  steps:
    - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
    - uses: actions/setup-node@39370e3970a6d050c480ffad4ff0ed4d3fdee5af # v4.1.0
  ```

### `sec-02-minimal-actions-permissions`
- **Rule ID**: `sec-02`
- **Impact Tier**: `CRITICAL`
- **Rationale**: The default `GITHUB_TOKEN` in GitHub Actions may have broad write permissions. Every workflow file must explicitly lock top-level permissions to `contents: read` and only grant write scopes to specific jobs that require them.
- **Incorrect (❌)**:
  ```yaml
  name: CI
  on: [push, pull_request]
  # No top-level permissions block!
  jobs:
    build: ...
  ```
- **Correct (✅)**:
  ```yaml
  name: CI
  on: [push, pull_request]
  permissions:
    contents: read
  jobs:
    build:
      permissions:
        contents: read
        packages: write # only when publishing
  ```

### `sec-03-secret-push-protection`
- **Rule ID**: `sec-03`
- **Impact Tier**: `CRITICAL`
- **Rationale**: Accidental commits containing API keys, database credentials, or private keys lead to immediate security compromises. Secret push protection must be enabled organization-wide and per repository.
- **Enforcement**:
  ```json
  {
    "security_and_analysis": {
      "secret_scanning": { "status": "enabled" },
      "secret_scanning_push_protection": { "status": "enabled" }
    }
  }
  ```

---

## 🟠 HIGH Impact

### `sec-04-dependabot-security-updates`
- **Rule ID**: `sec-04`
- **Impact Tier**: `HIGH`
- **Rationale**: Vulnerable dependencies are the primary entry point for web application attacks. Dependabot security alerts and automated security pull requests must be active for all manifest files.
- **Correct (`.github/dependabot.yml`)**:
  ```yaml
  version: 2
  updates:
    - package-ecosystem: "npm"
      directory: "/"
      schedule:
        interval: "weekly"
      open-pull-requests-limit: 10
      labels:
        - "type:dependency"
        - "area:security"
  ```

### `sec-05-no-service-keys-in-public-code`
- **Rule ID**: `sec-05`
- **Impact Tier**: `HIGH`
- **Rationale**: Service-role keys (e.g. Supabase Admin, AWS Master Keys, Stripe Secret Keys) must never appear in frontend code, mock files, or client-side bundles.

---

## 🟡 MEDIUM Impact

### `sec-06-require-signed-commits`
- **Rule ID**: `sec-06`
- **Impact Tier**: `MEDIUM`
- **Rationale**: Protects against commit author spoofing. Rulesets should enforce commit signature verification (GPG, SSH, or S/MIME) on protected branches.

### `sec-07-two-factor-auth-enforcement`
- **Rule ID**: `sec-07`
- **Impact Tier**: `MEDIUM`
- **Rationale**: All organization members and outside collaborators must have mandatory 2FA enabled before being granted repository write access.

---

## 🟢 LOW Impact

### `sec-08-security-policy-file`
- **Rule ID**: `sec-08`
- **Impact Tier**: `LOW`
- **Rationale**: Every public repository must contain a `.github/SECURITY.md` or `SECURITY.md` declaring supported versions, disclosure protocols, and response SLAs.
