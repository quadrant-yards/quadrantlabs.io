# quadrantlabs.io

Static site deployed on GitHub Pages from the root of `main`.

## Directory convention

- Web-served content lives at the root or in non-underscore directories (`public/`, `to/`, etc.)
- `_docs/` — internal notes, planning docs, specs; not served by GitHub Pages
- `_scripts/` — tooling and automation scripts; not served by GitHub Pages

Jekyll ignores directories prefixed with `_`, so they are never published. **Do not add a `.nojekyll` file** — that would remove this protection.

## Brand guide

`brand/` (served at quadrantlabs.io/brand/) is **generated**. Edit `_scripts/brand/brand.toml`,
then run `python3 _scripts/brand/build.py`. `--check` fails if `brand/` is out of date.
Design history: `_docs/wip/2026-11-01-brand-guide-design.md`.
