# Provenance and source audit

Built 2026-11-06. No Kinyxx media, copy, marks, ticket platforms, or social links are in `deploy/`.

## Wordmark

- Public mark: `deploy/assets/img/nsty-wordmark.svg` (favicon is the same drawing).
- It is filled SVG paths plus one shared metal gradient and a drop offset. It is not a font, and it does not embed a JPEG or PNG.
- The upper line of the account mark is omitted. The file does not spell that upper line.
- The 150×150 profile JPEG named in the brief (`sha256 e294e2e31611551b0bdf726d4b9b92440f86e26c03c2b11074d0d5d31d98953c`) was not present as a file in this workspace. A public fetch of the Instagram profile returned an error shell, and that fetch was not bypassed.
- The drawing is therefore a geometric reconstruction of the lower NSTY lettering and the lower chevron, made for review. It is not a pixel-overlay trace. Letter shapes need a human check against a high-resolution source.
- Close-up for that review: `/opt/cursor/artifacts/nsty-wordmark-closeup.png` and the SVG beside it.

## Fonts

Self-hosted WOFF2, SIL Open Font License 1.1, downloaded at build time from Fontsource packages and stored in `deploy/test/assets/fonts/`:

| Family | Package | Use |
| --- | --- | --- |
| Big Shoulders Display | `@fontsource/big-shoulders-display@5.2.5` | Headings |
| Barlow Condensed | `@fontsource/barlow-condensed@5.2.5` | Navigation |
| Outfit | `@fontsource/outfit@5.2.5` | Body |

`OFL.txt` in that directory is the license. The preview does not request a font CDN.

## Photographs

Jonathan (t175u, 2026-11-06) authorised reuse of posts authored or co-authored by `@lx.nsty`. Tagged-only posts stay out. The supplied provenance list was:

| File | Post | Credit / co-authors | Placement |
| --- | --- | --- | --- |
| `nsty-ig-01-DL3a1nkodkW.jpg` | `https://www.instagram.com/lx.nsty/p/DL3a1nkodkW/` | Photo credit @nyxianyx. Author lx.nsty. | Dated archive only. Printed 2025 lines are not a future schedule. |
| `collab-02-rayn.nyx-DNL0neeiqpj.jpg` | `https://www.instagram.com/rayn.nyx/p/DNL0neeiqpj/` | rayn.nyx and lx.nsty | Home, gallery, dress-code draft |
| `collab-03-rayn.nyx-DKttbxziMY8.jpg` | `https://www.instagram.com/rayn.nyx/p/DKttbxziMY8/` | rayn.nyx, gfbweekend.official, lx.nsty | Home, gallery, dress-code draft |
| `collab-04-artinblack.m-DYFuuUejBmAj.jpg` | `https://www.instagram.com/artinblack.m/p/DYFuuUejBmAjqEAUXljrRbLfaQ2U82xT4B8oMg0/` | artinblack.m and lx.nsty | Home, gallery, dress-code draft |
| `collab-05-rayn.nyx-DLH8AQbClDA.jpg` | `https://www.instagram.com/rayn.nyx/p/DLH8AQbClDA/` | rayn.nyx, gfbweekend.official, lx.nsty | Home hero and gallery. Not a future date. |
| `collab-06-mew_chiel-DLDT0Bos2FG.jpg` | `https://www.instagram.com/mew_chiel/p/DLDT0Bos2FG/` | mew_chiel, aenn_alien, lx.nsty | Gallery and dress-code draft. German Fetish Ball mark stays in frame. This site does not claim that event. |

Those paths were announced for this build (`/workspace/nsty-assets/images/…`) but the bytes were not on disk. Reading them failed. The public post URL returned an Instagram error page (`httpErrorPage`); no undocumented API and no login bypass was used. `tools/optimize_media.py` is ready to strip metadata, resize, and write JPEG and WebP when the files are placed in `nsty-assets/images/` or `sources/incoming/`. Until then the preview shows an empty-frame note and no invented photograph.

Post URLs above are audit records. The only outbound link in `deploy/` is `https://www.instagram.com/lx.nsty/`.

## Copy

Preview text is original draft wording for NSTY nights. It is labeled as awaiting approval. It does not reuse reference slogans, FAQ answers, or legal identity from any other promoter.
