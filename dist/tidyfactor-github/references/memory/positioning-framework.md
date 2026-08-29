# Open Source Positioning, Developer SEO & "Why Not?" Boundaries

<!-- last-verified: 2026-08-29 -->

Developer-first positioning rules to maximize clarity and eliminate marketing hyperbole.

---

## 🎯 1. Archetype Classification Matrix

Every project must declare its exact technical archetype:

```text
Archetype       Definition                            Anti-Pattern to Avoid
─────────────────────────────────────────────────────────────────────────────
Library         Focused function/utility set          Claiming to be a "full platform"
Framework       Opinionated architecture + lifecycle  Forcing runtime locks on simple tasks
CLI Tool        Terminal-executable utility           Missing non-interactive `--help` flags
Starter/Kit     Opinionated boilerplate template      Calling it a permanent framework
SDK             Client wrapper for remote APIs        Bundling server-side runtimes
```

---

## 🚫 2. The "Why Not?" & Boundary Protocol

Every production open-source README must include an honest "When NOT to use this" section:

```markdown
## When to Use & When NOT to Use

### Use This If:
- [x] You need zero runtime dependencies.
- [x] You deploy on shared/cPanel or edge environments.
- [x] You require strict SemVer and determinism.

### Do NOT Use This If:
- [ ] You require a heavy distributed microservice mesh.
- [ ] You need a proprietary database lock-in.
- [ ] You are looking for a complete no-code drag-and-drop builder.
```

---

## 🔍 3. Developer Discoverability & SEO Principles

- **Repository Description**: Under 120 characters, mentioning exact language/stack, core mechanism, and primary benefit.
- **Topics**: 5 to 10 curated GitHub topics (e.g. `ai-agents`, `developer-tools`, `cli`, `open-source`, `typescript`).
- **First Screen Clarity**: Within 3 scrolls, an engineer must see: What it does, 1-line installation, working code sample, and license.
