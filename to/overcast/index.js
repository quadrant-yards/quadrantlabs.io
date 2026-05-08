// Sync, no network. platform: 'ios' | 'web'
//   ios — https://overcast.fm/+itunes{ID}  opens Overcast app; 404 on desktop
//   web — https://overcast.fm/itunes{ID}   show page in browser; login wall but functional
function toOvercastURL(applePodcastsURL, platform) {
  const match = new URL(applePodcastsURL).pathname.match(/\/id(\d+)/);
  if (!match) throw new Error(`No iTunes ID found in: ${applePodcastsURL}`);
  const id = match[1];
  return platform === 'ios'
    ? `https://overcast.fm/+itunes${id}`
    : `https://overcast.fm/itunes${id}`;
}

// Async. Returns { web, view, app }:
//   web  — show page in browser
//   view — universal link; opens Overcast app on iOS, falls back to web on desktop
//   app  — iOS URL scheme that prompts subscription (requires iTunes API fetch for feed URL)
async function toOvercastURLs(applePodcastsURL) {
  const match = new URL(applePodcastsURL).pathname.match(/\/id(\d+)/);
  if (!match) throw new Error(`No iTunes ID found in: ${applePodcastsURL}`);
  const id = match[1];

  const res = await fetch(`https://itunes.apple.com/lookup?id=${id}`);
  const data = await res.json();
  const feedUrl = data.results?.[0]?.feedUrl;
  if (!feedUrl) throw new Error(`No feed URL found for iTunes ID: ${id}`);

  return {
    web: `https://overcast.fm/itunes${id}`,
    view: `https://overcast.fm/+itunes${id}`,
    app: `overcast://x-callback-url/add?url=${encodeURIComponent(feedUrl)}`,
  };
}

if (typeof module !== 'undefined') module.exports = { toOvercastURL, toOvercastURLs };
