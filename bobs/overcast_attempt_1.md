# Overcast Redirect Tool — Attempt 1 Post-Mortem

## Goal
Build a tool (web page + bookmarklet at `quadrantlabs.io/bobs/podcast`) that converts Apple Podcasts or Spotify URLs into Overcast URLs so you can quickly open a podcast in Overcast.

---

## What We Know About Overcast's URL Format

- `https://overcast.fm/?action=add&url=<encoded_feed_url>` — **the only working URL**. Takes an RSS feed URL and opens/subscribes to the podcast in Overcast. Returns HTTP 200.
- `overcast://x-callback-url/add?url=<encoded_feed_url>` — native iOS scheme version of the same thing.
- `https://overcast.fm/search` — **returns 404**. Does not exist.
- `https://overcast.fm/search?q=<name>` — **returns 404**. Does not exist.
- There is no Overcast URL that accepts an Apple Podcasts ID, Spotify ID, or podcast name directly.

**Conclusion:** To open anything in Overcast, you must have the RSS feed URL. There is no shortcut.

---

## How to Get the RSS Feed URL

### iTunes Lookup API
`GET https://itunes.apple.com/lookup?id=<podcast_id>&entity=podcast`

This works and returns `feedUrl` in the JSON response. Verified with curl — the correct feed URL for `id1666397158` is `https://rss.pdrl.fm/a94982/feeds.megaphone.fm/chameleonscamlikely`.

**But it cannot be called from a browser because:**
1. No `Access-Control-Allow-Origin` header → `fetch()` blocked by CORS.
2. Response has `Content-Disposition: attachment; filename=1.txt` → browser refuses to execute JSONP `<script>` tag injection.

### CORS Proxies (all failed)
- `corsproxy.io` — returns 403: "This domain has been blocked."
- `api.allorigins.win` — returns HTTP 500 / empty body for Apple domains.
- `api.codetabs.com` — empty response.
- `thingproxy.freeboard.io` — empty response.

### The Apple Podcasts Page Itself
`https://podcasts.apple.com/us/podcast/chameleon-scam-likely/id1666397158`

The page HTML **does** embed the feed URL as `"feedUrl":"https://..."` in its server-rendered HTML — confirmed with curl + regex. It appears ~24 times in the 1.2MB page.

Cannot be fetched cross-origin from a static web page (same CORS restrictions). The CORS proxies that were tested also fail for this URL.

**However:** When a bookmarklet runs *on* the Apple Podcasts page, `document.documentElement.innerHTML` should contain the feed URL — no network request needed. This is the most promising approach but was not verified working because the test kept failing and the root cause was not isolated.

---

## What Was Tried (in order)

### Attempt 1: `fetch()` to iTunes API
```javascript
const res = await fetch('https://itunes.apple.com/lookup?id=' + id + '&entity=podcast');
```
**Result:** CORS error. Browser blocks the request.

### Attempt 2: JSONP (script tag injection)
```javascript
const s = document.createElement('script');
s.src = 'https://itunes.apple.com/lookup?id=' + id + '&entity=podcast&callback=' + callbackName;
document.head.appendChild(s);
```
**Result:** `Content-Disposition: attachment` on the iTunes API response causes browsers to not execute the script. Callback never fires.

### Attempt 3: Slug extraction → Overcast search
```javascript
const name = url.match(/\/podcast\/([^\/]+)\/id\d+/)[1].replace(/-/g, ' ');
location.href = 'https://overcast.fm/search?q=' + encodeURIComponent(name);
```
**Result:** `overcast.fm/search?q=...` returns 404. The URL doesn't exist. Nothing happens (or user lands on Overcast 404 page).

### Attempt 4: Bookmarklet reading feedUrl from page DOM
```javascript
var m = document.documentElement.innerHTML.match(/"feedUrl":"([^"]+)"/);
location.href = 'https://overcast.fm/?action=add&url=' + encodeURIComponent(m[1]);
```
**Status:** Theoretically correct — the feed URL is in the HTML. Not confirmed working. May fail if the bookmarklet's execution context doesn't give access to script tag content, or if Apple's page uses a different rendering path in a real browser vs. curl.

---

## What a Working Solution Requires

For **the bookmarklet** (running on an open Apple Podcasts tab): Read `feedUrl` from the page DOM. Should work; needs real-browser verification.

For **the web page** (paste a URL): Requires a backend. Options:
- **Cloudflare Worker** — ~15 lines of JS, free tier, fetches iTunes API server-side and re-serves with CORS headers. Cleanest solution.
- **Vercel/Netlify serverless function** — same idea, different platform.
- No purely client-side solution exists.

---

## What to Try Next

1. **Verify the bookmarklet** in a real browser on `podcasts.apple.com`. Open dev tools console and manually run: `document.documentElement.innerHTML.match(/"feedUrl":"([^"]+)"/)` — if it returns a match, the bookmarklet approach works.
2. **Build a Cloudflare Worker** if the web page paste-URL feature is needed.
3. **Consider an iOS Shortcut** for the Messages use case on iPhone (the web page + bookmarklet don't help when a URL arrives in Messages and the user is on mobile).
