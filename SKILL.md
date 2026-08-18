---
name: homepage-jekyll
description: Jekyll homepage maintenance for content, configuration, and publishing workflows.
---

# Homepage repo skill file

This repository is a Jekyll-based website (al-folio theme).  
Use this as the default operating guide for edits and troubleshooting.

## Scope

Use Jekyll-native workflows for this repo unless the user asks for an alternative build system.

- Local content lives in Markdown/Liquid files under `_pages`, `_posts`, `_projects`, `_news`, `_layouts`, `_includes`, and `_data`.
- Styling and assets are in `_sass`, `assets`, and image/data directories.
- `_site` is generated output and should not be edited manually.
- Keep generated artifacts out of source edits unless explicitly requested.

## Common task patterns

### Local content updates

- Add or edit pages in `_pages/`.
- Add blog posts in `_posts/` using `YYYY-MM-DD-title.md`.
- Add projects in `_projects/` and news items in `_news/`.
- Update global metadata, plugin options, and URL behavior in `_config.yml`.
- Update publication metadata in `_bibliography/papers.bib`.
- Keep YAML front matter consistent (for example: `layout`, `title`, `date`, `permalink` as needed).

### Build and serve

- Install Ruby deps with `bundle install`.
- Start local preview with `bundle exec jekyll serve --livereload`.
- Build the site with `bundle exec jekyll build`.
- For GitHub Pages workflows, verify `_config.yml` and base URL settings before deploying.

### Safety rules

- Do not edit generated files under `_site` as source of truth.
- Do not remove or rename plugin/theme directories unless requested.
- Preserve existing front matter keys used by the theme (for example image, description, tags, categories, and collection metadata).
- Run formatting or dependency changes only when explicitly requested.

## Jekyll-focused best practices

- Use consistent naming and date conventions for posts.
- Keep new content minimal in diffs: small, isolated edits per task.
- Prefer existing layout patterns before creating new templates.
- If a page build fails, start by checking `_config.yml` syntax and front matter formatting.
