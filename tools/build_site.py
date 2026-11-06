#!/usr/bin/env python3
"""Write the static root page and the /test/ preview from local data."""

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
DERIV = ROOT / "sources" / "media" / "derivatives.json"

NAV = [
    ("home", "/test/", "/test/es/", "Home", "Inicio", True),
    ("manifest", "/test/manifest/", "/test/es/manifiesto/", "Manifest", "Manifiesto", True),
    ("rules", "/test/rules/", "/test/es/normas/", "Rules", "Normas", True),
    ("photos", "/test/photos/", "/test/es/fotos/", "Photos", "Fotos", True),
    ("dress", "/test/dress-code/", "/test/es/dress-code/", "Dress code", "Dress code", True),
    ("faq", "/test/faq/", "/test/es/faq/", "FAQ", "FAQ", True),
    ("contact", "/test/contact/", "/test/es/contacto/", "Contact", "Contacto", True),
    ("access", "/test/access/", "/test/es/acceso/", "Access", "Acceso", True),
    ("legal", "/test/aviso-legal/", "/test/es/aviso-legal/", "Legal notice", "Aviso legal", False),
]

IG = "https://www.instagram.com/lx.nsty/"
FIG = re.compile(r"\{fig:([a-z0-9-]+)(?::(eager|lazy))?\}")

FIGURES = {
    "runway": {
        "alt": {
            "en": "A person in brown-black latex and long black gloves walks a runway with arms open. People stand along both sides. A screen behind shows the same scene.",
            "es": "Una persona con látex marrón-negro y guantes largos negros camina por una pasarela con los brazos abiertos. Hay gente a ambos lados. Una pantalla detrás muestra la misma escena.",
        },
        "caption": {
            "en": "Photograph · @rayn.nyx with @lx.nsty",
            "es": "Fotografía · @rayn.nyx con @lx.nsty",
        },
    },
    "outdoor-latex": {
        "alt": {
            "en": "A person with short pink hair, a black spiked eye covering, brown-black latex, long gloves, and a black feathered collar, against a painted metal wall.",
            "es": "Una persona con pelo rosa corto, una cobertura negra de ojos con pinchos, látex marrón-negro, guantes largos y un cuello de plumas negras, contra una pared de metal pintada.",
        },
        "caption": {
            "en": "Photograph · @rayn.nyx with @lx.nsty",
            "es": "Fotografía · @rayn.nyx con @lx.nsty",
        },
    },
    "backstage-latex": {
        "alt": {
            "en": "A person with short pink hair, a black spiked eye covering, and dark latex stands in a dim corridor with a ring light. Another figure is far behind.",
            "es": "Una persona con pelo rosa corto, una cobertura negra de ojos con pinchos y látex oscuro, en un pasillo en penumbra con un aro de luz. Otra figura queda lejos al fondo.",
        },
        "caption": {
            "en": "Photograph · @rayn.nyx with @lx.nsty",
            "es": "Fotografía · @rayn.nyx con @lx.nsty",
        },
    },
    "monochrome-portrait": {
        "alt": {
            "en": "Black-and-white portrait of a person in a dark fur coat, a chest harness, and shiny trousers, one hand raised to the forehead.",
            "es": "Retrato en blanco y negro de una persona con abrigo de pelo oscuro, arnés y pantalón brillante, una mano en la frente.",
        },
        "caption": {
            "en": "Photograph · @artinblack.m with @lx.nsty",
            "es": "Fotografía · @artinblack.m con @lx.nsty",
        },
    },
    "white-latex": {
        "alt": {
            "en": "A person in a white latex two-piece with black flame shapes, a long white drape, and black platform boots, against a metal wall. An event mark is printed at the top of the frame.",
            "es": "Una persona con un conjunto de látex blanco con llamas negras, una tela blanca larga y botas negras de plataforma, contra una pared de metal. El marco lleva una marca de evento arriba.",
        },
        "caption": {
            "en": "Photograph · @mew_chiel with @lx.nsty. The event mark in the frame belongs to that night, not to NSTY.",
            "es": "Fotografía · @mew_chiel con @lx.nsty. La marca de evento del marco es de esa noche, no de NSTY.",
        },
    },
    "archive-2025-poster": {
        "alt": {
            "en": "A 2025 poster: a person in a sheer dark latex top and a black feathered garment, with a printed list of past dates.",
            "es": "Cartel de 2025: una persona con un top de látex oscuro y una prenda negra de plumas, con una lista impresa de fechas pasadas.",
        },
        "caption": {
            "en": "Archive · 2025 · photograph @nyxianyx · @lx.nsty",
            "es": "Archivo · 2025 · fotografía @nyxianyx · @lx.nsty",
        },
    },
}


def load_deriv():
    if not DERIV.is_file():
        return {}
    return json.loads(DERIV.read_text(encoding="utf-8"))


def esc(value):
    return html.escape(value, quote=True)


def figure_html(slug, lang, loading, deriv):
    if slug not in deriv:
        return (
            '<p class="note">This frame stays empty. The authorised photograph was not readable in this build, and no substitute image is used.</p>'
        )
    item = deriv[slug]
    sizes = item["derivatives"]
    largest = sizes[-1]
    srcset = ", ".join(f'{row["webp"]} {row["width"]}w' for row in sizes)
    alt = FIGURES[slug]["alt"][lang]
    caption = FIGURES[slug]["caption"][lang]
    return (
        '<figure class="frame">'
        "<picture>"
        f'<source type="image/webp" srcset="{esc(srcset)}" sizes="(min-width: 1100px) 1000px, 100vw">'
        f'<img src="{esc(largest["jpg"])}" alt="{esc(alt)}" width="{largest["width"]}" height="{largest["height"]}" loading="{loading}" decoding="async">'
        "</picture>"
        f"<figcaption>{esc(caption)}</figcaption>"
        "</figure>"
    )


def fill_figs(text, lang, deriv):
    def replace(match):
        loading = match.group(2) or "eager"
        return figure_html(match.group(1), lang, loading, deriv)

    return FIG.sub(replace, text)


def route_file(url):
    path = url.strip("/")
    if path == "test":
        return DEPLOY / "test" / "index.html"
    return DEPLOY / path / "index.html"


def page_shell(lang, key, body):
    route = {item[0]: item for item in NAV}[key]
    _, en_url, es_url, en_label, es_label, _ = route
    here = en_url if lang == "en" else es_url
    other = es_url if lang == "en" else en_url
    other_label = "ES" if lang == "en" else "EN"
    other_lang = "es" if lang == "en" else "en"
    label = en_label if lang == "en" else es_label
    title = "NSTY nights preview" if key == "home" and lang == "en" else (
        "NSTY noches, previsualización" if key == "home" else f"{label} — NSTY nights preview"
    )
    banner = (
        "Draft preview — content awaiting approval"
        if lang == "en"
        else "Borrador — contenido pendiente de aprobación"
    )
    home = "/test/" if lang == "en" else "/test/es/"
    hidden = "NSTY" 
    items = []
    for item in NAV:
        if not item[5]:
            continue
        href = item[1] if lang == "en" else item[2]
        text = item[3] if lang == "en" else item[4]
        current = ' aria-current="page"' if href == here else ""
        extra = ' class="nav-access"' if item[0] == "access" else ""
        items.append(f'<li><a href="{href}"{extra}{current}>{esc(text)}</a></li>')
    items.insert(-1, f'<li><a href="{other}" hreflang="{other_lang}" lang="{other_lang}">{other_label}</a></li>')
    footer_links = []
    for item in NAV:
        href = item[1] if lang == "en" else item[2]
        text = item[3] if lang == "en" else item[4]
        current = ' aria-current="page"' if href == here else ""
        footer_links.append(f'<li><a href="{href}"{current}>{esc(text)}</a></li>')
    ig_label = "Instagram"
    pending = (
        "Tickets, the room, and the next date are coming soon."
        if lang == "en"
        else "Entradas, sala y próxima fecha: próximamente."
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#000000">
<meta name="description" content="{esc(banner)}">
<title>{esc(title)}</title>
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{lang}" href="{here}">
<link rel="alternate" hreflang="{other_lang}" href="{other}">
<link rel="stylesheet" href="/test/assets/css/site.css">
</head>
<body>
<a class="skip" href="#content">{"Skip to content" if lang == "en" else "Saltar al contenido"}</a>
<p class="draft-banner">{esc(banner)}</p>
<header class="site-header">
<a class="brand" href="{home}"><img src="/assets/img/nsty-wordmark.svg" alt="" width="146" height="69"><span class="visually-hidden">{hidden}</span></a>
<button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav">{"Menu" if lang == "en" else "Menú"}</button>
<nav class="primary-nav" id="site-nav" data-nav-panel aria-label="{"Primary" if lang == "en" else "Principal"}">
<ul>
{"".join(items)}
</ul>
</nav>
</header>
<main id="content">
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<nav class="footer-nav" aria-label="{"Pages" if lang == "en" else "Páginas"}">
<ul>
{"".join(footer_links)}
<li><a class="external" href="{IG}" rel="noreferrer noopener">{ig_label}</a></li>
</ul>
</nav>
<p>{esc(pending)}</p>
</div>
</footer>
<script src="/test/assets/js/site.js" defer></script>
</body>
</html>
"""


from page_copy import BODIES

def write_root():
    text = """<!DOCTYPE html>
<html lang="zxx">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#000000">
<title>NSTY</title>
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/root.css">
</head>
<body>
<main>
<img src="/assets/img/nsty-wordmark.svg" alt="NSTY" title="NSTY" width="146" height="69">
</main>
</body>
</html>
"""
    (DEPLOY / "index.html").write_text(text, encoding="utf-8")


def write_routes():
    lines = [
        "# Route manifest",
        "",
        "Public URLs assume the deploy directory is the docroot of nstynights.com.",
        "Root is the mark only. Every other page is under `/test/` and is marked noindex.",
        "",
        "| URL | File | Language | Role |",
        "| --- | --- | --- | --- |",
        "| `/` | `deploy/index.html` | no linguistic content | Public mark |",
    ]
    for key, en_url, es_url, en_label, es_label, _ in NAV:
        lines.append(f"| `{en_url}` | `{route_file(en_url).relative_to(ROOT).as_posix()}` | en | {en_label} |")
        lines.append(f"| `{es_url}` | `{route_file(es_url).relative_to(ROOT).as_posix()}` | es | {es_label} |")
    lines.append("")
    lines.append("Language pairs switch between the two URLs on the same row group and stay on the equivalent page.")
    lines.append("")
    (ROOT / "docs" / "ROUTE-MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    deriv = load_deriv()
    write_root()
    for lang, pages in BODIES.items():
        for key, body in pages.items():
            route = {item[0]: item for item in NAV}[key]
            url = route[1] if lang == "en" else route[2]
            filled = fill_figs(body, lang, deriv)
            path = route_file(url)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(page_shell(lang, key, filled), encoding="utf-8")
            print(path.relative_to(ROOT))
    write_routes()


if __name__ == "__main__":
    main()
