# Workflow: brief-discovery

One outcome: a verified baseline brief written to `.tidyfactor/github-brief.md` via a single-round interview.

## Steps

1. Check if `.tidyfactor/github-brief.md` already exists.
   - If present and no re-brief requested: load settings and exit workflow silently.
2. If missing, evaluate repository files (e.g. `package.json`, `composer.json`, `pyproject.toml`, `.github/`).
3. Formulate max 3 unresolved multiple-choice questions:
   - Target Scope & Governance Level (`personal-public`, `org-public-oss`, `org-private-enterprise`).
   - Project Archetype (`library`, `saas-app`, `cli-tool`, `docs-portal`).
   - Bilingual Preference (`en-only`, `bilingual-ar-en`).
4. Write confirmed answers to `.tidyfactor/github-brief.md`.

## Validation checklist

- [ ] `.tidyfactor/github-brief.md` is created in project root
- [ ] No more than 3 questions were asked in the interview round
- [ ] File contains `project_type`, `scope_tier`, `governance_level`, and `bilingual_mode`
- [ ] File contains `<!-- last-verified: YYYY-MM-DD -->` date
