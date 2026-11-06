# Provenance and source audit

Sources were read from the supplied archive `nsty-authorised-media.zip`. Dimensions and SHA-256 were taken from those files before any resize.

| Archive path | Pixels | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `logo/lx-nsty-profile-1.jpg` | 150×150 | 4169 | `e294e2e31611551b0bdf726d4b9b92440f86e26c03c2b11074d0d5d31d98953c` |
| `images/nsty-ig-01-DL3a1nkodkW.jpg` | 1440×1800 | 442986 | `8b4079b4a01800f9641ecb27c1792a7553febb63d08b56eb2db548592aa42be3` |
| `images/collab-02-rayn.nyx-DNL0neeiqpj.jpg` | 1440×1920 | 271817 | `61d9e2036f450fe1b935bcacf94b50ebdbdcc23386cf990fe008d53eae1f1fcd` |
| `images/collab-03-rayn.nyx-DKttbxziMY8.jpg` | 1440×1800 | 139327 | `b33190bc006f44aeffc98b517289ba2719f6d2891d2bda64630056727ab0a47d` |
| `images/collab-04-artinblack.m-DYFuuUejBmAj.jpg` | 1170×1560 | 223633 | `e694489b7ab9a4b7d4b098a2eca264c617b6acdd8978889e607b8e0232df43b9` |
| `images/collab-05-rayn.nyx-DLH8AQbClDA.jpg` | 1440×1800 | 204489 | `704abb04ea6f1bc2f7bd7775031af3a1da53b2bd5349fe766b36e26840364f08` |
| `images/collab-06-mew_chiel-DLDT0Bos2FG.jpg` | 1440×1800 | 533787 | `a5e8dc26c6edc406154064c3de10a4820a11362111483d4421ef62de215858aa` |

The profile hash matches the earlier brief. No network fetch was used for these files.

## Wordmark

`deploy/assets/img/nsty-wordmark.svg` is a potrace of the lower NSTY pixels in `logo/lx-nsty-profile-1.jpg`. Rows above that word were dropped, so the upper line is not in the drawing. Paths are filled with a metal gradient. The SVG does not embed a raster and does not use a font.

The same mark is visible, sharper, at the top right of `images/nsty-ig-01-DL3a1nkodkW.jpg`. That plate sits on a photographed background, so the trace uses the clean black profile bitmap. The source crop and the vector are shown together in `/opt/cursor/artifacts/nsty-source-vs-vector.png`. The 150-pixel source limits how tight the corners can be.

## Photographs

Jonathan (t175u, 2026-11-06) authorised posts authored or co-authored by `@lx.nsty`. Tagged-only posts stay out. Optimised JPEG and WebP live under `deploy/test/assets/media/`. Camera EXIF is stripped. Frames are not cropped in a way that removes printed marks.

| Use | Source | Credit on the page |
| --- | --- | --- |
| Home and gallery | 05 runway, 02 outdoor latex, 04 monochrome, 03 backstage | @rayn.nyx or @artinblack.m with @lx.nsty |
| Gallery and dress | 06 white latex | @mew_chiel with @lx.nsty. The event mark in the frame is not NSTY’s. |
| Dated archive only | 01 poster | @nyxianyx · @lx.nsty. Printed 2025 lines are past dates, not a coming schedule. |

Post URLs from the archive’s `images/PROVENANCE.md` stay in that file. The only outbound link in `deploy/` is `https://www.instagram.com/lx.nsty/`.

## Fonts

Self-hosted WOFF2, SIL Open Font License 1.1, from Fontsource 5.2.5: Big Shoulders Display, Barlow Condensed, Outfit. License text is `deploy/test/assets/fonts/OFL.txt`.
