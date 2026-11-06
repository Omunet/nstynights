# nstynights

Static preview for nstynights.com.

`deploy/` is the docroot. `/` is a black page with the NSTY wordmark only. The bilingual draft site lives under `/test/` and is marked noindex.

`docs/` is not part of the upload. Rebuild HTML with `python3 tools/build_site.py` after copy or cleared media changes. Image derivatives are produced by `python3 tools/optimize_media.py`.

Local check, from this directory:

```
python3 -m http.server -d deploy 8765
```

Do not deploy, change DNS, or merge this branch from the agent. See `docs/DEPLOYMENT.md`.
