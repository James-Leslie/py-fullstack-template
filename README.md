# py-fullstack-template

A batteries-included Python project template for building full-stack applications with FastAPI and Streamlit, optimized for rapid development with Claude AI assistance.

## What's Included

- **`example_pkg/`** - Core package for shared business logic, models, and utilities
- **`api/`** - FastAPI backend application (optional)
- **`app/`** - Streamlit frontend application (optional)
- **`CLAUDE.md`** - Project context and guidelines for Claude AI
- **`tests/`** - Test structure ready to go

## Getting Started

### 1. Create Your Repository

Click "Use this template" at the top of this repository to create a new repo.

### 2. Clone and Rename

```bash
git clone https://github.com/yourusername/your-new-project.git
cd your-new-project
mv example_pkg your_package_name
```

Update references in `pyproject.toml` and any imports.

### 3. Install Dependencies

```bash
uv sync
```

### 4. Customize for Your Use Case

- **API-only**: Delete `app/`, develop in `api/` and your package
- **Streamlit-only**: Delete `api/`, develop in `app/` and your package
- **Full-stack**: Keep both, share common logic via your package

## Running the Applications

**FastAPI:**

```bash
uv run uvicorn api.main:app --reload
```

**Streamlit:**

```bash
uv run streamlit run app/streamlit_app.py
```

## Project Structure

The template follows a "shared core" pattern:

- **`example_pkg/`** contains business logic, data models, and utilities that both your API and app can import
- **`api/`** is a thin layer handling HTTP requests/responses
- **`app/`** is a thin layer handling UI and visualization

This separation means you can test business logic independently, reuse code across interfaces, and add new interfaces (CLI, scheduled jobs) without touching core logic.

## License

MIT License - feel free to use this template for any purpose.
