# Command: style

Runtime entry point for repository visual styling, badge hierarchy, and Social Preview Open Graph design.

## Dispatch steps

1. Load `../workflows/design-social-preview.md` — visual card and styling workflow.
2. Load `../memory/repo-design-tokens.md` — tokens, aspect ratios, and badge palettes.
3. Load `../rules/content-rules.md` — visual hierarchy rules.
4. Output Open Graph card specification and structured badge snippet.

## Do not

- Do not use non-standard aspect ratios for social preview cards (must be 2:1 / 1280x640).
- Do not overload README with conflicting badge styles.
