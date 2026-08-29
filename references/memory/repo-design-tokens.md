# Repository Design Tokens & Social Preview Specifications

<!-- last-verified: 2026-08-29 -->

Design tokens, badge formatting, and Open Graph card dimensions for GitHub repositories.

---

## 1. Social Preview Open Graph Card Specs

- **Aspect Ratio**: `2:1`
- **Recommended Dimensions**: `1280 x 640 px`
- **Safe Zone**: `1080 x 540 px` (Center aligned, 100px padding)
- **Visual Elements**:
  - Top Left: Category Pill (e.g. `TIDYFACTOR / GOVERNANCE`)
  - Center: Project Title (Bold Sans-Serif, 56-64px) + Tagline (Regular, 24-28px)
  - Bottom Bar: Ecosystem Badges + Compatibility Icons

---

## 2. Standard Shields.io Badge Tokens

- **Style**: `style=for-the-badge` (Bold, premium developer aesthetic)
- **Palette**:
  - `Version / NPM`: `blue` (`#0284C7` / `color=0284C7`)
  - `License`: `blue` (`License-Apache--2.0-blue`)
  - `Ecosystem Tier`: `purple` (`purple` / `#6f42c1`)
  - `Compatibility`: `orange` (`orange` / `#f66a0a`)
  - `RTL Native Support`: `emerald` (`emerald` / `#10b981`)
  - `Quality / Score`: `green` (`green` / `#22c55e`)
  - `Universal AI Agents`: `blue` (`#4285F4`)

### Generic Badge Suite Schema
```markdown
[![npm version](https://img.shields.io/npm/v/<package-name>.svg?style=for-the-badge&color=0284C7&logo=npm)](https://www.npmjs.com/package/<package-name>)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg?style=for-the-badge)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/<Ecosystem>-<Tier>-purple.svg?style=for-the-badge)](<ecosystem-link>)
[![Compatibility](https://img.shields.io/badge/Agents-<Agent1>%20|%20<Agent2>%20|%20<Agent3>-orange.svg?style=for-the-badge)](SKILL.md)
[![RTL Native Arabic](https://img.shields.io/badge/RTL-Native%20Arabic-emerald.svg?style=for-the-badge)](README.ar.md)
[![Architect Score](https://img.shields.io/badge/Architect%20Score-8%2F8%20Pass%20(100%25)-green.svg?style=for-the-badge)](#-governance--quality-bar)
[![AI Agents Compatible](https://img.shields.io/badge/AI%20Agents-Universal%20Compatibility-4285F4.svg?style=for-the-badge)](SKILL.md)
```

