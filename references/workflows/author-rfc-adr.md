# Workflow: author-rfc-adr

One outcome: a structured, version-controlled Request for Comments (RFC) or Architecture Decision Record (ADR) document linked to issues and pull requests.

## Steps

1. Load `references/memory/oss-governance-models.md` and `assets/templates/RFC-TEMPLATE.md` or `assets/templates/ADR-TEMPLATE.md`.
2. For an RFC:
   - Scaffold `docs/rfcs/NNNN-feature-name.md` containing Problem, Motivation, Proposed Solution, Alternatives, Breaking Changes, and Security Impact.
   - Validate against `schemas/rfc.schema.json`.
3. For an ADR:
   - Scaffold `docs/adrs/NNNN-decision-title.md` containing Context, Decision, Consequences, and Status (`Proposed`, `Accepted`, `Deprecated`).
4. Link RFC/ADR to relevant GitHub Discussion, Issue, or Tracking Milestone.

## Validation checklist

- [ ] RFC/ADR uses standard zero-gap template structure
- [ ] Alternatives considered and drawbacks explicitly documented
- [ ] Breaking changes and migration paths declared
- [ ] Linked to GitHub tracking issue or PR
