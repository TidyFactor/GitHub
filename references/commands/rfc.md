# Command: rfc

Runtime entry point for Request for Comments (RFC) and Architecture Decision Records (ADR).

## Dispatch steps

1. Load `../workflows/author-rfc-adr.md` — RFC/ADR scaffolding and lifecycle tracking workflow.
2. Load `../../assets/templates/RFC-TEMPLATE.md` and `../../assets/templates/ADR-TEMPLATE.md`.
3. Scaffold new RFC (`docs/rfcs/0000-title.md`) or ADR (`docs/adrs/0000-title.md`).
4. Validate schema against `../../schemas/rfc.schema.json`.

## Do not

- Do not introduce breaking API changes without an approved RFC or linked migration guide.
