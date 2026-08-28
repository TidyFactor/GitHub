# Workflow: optimize-discoverability

One outcome: optimized repository metadata, curated topic tags, and high-converting description.

## Steps

1. Load `references/memory/rdo-matrix.md`.
2. Evaluate current repository name, description, homepage, and topics.
3. Formulate optimized metadata:
   - Description: $\le 120$ characters following the capability formula.
   - Topics: 8 to 12 curated tags covering brand, platform, domain, and stack.
   - Homepage: Verified URL pointing to live documentation or ecosystem portal.
4. Output proposed `gh repo edit` commands or apply with user authorization in `APPLY` mode.

## Validation checklist

- [ ] Topics count is between 6 and 12 tags
- [ ] No generic or forbidden topics included
- [ ] Description is $\le 120$ characters and contains zero fluff
- [ ] Homepage URL is valid and reachable
