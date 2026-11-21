# Brief: Publish OAuth home page and privacy policy on quadrantlabs.io

## Goal

Publish two small public pages on `quadrantlabs.io` so the Google OAuth app for the household assistant (now **Quadrant Agents**) can move from Testing to Production. Google won't enable **Publish app** until the app's Branding page has a home page and a privacy policy link on an authorized domain.

## Deliverables

1. **Home page**, for example `https://quadrantlabs.io/apps/agents/`
2. **Privacy policy**, for example `https://quadrantlabs.io/apps/agents/privacy`
3. Optional, only if Sam asks: **Terms of service** at `https://quadrantlabs.io/apps/agents/terms`

Pick paths that fit the existing site structure. Both pages must:

- load over HTTPS on `quadrantlabs.io` itself, not a subdomain or a third-party host
- be public, with no login
- stay small and plain, matching the site's existing style

Report back with the final URLs.

## Page content

**Home page.** A few sentences: Quadrant Agents is a private assistant tool run by Quadrant Labs for one household user. It is not offered to the public. Link to the privacy policy. Contact: sam@quadrantlabs.io.

**Privacy policy.** It must cover these points:

- **Who:** operated by Quadrant Labs. Contact: sam@quadrantlabs.io.
- **What Google data it accesses:**
  - Gmail, read-only
  - Google Calendar events, view and edit
  - the user's calendar list, read-only
  - basic account info (email address)
- **Why:** to let the user's personal assistant read email and manage calendar events when the user asks.
- **Sharing:** Google user data is not sold, not used for advertising, and not shared with third parties except as needed to provide the feature.
- **Storage:** OAuth tokens are stored encrypted on a private server.
- **Revoking access:** users can revoke access at any time at https://myaccount.google.com/permissions.
- **Required statement, verbatim:** "Quadrant Labs' use and transfer of information received from Google APIs will adhere to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements."
- **Effective date:** the date of publishing.

**For Sam to confirm before publishing:** how long, if at all, email or calendar content is kept after the assistant uses it. Don't invent a retention period. Leave a clear placeholder and ask.

## Constraints

- Work only in repositories in the `quadrant-yards` GitHub organization.
- Keep these out of the pages: personal email addresses, server hostnames, project IDs, client IDs, and any secrets.
- Don't change the rest of the site beyond adding these pages, plus a footer link only if the site already has a pattern for one.
- Commit on a branch and open a PR unless the site's repo says otherwise.

## Afterwards (Sam does this, not the agent)

On the Google Cloud **Branding** page for the app's project:

1. Fill in the home page and privacy policy URLs.
2. Add `quadrantlabs.io` under Authorized domains.
3. Save.
4. On **Audience**, click **Publish app**.

Then follow step 4 of the Google access check doc (kept outside this repo) so the assistant approves access again.
