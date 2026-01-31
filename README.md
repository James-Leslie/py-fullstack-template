# py-fullstack-template

A batteries-included Python project template for building full-stack applications with FastAPI and Streamlit, optimized for rapid development with Claude AI assistance.

## Why This Template?

Starting a new Python project often means repeating the same setup steps: configuring `pyproject.toml`, setting up project structure, adding common dependencies, and creating context for AI coding assistants. This template eliminates that friction by providing a pre-configured foundation that works out of the box.

**Key benefits:**

- Pre-configured modern Python tooling (UV-ready, proper dependency management)
- Flexible structure supporting API-only, app-only, or full-stack projects
- Claude AI integration via `CLAUDE.md` and custom skills
- Consistent project organization across your work
- Zero-config start for common Python project types

## What's Included

- 📦 **`example_pkg/`** - Core package for shared business logic, models, and utilities
- 🚀 **`api/`** - FastAPI backend application (optional)
- 📊 **`app/`** - Streamlit frontend application (optional)
- 🤖 **`.claude/skills/`** - Custom Claude skills for project-specific assistance
- 📝 **`CLAUDE.md`** - Project context and guidelines for Claude AI
- 🔧 **`pyproject.toml`** - Modern Python dependencies and project configuration
- ✅ **`tests/`** - Test structure ready to go

## Getting Started

### 1. Use This Template

Click the "Use this template" button at the top of this repository to create a new repo from this template.

### 2. Clone and Rename

```bash
git clone https://github.com/yourusername/your-new-project.git
cd your-new-project
```

Rename `example_pkg` to your actual package name:

```bash
mv example_pkg your_package_name
```

Update references in `pyproject.toml` and any imports.

### 3. Install Dependencies

```bash
uv sync
```

### 4. Customize for Your Use Case

**For API-only projects:**

- Delete the `app/` folder
- Focus development in `api/` and `example_pkg/`

**For Streamlit-only projects:**

- Delete the `api/` folder
- Focus development in `app/` and `example_pkg/`

**For full-stack projects:**

- Keep both folders
- Share common logic via `example_pkg/`

### 5. Update Project Context

Edit `CLAUDE.md` with your project-specific information:

- Project goals and scope
- Architecture decisions
- Key dependencies and why they were chosen
- Development conventions

## Running the Applications

**FastAPI:**

```bash
uvicorn api.main:app --reload
```

**Streamlit:**

```bash
streamlit run app/streamlit_app.py
```

## Project Structure Philosophy

The template follows a "shared core" pattern:

- **`example_pkg/`** contains business logic, data models, and utilities that both your API and app can import
- **`api/`** is a thin layer handling HTTP requests/responses
- **`app/`** is a thin layer handling UI and visualization

This separation means you can:

- Test business logic independently of the interface
- Reuse code across multiple interfaces
- Swap out Streamlit for another UI framework without touching core logic
- Add additional interfaces (CLI, scheduled jobs, etc.) easily

## Working with Claude

This template includes Claude AI integration:

1. **`CLAUDE.md`**: Maintains project context, decisions, and conventions
2. **`.claude/skills/`**: Custom skills for project-specific workflows
3. **Dependency documentation**: Clear `pyproject.toml` with commented sections

When working on the project, Claude will automatically reference `CLAUDE.md` for context about your architecture, conventions, and goals.

## Customization Tips

- **Dependencies**: Update `pyproject.toml` with your typical stack
- **Pre-commit hooks**: Add linting/formatting tools
- **CI/CD**: Add GitHub Actions workflows
- **Docker**: Add `Dockerfile` and `docker-compose.yml` if needed
- **Environment variables**: Add `.env.example` for configuration

## Why UV?

This template is optimized for [UV](https://github.com/astral-sh/uv), a fast Python package installer and resolver. UV provides:

- Significantly faster dependency resolution
- Better lock file management
- Improved reproducibility
- Drop-in replacement for pip/pip-tools

You can still use pip if preferred, but UV is recommended for the best experience.

## License

MIT License - feel free to use this template for any purpose.

## Contributing

Found a way to improve this template? PRs welcome! This template evolves based on real-world usage patterns.
