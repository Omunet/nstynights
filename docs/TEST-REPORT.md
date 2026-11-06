# Test report

Date: 2026-11-06. Local server: `python3 -m http.server -d deploy 8765`. Nothing was deployed.

## Static check — pass, with one media gap

`python3 tools/check_static.py`

- 19 HTML documents.
- Every `/test/` page has `noindex, nofollow`. Root does not.
- Internal links stay under `/test/` or the shared wordmark assets. The only external URL is `https://www.instagram.com/lx.nsty/`.
- No forms, password fields, or inputs.
- Header mark links to `/test/` or `/test/es/` only.
- Language pairs point at the equivalent page and back.
- Wordmark SVG has no upper-line lettering, no `<text>`, and no embedded raster.
- `.htaccess` pattern denies dotfiles and the listed extensions, and allows `/.well-known/`. It does not set HSTS or an HTTPS redirect.
- `robots.txt` disallows `/test`.
- No Kinyxx, ticket-platform, or reference-social host strings in `deploy/`.
- Media gap: the six authorised photographs were not readable, so no `<img>` was emitted for them and the archive poster is not on the home page.

## Browser check — pass

`node tools/browser_check.mjs` against the local server.

| Check | Result |
| --- | --- |
| Console exceptions | none on `/`, `/test/`, FAQ, photos, ES home, access, dress code, contact, legal notice |
| Horizontal overflow | 0 at 1440, 1280, and 390 |
| Broken images | none (only the wordmark is currently referenced) |
| Root | title NSTY, one image, no links, no inputs |
| Mobile menu | button sets `aria-expanded="true"` at 390px |
| FAQ | `<details>` opens from the summary |
| Language | `/test/` → `/test/es/`; `/test/es/` → `/test/` |
| Access and contact | no inputs |

## Not verified here

Apache on the OVH host was not run, so header delivery and the rewrite rules are reviewed as text only. HTTPS was not tested. DNS was not changed.
