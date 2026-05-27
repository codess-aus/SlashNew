# Scaling Guacamole — SlashNew Conf 2026

A 22-chapter responsible / agentic AI talk by **@Codess-Aus**, published as a static MkDocs site and deployed to GitHub Pages.

> Live site: https://codess-aus.github.io/SlashNew/

## Stack

- **MkDocs** + **Material for MkDocs** (theme heavily customized)
- Custom CSS in [docs/stylesheets/extra.css](docs/stylesheets/extra.css) — purple/black brand palette, **no grey text anywhere** (white on black in dark mode, black on white in light mode)
- Mona Sans (web font), falling back to Calibri
- Built-in light / dark toggle in the header
- Responsive grid landing page, hero-image-per-chapter detail pages
- One chapter per image in [docs/assets/](docs/assets/) — 22 in total

## Local development

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000.

## Regenerate the chapter pages

The 22 chapter markdown files in [docs/chapters/](docs/chapters/) are generated from a single source-of-truth script:

```bash
python scripts/build_chapters.py
```

Edit chapter content in [scripts/build_chapters.py](scripts/build_chapters.py) and re-run.

## Build for production

```bash
mkdocs build --strict
```

Output goes to `site/`.

## Deploy

A GitHub Actions workflow ([.github/workflows/deploy.yml](.github/workflows/deploy.yml)) builds and deploys to GitHub Pages on every push to `main`.

One-time setup in the repo:

1. **Settings → Pages → Build and deployment → Source:** `GitHub Actions`.
2. Push to `main`. The workflow handles the rest.

## Accessibility & design notes

- Pure black / pure white body text — never grey — to keep AA+ contrast in both modes.
- Visible focus rings on all interactive elements.
- Hero images carry descriptive `alt` text.
- Grid landing page collapses cleanly down to a single column on mobile.
- Headings use the brand purple in both modes; chosen for AA contrast against both backgrounds.
