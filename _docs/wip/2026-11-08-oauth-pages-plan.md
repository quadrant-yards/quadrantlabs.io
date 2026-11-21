# Plan: Agents OAuth home page, privacy policy, and terms

Brief: [2026-11-08-oauth-reqs.md](2026-11-08-oauth-reqs.md)

## Decisions (Nov 21, 2026)

- **Generic name only.** The public pages, paths, titles, and copy use the generic name **Agents** ("Quadrant Agents" where a full name is needed). The assistant's old internal name does not appear on the site or in this repo.
  - The consent screen app name has to match the home page, so **Sam renames the OAuth app** on the Google Cloud Branding page from its old internal name to `Quadrant Agents`. Do this in the same edit that adds the URLs.
- **Retention (corrected Nov 21, 2026 after PR #1 review):** conversation history can include Gmail and Calendar content and is kept until the operator deletes it, along with related assistant memory and indexes. Users can ask for deletion at apps@quadrantlabs.io, with no deletion deadline promised. Operational logs are kept up to 7 days, and security and audit metadata up to 30 days. Do not claim encryption at rest for history or tokens; neither is verified.
- **OAuth credentials:** refresh tokens are stored on a private server with access restricted to the service account, and access tokens are held in memory. **Gate:** the policy's credentials paragraph must be checked against the Quadrant Agents OAuth implementation once it is configured, before merging.
- **Contact:** apps@quadrantlabs.io on every page.
- **Model providers:** yes. Content is sent to an AI model provider only to answer the user's request. The Sharing section says so.
- **Terms of service:** include them.
- **Effective date:** Nov 1, 2026, on all three pages.

## What the site looks like today

- Plain static HTML on GitHub Pages from `main`. No Jekyll layouts or includes. The root `index.html` is a single image.
- `brand/tokens.css` and `brand/base.css` are generated, shared stylesheets with Clear Day colors, dark mode, Jost and Plex fonts. New pages can link them as-is.
- There is no nav or footer anywhere, so there's no footer pattern to extend. **No footer link will be added.**
- `CNAME` is `www.quadrantlabs.io`. The apex `quadrantlabs.io` 301-redirects to `www`. The canonical URLs are therefore on `www`. Google accepts this: the authorized domain is `quadrantlabs.io`, and that covers `www`.
- The repo has no `apps/` directory yet. The only earlier tool page was `to/overcast/`, now removed.

## Paths

| Page | File | URL |
|---|---|---|
| Home | `apps/agents/index.html` | `https://www.quadrantlabs.io/apps/agents/` |
| Privacy | `apps/agents/privacy/index.html` | `https://www.quadrantlabs.io/apps/agents/privacy/` |
| Terms | `apps/agents/terms/index.html` | `https://www.quadrantlabs.io/apps/agents/terms/` |

Folder-per-page with `index.html` gives clean trailing-slash URLs and doesn't depend on GitHub Pages serving `.html` files without the extension.

## Page design

All three pages share the same minimal shell:

- `<link>` to `/brand/tokens.css` and `/brand/base.css`, plus the same Google Fonts link the brand guide uses. Favicon `/brand/assets/favicon.svg`.
- Small app bar per the brand guide's Products rules: outline mark (16 to 20px, `primary`), then the product name.
- One narrow column (`--q-measure`), 16px side gutter, readable on a phone.
- `<title>`: `Quadrant Agents` for home, `Privacy policy · Quadrant Agents` and `Terms of service · Quadrant Agents` for the others.
- Voice: plain and specific, sentence-case headings, no nautical flourishes. Dates written like "Nov 8, 2026".

**App name on the page.** Google checks that the home page names the app the same way as the consent screen. The pages say **Quadrant Agents**, and Sam renames the consent screen app to match (see Decisions).

## Content

**Home page** (about 4 sentences):
- Quadrant Agents is a private assistant tool run by Quadrant Labs for one household user. It is not offered to the public.
- What it does, in one line: it lets the user's assistant read their Gmail and manage their Google Calendar when they ask.
- Links to the privacy policy and terms.
- Contact: apps@quadrantlabs.io.

**Privacy policy** sections, in this order:
1. Who operates it: Quadrant Labs, apps@quadrantlabs.io
2. Google data it accesses: Gmail (read-only), Calendar events (view and edit), calendar list (read-only), basic account info (email address)
3. Why: so the user's assistant can read email and manage calendar events when the user asks
4. Sharing: not sold, not used for ads, not shared with third parties except as needed to provide the feature. Content is sent to an AI model provider only to answer the user's request.
5. Storage: OAuth tokens stored encrypted on a private server
6. Storage and retention: conversation history, logs, and OAuth credentials as described in Decisions
7. Revoking access: link to https://myaccount.google.com/permissions
8. Limited Use statement, verbatim from the brief, with the link
9. Effective date: Nov 1, 2026

**Terms of service** (short):
1. What it is: a private tool for one household user, not offered to the public
2. Provided as is, with no warranty
3. The user's use of Google services stays subject to Google's own terms
4. Access can be revoked at any time (link to https://myaccount.google.com/permissions)
5. Changes to these terms will be posted on this page
6. Contact: apps@quadrantlabs.io
7. Effective date: Nov 1, 2026

Not on any page: the old internal app name, personal email addresses, server hostnames, the GCP project ID, client IDs, or secrets.

## Steps

1. Branch from `main`: `agents-oauth-pages`.
2. Add `apps/agents/index.html`, `apps/agents/privacy/index.html`, and `apps/agents/terms/index.html`.
3. Check them locally (`python3 -m http.server`): light mode, dark mode, phone width, links work.
4. Grep the new files for leaked identifiers (the old internal app name case-insensitive, the GCP project ID, `googleusercontent`, hostnames, any address other than apps@quadrantlabs.io).
5. Confirm `python3 _scripts/brand/build.py --check` still passes, which shows `brand/` was not touched.
6. Commit and open a PR to `main`. Merging deploys.
7. After the merge, `curl` all three URLs to confirm 200 over HTTPS, and confirm the apex URLs redirect to them.
8. Report the final URLs. Sam then does the Google Cloud Branding and Audience steps from the brief, renames the app to `Quadrant Agents`, and adds the terms URL.

## Open questions for Sam

None. All answered on Nov 21, 2026 (see Decisions).
