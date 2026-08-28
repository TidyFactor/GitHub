# Prioritized Rule Catalog: GitHub Actions CI/CD (`ci-`)

<!-- last-verified: 2026-08-29 -->

Deterministic rules for fast, secure, idempotent, and resource-efficient GitHub Actions workflows.

---

## 🔴 CRITICAL Impact

### `ci-01-concurrency-cancel-in-progress`
- **Rule ID**: `ci-01`
- **Impact Tier**: `CRITICAL`
- **Rationale**: Pushing multiple commits to an open PR triggers redundant build matrix runs, wasting GitHub Actions runner minutes and delaying merge checks.
- **Correct**:
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
    cancel-in-progress: true
  ```

---

## 🟠 HIGH Impact

### `ci-02-explicit-job-timeouts`
- **Rule ID**: `ci-02`
- **Impact Tier**: `HIGH`
- **Rationale**: The default job timeout in GitHub Actions is 360 minutes (6 hours). A hung test or infinite loop will exhaust runner quotas unless capped explicitly.
- **Correct**:
  ```yaml
  jobs:
    test:
      runs-on: ubuntu-latest
      timeout-minutes: 15
      steps: ...
  ```

### `ci-03-native-dependency-caching`
- **Rule ID**: `ci-03`
- **Impact Tier**: `HIGH`
- **Rationale**: Re-downloading dependencies on every run adds 1-3 minutes of latency per job. Use native action caching options (`actions/setup-node` `cache: 'npm'`, `setup-python` `cache: 'pip'`).

---

## 🟡 MEDIUM Impact

### `ci-04-matrix-fast-fail`
- **Rule ID**: `ci-04`
- **Impact Tier**: `MEDIUM`
- **Rationale**: In matrix builds (e.g. Node 18, 20, 22), failing fast on the first error saves compute time on already-broken PRs.
- **Correct**:
  ```yaml
  strategy:
    fail-fast: true
    matrix:
      node-version: [18, 20, 22]
  ```

---

## 🟢 LOW Impact

### `ci-05-descriptive-step-names`
- **Rule ID**: `ci-05`
- **Impact Tier**: `LOW`
- **Rationale**: Every step must have a concise `name:` describing its action so failed logs can be diagnosed without opening step definitions.
