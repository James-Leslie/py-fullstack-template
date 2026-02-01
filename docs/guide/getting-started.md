# Getting Started

## Installation

```bash
uv sync
```

## Running the Applications

### FastAPI Backend

```bash
uv run fastapi dev api/main.py
```

The API will be available at `http://localhost:8000`.

### Streamlit Frontend

```bash
uv run streamlit run app/app.py
```

The app will be available at `http://localhost:8501`.

## Project Structure

- `example_pkg/` - Core package with shared business logic
- `api/` - FastAPI backend application
- `app/` - Streamlit frontend application
- `tests/` - Test suite
