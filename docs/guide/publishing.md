# Publishing Your Documentation

This guide covers deploying your documentation site to GitHub Pages using GitHub Actions.

## Prerequisites

1. Your repository must be hosted on GitHub
2. GitHub Pages must be enabled for your repository

## Setting Up GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Build and deployment**, set **Source** to **GitHub Actions**

## GitHub Actions Workflow

Create `.github/workflows/deploy-docs.yml` in your repository:

```yaml
name: Deploy docs

on:
  push:
    branches:
      - main

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    defaults:
      run:
        shell: bash
    steps:
      - name: Configure GitHub Pages
        uses: actions/configure-pages@v5

      - name: Checkout
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true

      - name: Install Python
        run: uv python install 3.13

      - name: Build docs
        run: uvx zensical build --clean

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: site

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## How It Works

1. **Trigger**: The workflow runs automatically when you push to the `main` branch
2. **Build**: Zensical generates static HTML in the `site` directory
3. **Deploy**: The built site is uploaded and deployed to GitHub Pages

## Viewing Your Site

After the workflow completes, your documentation will be available at:

```
https://<username>.github.io/<repository>/
```

## Local Preview

To preview your documentation locally before publishing:

```bash
uv run zensical serve
```

This starts a development server at `http://localhost:8000`.
