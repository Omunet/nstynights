# Deployment

This branch does not deploy, change DNS, merge, or alter repository visibility.

## What to upload

Upload the **contents** of `deploy/` to the dedicated docroot:

`/home/dracoborir/nstynights`

Do not upload `docs/`, `tools/`, `sources/`, or `.git`. The SFTP host recorded for this hosting is `ftp.cluster126.hosting.ovh.net`, port 22, user `dracoborir`. The password is not in this repository and must not be added.

Cluster addresses recorded for the non-CDN host are `87.98.154.146` and `2001:41d0:301::26`. Public DNS was still parked when this branch was built. Do not point DNS from this branch.

## What the docroot contains

- `/` — black page, NSTY wordmark only
- `/test/` — bilingual draft site, `noindex, nofollow` in HTML and, when `mod_headers` is available, in `X-Robots-Tag`
- `/robots.txt` — `Disallow: /test`
- `/.htaccess` — indexes off, dotfiles denied except `/.well-known/`, sensitive extensions denied, security headers

OVH must allow `AllowOverride` for `Options`, `FileInfo`, and rewrite. If `mod_headers` or `mod_rewrite` is off, the HTML `noindex` meta still covers `/test/`, but the header and dotfile rules will not.

## HTTPS and HSTS — do not enable yet

No HTTPS redirect and no `Strict-Transport-Security` header are in `.htaccess`. Leave them out until a certificate is valid for **both** `nstynights.com` and `www.nstynights.com`.

After that confirmation, a later change can add:

```apache
RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
Header always set Strict-Transport-Security "max-age=31536000" env=HTTPS
```

Do not add `upgrade-insecure-requests` to the CSP before that either. The current CSP is local assets only: `default-src 'self'`, no form target, no frames, no remote fonts, no connections.

## Checks before the first public copy

1. Serve `deploy/` and open `/` and `/test/`.
2. Confirm `/test/` responses carry `X-Robots-Tag: noindex, nofollow` once headers work.
3. Confirm `https://` works for apex and www before any HSTS.
4. Keep the zone backup diff in mind and preserve MX when DNS is changed later.
