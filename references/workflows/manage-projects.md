# Workflow: manage-projects

One outcome: a structured GitHub Projects (v2) configuration with standard fields and views.

## Steps

1. Define Project Fields:
   - `Status` (`Backlog`, `Ready`, `In Progress`, `In Review`, `Done`).
   - `Priority` (`P0`, `P1`, `P2`, `P3`).
   - `Estimate / Size` (`XS`, `S`, `M`, `L`, `XL`).
   - `Iteration / Sprint` (2-week cadence).
2. Configure Project Views:
   - **Sprint Board**: Kanban grouped by Status.
   - **Backlog Table**: Grouped by Priority and Area.
   - **Roadmap View**: Time-series timeline grouped by Milestone.
3. Link project to repositories and setup auto-add workflow for new issues.

## Validation checklist

- [ ] Project schema includes Status, Priority, and Size fields
- [ ] Views are partitioned logically (Board, Table, Roadmap)
- [ ] Auto-add automation is configured for target repositories
