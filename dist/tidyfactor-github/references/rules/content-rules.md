# Prioritized Rule Catalog: Content & README Anti-Slop (`content-`)

<!-- last-verified: 2026-08-29 -->

Deterministic rules for technical clarity, scannability, README UX, and eliminating AI slop.

---

## 🔴 CRITICAL Impact

### `content-01-ban-marketing-slop`
- **Rule ID**: `content-01`
- **Impact Tier**: `CRITICAL`
- **Rationale**: Marketing buzzwords, vague adjectives, and hype diminish developer trust and obscure actual functionality.
- **Banned Words & Phrases (❌)**:
  - *"A revolutionary next-generation platform..."*
  - *"Blazing fast, game-changing framework..."*
  - *"Seamlessly leverages cutting-edge AI power..."*
  - *"The ultimate all-in-one solution for developers..."*
  - *"State of the art magic..."*
- **Correct Technical Replacement (✅)**:
  - *"Modular TypeScript engine for tenant-isolated PostgreSQL workloads with automated RLS policy generation."*
  - *"Zero-dependency vanilla JavaScript routing proxy with microsecond state propagation."*

---

## 🟠 HIGH Impact

### `content-02-above-the-fold-clarity`
- **Rule ID**: `content-02`
- **Impact Tier**: `HIGH`
- **Rationale**: A developer visiting a repository must understand within 5 seconds: What it is, why it exists, and how to install/run it.
- **Required Above-the-Fold Order**:
  1. Title / Logo
  2. One-line crisp technical positioning statement
  3. Curated status badges (max 5)
  4. 3-line Quick Start code block (install + run)
  5. 2-sentence value proposition with zero fluff

### `content-03-badge-density-limit`
- **Rule ID**: `content-03`
- **Impact Tier**: `HIGH`
- **Rationale**: Giant badge walls (> 6 badges) create visual clutter and slow page loading.
- **Allowed Badges**:
  - `Version / Release`
  - `Build / CI Status`
  - `Code Coverage / Quality`
  - `License`
  - `TypeScript / Language version`

---

## 🟡 MEDIUM Impact

### `content-04-scannable-heading-hierarchy`
- **Rule ID**: `content-04`
- **Impact Tier**: `MEDIUM`
- **Rationale**: Long walls of unbroken text are skipped. Use bullet points, comparison tables, and collapsible details (`<details><summary>`) for deep technical references.

### `content-05-bilingual-arabic-rtl`
- **Rule ID**: `content-05`
- **Impact Tier**: `MEDIUM`
- **Rationale**: When providing an Arabic version (`README.ar.md`):
  - Must include `<div dir="rtl">`.
  - Use natural technical Arabic (فصحى معاصرة رصينة), not mechanical machine translation.
  - Never translate core code symbols, CLI commands, or standard abbreviations (e.g. CI/CD, PR, API, RBAC).

---

## 🟢 LOW Impact

### `content-06-working-demo-media`
- **Rule ID**: `content-06`
- **Impact Tier**: `LOW`
- **Rationale**: Screenshots and GIFs must show actual code outputs, terminal commands, or UI states—never generic stock photos or unlabelled diagrams.
