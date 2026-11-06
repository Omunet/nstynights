#!/usr/bin/env python3
"""Check the static tree: links, containment, security text, and routes."""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
IG = "https://www.instagram.com/lx.nsty/"
ASSET_OK = {
    "/assets/img/nsty-wordmark.svg",
    "/assets/img/favicon.svg",
    "/assets/css/root.css",
}
FORBIDDEN = re.compile(
    r"kinyxx|eventbrite|skiddle|fever\.|luxus|residentadvisor|ra\.co|ticketmaster|dice\.fm|facebook\.com|youtube\.com|youtu\.be|t\.me|telegram|web_profile_info",
    re.I,
)
PAIRS = {
    "/test/": "/test/es/",
    "/test/manifest/": "/test/es/manifiesto/",
    "/test/rules/": "/test/es/normas/",
    "/test/photos/": "/test/es/fotos/",
    "/test/dress-code/": "/test/es/dress-code/",
    "/test/faq/": "/test/es/faq/",
    "/test/contact/": "/test/es/contacto/",
    "/test/access/": "/test/es/acceso/",
    "/test/aviso-legal/": "/test/es/aviso-legal/",
}


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.attrs = []
        self.ids = set()
        self.tags = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        self.tags.append(tag)
        self.attrs.append((tag, attr))
        if "id" in attr:
            self.ids.add(attr["id"])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_data(self, data):
        self.text.append(data)


def page_url(path):
    rel = path.relative_to(DEPLOY).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def local_target(url, attr):
    if attr.startswith(("http://", "https://", "mailto:", "data:")):
        return None
    if attr.startswith("#"):
        return ("fragment", attr[1:])
    path = attr.split("#", 1)[0]
    if not path.startswith("/"):
        return ("bad-relative", attr)
    return ("path", path)


def exists(path):
    rel = path[1:]
    candidate = DEPLOY / rel
    if candidate.is_file():
        return True
    if candidate.is_dir() and (candidate / "index.html").is_file():
        return True
    if path.endswith("/") and (DEPLOY / rel / "index.html").is_file():
        return True
    if not path.endswith("/") and (DEPLOY / (rel + "/index.html")).is_file():
        return True
    return False


def main():
    errors = []
    notes = []
    pages = sorted(DEPLOY.rglob("*.html"))
    if not pages:
        errors.append("no html")
    dot_rule = re.compile(r"(^|/)\.(?!well-known(?:/|$))")
    ext_rule = re.compile(r"(?i)\.(?:env|zip|sql|bak|log|ini|php|phps|phtml|phar)$")
    samples = {
        "/.htaccess": True,
        "/.env": True,
        "/.git/config": True,
        "/test/assets/css/site.css": False,
        "/.well-known/acme-challenge/token": False,
        "/file.zip": True,
        "/test/index.html": False,
    }
    for sample, blocked in samples.items():
        hit = bool(dot_rule.search(sample) or ext_rule.search(sample))
        if hit != blocked:
            errors.append(f"htaccess pattern mismatch for {sample}: blocked={hit}")

    ht = (DEPLOY / ".htaccess").read_text(encoding="utf-8").lower()
    if "strict-transport-security" in ht or "rewritecond %{https}" in ht:
        errors.append("htaccess enables HTTPS forcing or HSTS")
    for needle in ("options -indexes", "nosniff", "sameorigin", "strict-origin-when-cross-origin", "noindex, nofollow", "content-security-policy"):
        if needle not in ht:
            errors.append(f"htaccess missing {needle}")

    robots = (DEPLOY / "robots.txt").read_text(encoding="utf-8")
    if "Disallow: /test" not in robots:
        errors.append("robots.txt does not disallow /test")

    svg = (DEPLOY / "assets/img/nsty-wordmark.svg").read_text(encoding="utf-8")
    if re.search(r"LX", svg):
        errors.append("wordmark svg contains LX")
    if "<text" in svg:
        errors.append("wordmark uses a text element")
    if "data:image" in svg or ".jpg" in svg or ".png" in svg:
        errors.append("wordmark embeds a raster")

    seen = {}
    for path in pages:
        url = page_url(path)
        raw = path.read_text(encoding="utf-8")
        parser = Collector()
        parser.feed(raw)
        seen[url] = parser
        if FORBIDDEN.search(raw):
            errors.append(f"forbidden reference in {url}")
        if url == "/":
            if "noindex" in raw.lower():
                errors.append("root is noindex")
            if "<nav" in raw.lower() or "<a " in raw.lower():
                errors.append("root has a link or nav")
            if "LX" in raw:
                errors.append("root contains LX")
        else:
            if 'content="noindex, nofollow"' not in raw:
                errors.append(f"missing robots meta on {url}")
            if not url.startswith("/test/"):
                errors.append(f"unexpected page outside /test: {url}")
            if "<form" in raw.lower() or 'type="password"' in raw.lower() or "<input" in raw.lower():
                errors.append(f"form or input on {url}")
            brands = [tag for tag, attr in parser.attrs if tag == "a" and attr.get("class") != "external" and "brand" in (attr.get("class") or "")]
            # brand is class on the anchor
            for tag, attr in parser.attrs:
                if tag == "a" and "brand" in (attr.get("class") or ""):
                    href = attr.get("href")
                    if href not in ("/test/", "/test/es/"):
                        errors.append(f"brand link on {url} points to {href}")
        for tag, attr in parser.attrs:
            for key in ("href", "src"):
                value = attr.get(key)
                if not value:
                    continue
                if value.startswith("#"):
                    frag = value[1:]
                    if frag not in parser.ids:
                        errors.append(f"dead fragment {value} on {url}")
                    continue
                if value.startswith("https://") or value.startswith("http://"):
                    if value.rstrip("/") != IG.rstrip("/"):
                        errors.append(f"unexpected external {value} on {url}")
                    continue
                target = local_target(url, value)
                if target[0] == "bad-relative":
                    errors.append(f"relative url {value} on {url}")
                    continue
                path_only = target[1]
                if path_only in ASSET_OK or path_only.startswith("/test/"):
                    if not exists(path_only):
                        errors.append(f"missing {path_only} referenced by {url}")
                    continue
                errors.append(f"url escapes preview: {value} on {url}")
            srcset = attr.get("srcset")
            if srcset:
                for part in srcset.split(","):
                    token = part.strip().split()[0]
                    if not token.startswith("/test/") or not exists(token):
                        errors.append(f"bad srcset {token} on {url}")

    for en, es in PAIRS.items():
        if en not in seen or es not in seen:
            errors.append(f"missing pair {en} {es}")
            continue
        en_hrefs = [attr.get("hreflang") and attr.get("href") for _, attr in seen[en].attrs if attr.get("hreflang") == "es"]
        es_hrefs = [attr.get("href") for _, attr in seen[es].attrs if attr.get("hreflang") == "en"]
        if en not in [attr.get("href") for _, attr in seen[es].attrs if attr.get("hreflang") == "en"]:
            errors.append(f"{es} does not point back to {en}")
        if es not in [attr.get("href") for _, attr in seen[en].attrs if attr.get("hreflang") == "es"]:
            errors.append(f"{en} does not point to {es}")

    home = (DEPLOY / "test/index.html").read_text(encoding="utf-8")
    if "archive-2025-poster" in home:
        errors.append("archive poster is on the home page")
    audit_phrases = (
        "frame stays empty",
        "verified public",
        "One verified",
        "not readable in this build",
        "German Fetish",
        "BERLINA",
        "DeSade",
        "31.05.2025",
    )
    for path in pages:
        raw = path.read_text(encoding="utf-8")
        for phrase in audit_phrases:
            if phrase in raw:
                errors.append(f"audit phrase {phrase!r} in {page_url(path)}")
    media = (ROOT / "sources/media/derivatives.json").is_file()
    if media:
        for slug in ("runway", "outdoor-latex", "backstage-latex", "monochrome-portrait"):
            if slug not in home:
                errors.append(f"home missing {slug}")
        dress = (DEPLOY / "test/dress-code/index.html").read_text(encoding="utf-8")
        photos = (DEPLOY / "test/photos/index.html").read_text(encoding="utf-8")
        for slug in ("outdoor-latex", "backstage-latex", "white-latex", "monochrome-portrait"):
            if slug not in dress:
                errors.append(f"dress code missing {slug}")
        if "archive-2025-poster" not in photos:
            errors.append("photos archive missing poster")
        if photos.count("<img ") < 5:
            errors.append("photos page has fewer than 5 images")
    else:
        errors.append("derivatives.json missing; photographs were not built")

    print(f"pages {len(pages)}")
    for note in notes:
        print(note)
    if errors:
        print(f"FAIL {len(errors)}")
        for error in errors:
            print(" -", error)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
