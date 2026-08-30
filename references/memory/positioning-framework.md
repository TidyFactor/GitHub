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

- **First Screen Clarity**: Within 3 scrolls, an engineer must see: What it does, 1-line installation, working code sample, and license.

---

## 🏗️ 4. Lifecycle Positioning Taxonomy (Pre-Gen Constraint vs. In-Codebase Production Engine)

When auditing, positioning, or benchmarking tools in the AI-UI ecosystem:

```text
Dimension              Pre-Code Constraint Layer (e.g. VibeCurb)     In-Codebase Production Engine (e.g. Styler)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────
Lifecycle Stage        Pre-generation / Scratchpad prototyping       Post-launch / In-codebase live apps
Primary Job            "Stop agent before writing generic code"       "Surgically refactor live app without breaking it"
Stack Scope            Implicit React/Next.js/Tailwind assumptions   Agnostic: PHP 8, WordPress, Next.js, Vanilla
RTL / Arabic Support   Untouched / Directional LTR defaults          First-class Logical CSS, Bidi, Arabic typography
Quality Gate           Qualitative drift check                       Quantified 7-Axis CDL Rubric (P,H,E,S,R,V,D)
Ecosystem Integration  Single-purpose isolated repository            1 of 12 TidyFactor interoperable skill suites
```

### Strategic Antidotes to Generic AI Output:
1. **Manifesto-First Hook**: Always state the core problem explicitly above the fold (raw LLMs default to statistical mediocrity).
2. **Visual Proof Above The Fold**: Include interactive before/after comparisons demonstrating concrete failure points vs. production polish.
3. **Defensible Wedge**: Lead with multi-framework compatibility and native Arabic/RTL engineering rather than generic aesthetics.

