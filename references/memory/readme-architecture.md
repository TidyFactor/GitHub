# README Architecture & Developer UX Hierarchy

<!-- last-verified: 2026-08-29 -->

Structured blueprint for writing high-converting, developer-first README documents.

---

## 1. The 8-Stage Reading Progression

```text
1. Header & Identity     → Logo + Name + One-line positioning
2. Proof & Badges        → Max 5 status badges + Bilingual switcher
3. Above-the-Fold Value  → 2-sentence summary + 3-line Quick Start code
4. Visual / Architecture → ASCII diagram or clear component breakdown
5. Command / Feature API → Scannable table of commands / capabilities
6. Developer Workflows   → Step-by-step usage guide & examples
7. Governance & Quality  → Rulesets, testing, and contribution links
8. Footer & License      → License notice and brand attribution
```

---

## 2. Structural Section Checkpoints

- **Quick Start Rule**: Must require $\le 3$ commands to run or test locally.
- **Table of Commands**: Must format capabilities in Markdown tables rather than giant bullet lists.
- **Deep Reference Folding**: Deep technical specifications or long configs must use `<details><summary>Detailed Reference</summary>...</details>`.
- **RTL Support**: Arabic README (`README.ar.md`) must wrap content in `<div align="center" dir="rtl">` header and maintain right-to-left flow.
- **Standard Organization & License Footer**: README must conclude with a clear Organization/Support section (Website, Docs, Contact channels) and a formal open-source License attribution block.

