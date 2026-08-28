# AGENTS.md — TidyFactor GitHub Skill Governance

This file governs the behavior of all AI Coding Agents (*Google Antigravity, Claude Code, Cursor, Codex, Windsurf*) working within the `tidyfactor-github` skill.

---

## 🏛️ Non-Negotiable Governance Rules

1. **Dispatcher Discipline**: `SKILL.md` is strictly a router (~340 tokens). All domain logic and workflows live under `references/`.
2. **One Workflow = One Outcome**: Every workflow in `references/workflows/` ends with a mandatory `## Validation checklist`.
3. **Operational Memory**: All memory files under `references/memory/` contain pure facts, schemas, and catalogs with `<!-- last-verified: 2026-08-29 -->`.
4. **Prioritized Rules**: All rule files in `references/rules/` rank violations by impact (`CRITICAL` -> `HIGH` -> `MEDIUM` -> `LOW`) with code/config examples.
5. **Triple Execution Modes & Safety Gate**: Default to `AUDIT` (read-only) or `PLAN` (dry-run). Never execute destructive actions (repo deletion, branch force push, admin elevation, visibility change) without explicit user confirmation in `APPLY` mode.
