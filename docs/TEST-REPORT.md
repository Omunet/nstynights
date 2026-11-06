# Test report

Date: 2026-11-06. Local server rooted at `deploy/`. Nothing was deployed.

## Static check — pass

`python3 tools/check_static.py`

- 19 HTML documents.
- Every `/test/` page has `noindex, nofollow`. The root page does not.
- Internal links stay under `/test/` or the shared wordmark assets. The only external URL is `https://www.instagram.com/lx.nsty/`.
- No forms, password fields, or inputs.
- Header mark links only to the preview home in the current language.
- Language pairs point at the equivalent page and back.
- Wordmark SVG has no upper-line lettering, no text element, and no embedded raster.
- Home uses the runway, outdoor, backstage, and monochrome frames. The 2025 poster is only on the photos archive.
- Dress code uses four photographs. The photos page has six figures (five looks plus the archive poster).
- Audit phrasing from the previous draft is gone from the HTML.
- `.htaccess` denies dotfiles and the listed extensions, allows `/.well-known/`, and does not set HSTS or an HTTPS redirect.

## Browser check — pass

`node tools/browser_check.mjs`

| Check | Result |
| --- | --- |
| Console exceptions | none on root, both homes, FAQ, photos, access, dress code, contact, legal notice |
| Horizontal overflow | 0 at 1440, 1280, and 390 |
| Broken images | none. Home has 5 images (mark plus four photographs). Photos has 7 (mark plus six frames). |
| Root | title NSTY, one image, no links |
| Mobile menu | `aria-expanded` becomes true at 390px |
| FAQ | the first details element opens |
| Language | `/test/` links to `/test/es/` and back |

## Metadata

A shipped JPEG (`runway-800.jpg`) has no EXIF, GPS, IPTC, or XMP. Only file-type and JFIF structure remain.

## Not verified on the host

Apache on the OVH machine was not executed, so header delivery is reviewed as configuration text. HTTPS was not tested. DNS was not changed.
