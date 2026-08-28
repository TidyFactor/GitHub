# Workflow: automate-release

One outcome: an atomically synchronized SemVer release with updated CHANGELOG.md, version tags, and build bundles.

## Steps

1. Validate working tree clean state (`git status --porcelain`).
2. Determine new SemVer bump (`MAJOR`, `MINOR`, or `PATCH`).
3. Update metadata files atomically:
   - `package.json` (`"version": "x.y.z"`)
   - `.tidyfactor` (`"version": "x.y.z"`)
   - `brand.json` (`"version": "x.y.z"`)
   - `CHANGELOG.md` (add dated release entry with Added, Changed, Fixed sections).
4. Run validation tool (`python tools/validate_skill.py`).
5. Run build and sync tool (`node tools/build-skill.js`).

## Validation checklist

- [ ] All 3 JSON metadata files have identical `"version"` values
- [ ] `CHANGELOG.md` contains an entry for the target version
- [ ] `python tools/validate_skill.py` exits with code 0
- [ ] Distribution archive and versioned archive created in `dist/`
