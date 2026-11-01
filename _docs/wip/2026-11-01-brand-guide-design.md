# Quadrant brand / style guide — design doc

Status: **v1.0.0 live** at https://www.quadrantlabs.io/brand/ (merged 2026-11-01) · Started 2026-11-01

## Goal

One brand guide for everything in the `quadrant-yards` org, usable equally by
human designers and AI agents. An agent working in any Quadrant repo should be
able to fetch one URL and produce on-brand UI, copy, and assets without asking.

## Decisions so far

| # | Decision | Choice |
|---|----------|--------|
| 1 | Scope | **Umbrella + products.** Quadrant Labs is the core brand. Product UIs (quadrant-planner, trip-split, bookrec, metronome, …) inherit shared tokens, type and voice. Shared palette (see #7). |
| 2 | Palette approach | **Fresh start.** The v1 navy/brass palette and the homepage watercolor palette were treated as exploration only. |
| 3 | Home | **Served publicly from this repo** at `quadrantlabs.io/brand/`. |
| 4 | Voice | **Quiet craftsman.** Plain, precise, warm, lightly nautical. Few words, no hype. |
| 5 | Palette | **B1 Clear Day** (Slack Water family), chosen 2026-11-01 after 4 rounds. See Palette below. |
| 6 | Product naming | **Plain name + small "Quadrant".** e.g. "Planner · Quadrant": the app's own name leads, the mark and a small "Quadrant" sign it. |
| 7 | Product color | **Shared palette, no per-app accents.** Every app uses Clear Day as-is; apps differ by name and content, not color. (Supersedes the "own accent" idea in #1.) |
| 8 | Typography | **T1 Engineered:** Jost headings + IBM Plex Sans (body and UI) + IBM Plex Mono. Chosen 2026-11-01. See Typography below. |

### Carried forward (not reopened)

- **Mark:** the fan-sector mark from the Hartge Quadrant sloop (now `brand/assets/`; the old `public/mark.svg` was removed 2026-11-01).
  Outline as primary; filled variant for favicon/avatar only.
- **Wordmark:** Jost 400, uppercase, tracked +0.16em.
- **Origin story:** Hartge Yacht Yard, Galesville MD; Quadrant sloop, 1956.
  The navigation instrument (a quadrant) supports the "find your bearings" idea.

## Palette — B1 Clear Day (locked)

The Chesapeake on a bright, windy afternoon: clear bay water, summer marsh, one
signal-orange channel buoy. Source exploration: `_docs/brand/palette-exploration-b.html`.

| Token | Role | Light | Dark |
|-------|------|-------|------|
| `paper` | Page background | `#F6F7F3` Spray | `#0B1615` |
| `surface` | Cards, panels, inputs | `#FFFFFF` | `#112120` |
| `ink` | Body text, headings | `#10211F` Deep Channel | `#E8F0EC` |
| `muted` | Secondary text | `#4E5E59` | `#94A8A2` |
| `border` | Rules, outlines | `#DCE2DC` | `#20332F` |
| `tint` | Subtle fills, focus halo, chips | `#DDEEE9` | `#173230` |
| `primary` | Brand color as text/outline (links, ghost buttons, focus) | `#0B5E5A` Bay Water | `#5FCFC3` |
| `fill` / `on-fill` | Primary buttons, bars, solid brand areas | `#0B5E5A` / `#FFFFFF` | `#0F716C` / `#FFFFFF` |
| `accent` | Emphasis and warnings **as text** | `#B8410E` | `#FF8A4C` |
| `signal` / `on-signal` | Vivid buoy orange **as a fill only** (badges, alerts, highlights) | `#EE6A2A` / `#10211F` | `#EE6A2A` / `#10211F` |
| `secondary` | Second data series, marsh accents | `#6E8F2E` Summer Marsh | `#9DBE5A` |

Rules:
- **Fill vs. text.** Every brand color has a fill shade and a text shade. Vivid
  fills get whichever text passes contrast (white on Bay Water, Deep Channel on
  orange). Never set `signal` orange as text; use `accent`.
- **Orange is scarce.** One signal per view: the thing that needs attention.
  Bay Water carries the brand; orange is the buoy, not the water.
- All text pairs above meet WCAG AA (≥ 4.5:1); checked 2026-11-01.

## Typography — T1 Engineered (locked)

Source exploration: `_docs/brand/type-exploration.html`. All fonts free on Google Fonts.

| Role | Font | Weights | Fallback |
|------|------|---------|----------|
| Wordmark | Jost, uppercase, tracked +0.16em | 400 | (always use the SVG asset) |
| Headings | Jost | 500 | `'Helvetica Neue', Arial, sans-serif` |
| Body + UI | IBM Plex Sans | 400 text · 500 labels/buttons · 600 strong UI emphasis | `system-ui, sans-serif` |
| Code | IBM Plex Mono | 400 · 500 | `ui-monospace, Menlo, monospace` |

Scale (rem, 16px base, ~1.25 ratio):

| Token | Size | Line height | Use |
|-------|------|-------------|-----|
| `display` | 3rem / 48px | 1.1 | Homepage hero only |
| `h1` | 2.375rem / 38px | 1.12 | Page titles |
| `h2` | 1.875rem / 30px | 1.2 | Section titles |
| `h3` | 1.5rem / 24px | 1.25 | Subsections, card titles on marketing pages |
| `h4` | 1.25rem / 20px | 1.3 | App panel titles |
| `body` | 1rem / 16px | 1.6 | Paragraphs (max ~68ch) |
| `ui` | 0.875rem / 14px | 1.4 | Buttons, inputs, tables, nav |
| `small` | 0.8125rem / 13px | 1.45 | Captions, hints, metadata |
| `kicker` | 0.75rem / 12px, Plex 500, uppercase, +0.14em | 1 | Eyebrow labels above headings |

Rules:
- Headings: Jost 500, letter-spacing −0.005em, sentence case. Never all-caps headings;
  tracked caps belong to the wordmark and kickers only.
- Numbers in tables, prices and metrics: `font-variant-numeric: tabular-nums`.
- No weight above 600. No italics for emphasis in UI; use 500/600.
- Inline code: Plex Mono at 0.875em on a `tint` background.
- Not used: soft display serifs (Fraunces, Instrument Serif, Playfair), Inter.
  (A serif for long-form was considered, T3, and not adopted.)

## Proposed structure of the published guide

```
brand/
  index.html        human-readable guide (visual, with examples)
  llms.txt          agent-readable guide: same rules, plain text, imperative
  tokens.css        CSS custom properties (--q-*), light + dark
  base.css          optional element defaults + .q-* component classes
  tokens.json       same tokens, for non-CSS tools
  assets/           mark (3 colors), horizontal logo (2), favicon, app icon
```

- `index.html` and `llms.txt` are generated from, or kept in sync with, one
  source of truth (tokens + rules). How to enforce sync is an open decision.
- Agent file uses `.txt`, not `.md`: GitHub Pages runs
  `jekyll-optional-front-matter`, which may render `.md` files to HTML instead
  of serving them raw. Files without front matter (`.txt`, `.css`, `.json`, `.svg`,
  and our `index.html`) are copied as-is. Confirm after deploy (see Still open).
- Product repos reference it from their `CLAUDE.md` / `AGENTS.md` with one line,
  e.g. "Follow https://quadrantlabs.io/brand/llms.txt for all UI and copy."

## Guide contents (outline)

1. Principles — 3–5 short rules that resolve ambiguity
2. Logo — mark, lockups, clear space, minimum size, misuse
3. Color — core neutrals, primary, accent, product accents, dark mode, contrast rules
4. Typography — display / body / mono, scale, usage
5. Layout & components — spacing scale, radius, borders, shadows, buttons, inputs
6. Illustration & imagery — when watercolor/illustration is used, and when it isn't
7. Voice & writing — tone, word list, before/after examples, UI microcopy
8. Product sub-branding — how an app names itself, picks an accent, uses the mark
9. For agents — checklist and "do / don't" in machine-friendly form

## Open decisions

- [x] Palette direction → **B1 Clear Day**. History:
  - Round 1 (`_docs/brand/palette-exploration.html`): A Boatyard / B Slack Water / C Chart Room.
    Sam leans **A**, but it reads as "generic AI" (cream paper + terracotta + warm greys).
  - Round 2 (`_docs/brand/palette-exploration-a.html`): A1 Brightwork (dark-first mahogany/varnish),
    A2 Livery (white topsides, navy boot stripe, red bottom paint), A3 Workshop (primer grey, mahogany, cool Bay-blue accent).
  - Principle from this round, regardless of winner: avoid the AI-default look in type, motif,
    copy and contrast, not just color. Add an explicit "don't" list to the guide.
  - Sam picked **A2 Livery**, but its dark mode felt off. Cause: the red was lightened into coral
    (also used as button fill), the boot stripe faded, and the background went cool blue.
  - Round 3 (`_docs/brand/palette-a2-dark.html`): D1 Split red / D2 Navy hull / D3 Black hull.
  - New rule regardless of pick: **fill red vs. text red.** Deep red for solid areas with white
    text on it; a lighter red only for red text on dark. Never use the light red as a fill.
  - Sam then switched back to **B Slack Water** (A2 dark-mode question left open). Concern: B is
    a little muted. Cause: primary #2B5552 is dark and greyed (33% sat / 25% light), paper is
    grey-green, and the orange was darkened in round 1 to pass contrast.
  - Round 4 (`_docs/brand/palette-exploration-b.html`): B1 Clear Day (same structure, saturated),
    B2 Blue Crab (claw blue + shell olive + red claw tip), B3 Day Marker (B's calm neutrals,
    buoy orange as the bold action color).
  - Generalized rule: each brand color has a **fill** shade and a **text** shade; vivid fills
    get whichever text color passes contrast (dark text on orange, white on blue/teal).
- [x] Body + mono typefaces → **T1 Engineered** (decision #8)
  - Exploration: `_docs/brand/type-exploration.html`, all in Clear Day.
    T1 Engineered (Jost headings + IBM Plex Sans/Mono), T2 Hull Lettering (Archivo wide
    headings + Archivo + JetBrains Mono), T3 Logbook (Jost headings + Source Serif 4 long-form
    + Source Sans 3 UI + Source Code Pro).
  - Ruled out: soft display serifs (Fraunces, Instrument Serif, Playfair) and Inter, as AI-default.
- [x] Homepage watercolor → repainted in Clear Day on 2026-11-01 (see Still open).
- [x] Sync strategy → **generated.** `_scripts/brand/brand.toml` is the single source;
  `_scripts/brand/build.py` (stdlib only) writes `brand/index.html`, `llms.txt`, `tokens.css`,
  `base.css`, `tokens.json` and `assets/*.svg`, and fails the build if any text color drops
  below WCAG AA. `--check` verifies `brand/` is current. The wordmark is outlined once from
  Jost via `outline_wordmark.py` (needs fonttools) into `wordmark.json`.

## Still open (after v1.0.0)

- [ ] Pronoun on the consulting site: "I" (sole practitioner) or "we"? The voice example uses "I".
- [ ] Policy on AI-generated imagery (guide currently says nothing either way).
- [x] Repaint the homepage watercolor in Clear Day (done 2026-11-01): `public/quadrant-sloop.svg`
      recolored (teal sky and water, marsh shore, white sails, Deep Channel boot stripe, one orange
      channel buoy, whitecaps for wind). Page is flat `paper` with dark mode, no gradient or shadow.
      Favicon now `brand/assets/favicon.svg`; `public/mark.svg` (v1 navy) deleted. Guide's "known
      exception" replaced with a pointer to the homepage as the illustration reference.
- [ ] Social card / OG image template in Clear Day.
- [x] After deploy: `llms.txt` is served as `text/plain` (checked 2026-11-01). Guide URLs use
      `www.quadrantlabs.io`, the canonical host; the bare domain 301-redirects there.
- [ ] Optional: CI or pre-commit hook running `build.py --check`.
- [x] Product accent set → none (decision #7)
- [x] Product naming → decision #6
