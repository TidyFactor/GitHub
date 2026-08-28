# Command: brief

Runtime entry point for strategic repository and organization discovery (Contextual Decision Layer).

## Dispatch steps

1. Load `../workflows/brief-discovery.md` — the single-round interview protocol.
2. Load `../memory/decision-points.md` — the decision parameters and caching schema.
3. Check if `.tidyfactor/github-brief.md` already exists in the project root. If present, load cached decisions silently unless the user explicitly requested a reconfiguration.
4. If missing, execute the brief discovery workflow and write `.tidyfactor/github-brief.md`.

## Do not

- Do not re-interview the user for downstream commands (`/audit`, `/readme`, `/action`) when `.tidyfactor/github-brief.md` exists.
- Do not ask more than 3 questions in a single round.
