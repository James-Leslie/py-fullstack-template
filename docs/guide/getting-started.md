## Configuration

All of your documentation site configuration is stored in the `zensical.toml` file in the root of your project.

## Create your site

### Preview as you write

You can preview your documentation site locally as you write by using the following command:

```bash
uv run zensical serve
```

The site will be available at `http://localhost:8000`.

### Build your site

To build your documentation site for deployment, run:

```bash
uv run zensical build
```

## API reference

Your project's [API reference](../reference/index.md) documentation is automatically generated from your code's docstrings, using `mkdocstrings`.
