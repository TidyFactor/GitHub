# Command: project

Runtime entry point for GitHub Projects (v2), custom fields, views, roadmaps, and iteration cycles.

## Dispatch steps

1. Load `../workflows/manage-projects.md` — project setup and field design workflow.
2. Load `../memory/maturity-model.md` — project tracking conventions.
3. Configure Project fields (Status, Priority, Size, Iteration) and views (Board, Table, Roadmap).

## Do not

- Do not create disconnected project boards without repository item tracking.
- Do not overload projects with redundant custom fields.
