---
description: Run full quality check suite (format, lint, types, tests)
---

Run a complete quality check of the codebase in this order:

1. Check Python formatting: `uv run ruff format --check .`
2. Check Python linting: `uv run ruff check .`
3. Run type checking: `uv run ty check`
4. Run tests with coverage: `uv run pytest`

Report all issues found. If any checks fail, explain what needs to be fixed before committing.
