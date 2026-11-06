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
            "en": "Runway photograph. A person with pink hair, a brown-black latex outfit, and long black gloves walks forward with arms extended. People stand along both sides. A large screen behind shows the scene and a metallic mark.",
            "es": "Fotografía de pasarela. Una persona con pelo rosa, un conjunto de látex marrón-negro y guantes largos negros camina hacia delante con los brazos abiertos. Hay gente a ambos lados. Una pantalla grande detrás muestra la escena y una marca metálica.",
        },
        "caption": {
            "en": "Co-authored photograph. Accounts named on the post: @rayn.nyx, @gfbweekend.official, and @lx.nsty. The graphic on the screen is left as printed. This frame is not a future date.",
            "es": "Fotografía en coautoría. Cuentas nombradas en la publicación: @rayn.nyx, @gfbweekend.official y @lx.nsty. El gráfico de la pantalla se deja como está impreso. Esta imagen no es una fecha futura.",
        },
    },
    "outdoor-latex": {
        "alt": {
            "en": "A person with short bright pink hair, a black spiked eye covering, a brown-black latex outfit, long black gloves, and a black feathered collar, standing against a painted corrugated metal wall.",
            "es": "Una persona con pelo rosa corto, una cobertura negra de ojos con pinchos, un conjunto de látex marrón-negro, guantes largos negros y un cuello de plumas negras, de pie contra una pared de metal ondulado pintada.",
        },
        "caption": {
            "en": "Co-authored photograph. Accounts named on the post: @rayn.nyx and @lx.nsty. Draft reference only, not a dress rule.",
            "es": "Fotografía en coautoría. Cuentas nombradas en la publicación: @rayn.nyx y @lx.nsty. Solo referencia de borrador, no una norma de vestimenta.",
        },
    },
    "backstage-latex": {
        "alt": {
            "en": "A person with short bright pink hair, a black spiked eye covering, and a dark latex outfit with long gloves, standing in a dim corridor with a lighting truss and a ring light. Another figure is far in the background.",
            "es": "Una persona con pelo rosa corto, una cobertura negra de ojos con pinchos y un conjunto de látex oscuro con guantes largos, de pie en un pasillo en penumbra con una estructura de luces y un aro de luz. Otra figura aparece lejos al fondo.",
        },
        "caption": {
            "en": "Co-authored photograph. Accounts named on the post: @rayn.nyx, @gfbweekend.official, and @lx.nsty. The credit is not a claim that this preview organises an event.",
            "es": "Fotografía en coautoría. Cuentas nombradas en la publicación: @rayn.nyx, @gfbweekend.official y @lx.nsty. El crédito no afirma que esta previsualización organice un evento.",
        },
    },
    "monochrome-portrait": {
        "alt": {
            "en": "Black-and-white photograph of a person wearing a large dark fur coat, a chest harness, a collar with visible lettering, and shiny dark trousers, one hand raised to the forehead, in front of a bright grid.",
            "es": "Fotografía en blanco y negro de una persona con un abrigo amplio de pelo oscuro, un arnés en el pecho, un collar con letras visibles y un pantalón oscuro brillante, una mano en la frente, delante de una retícula luminosa.",
        },
        "caption": {
            "en": "Co-authored photograph. Accounts named on the post: @artinblack.m and @lx.nsty.",
            "es": "Fotografía en coautoría. Cuentas nombradas en la publicación: @artinblack.m y @lx.nsty.",
        },
    },
    "white-latex": {
        "alt": {
            "en": "A person with tattoos wearing a white latex two-piece with black flame shapes, a long white drape, and black platform boots, against a corrugated metal wall. A German Fetish Ball mark is printed at the top and a photographer mark sits along the lower edge.",
            "es": "Una persona con tatuajes, un conjunto de látex blanco con formas de llama negras, una tela blanca larga y botas negras de plataforma, contra una pared de metal ondulado. Arriba está impresa una marca de German Fetish Ball y en el borde inferior hay una marca de fotógrafo.",
        },
        "caption": {
            "en": "Co-authored photograph. Accounts named on the post: @mew_chiel, @aenn_alien, and @lx.nsty. The German Fetish Ball mark and the photographer mark are left unedited. This preview does not organise that event and does not own that mark.",
            "es": "Fotografía en coautoría. Cuentas nombradas en la publicación: @mew_chiel, @aenn_alien y @lx.nsty. La marca de German Fetish Ball y la marca del fotógrafo se dejan sin editar. Esta previsualización no organiza ese evento ni es dueña de esa marca.",
        },
    },
    "archive-2025-poster": {
        "alt": {
            "en": "Poster showing a person in a sheer dark latex top and a black feathered garment, with sunglasses on the head. The poster prints a 2025 date list and a metallic mark in the upper corner.",
            "es": "Cartel con una persona en un top de látex oscuro semitransparente y una prenda negra de plumas, con gafas de sol sobre la cabeza. El cartel imprime una lista de fechas de 2025 y una marca metálica en la esquina superior.",
        },
        "caption": {
            "en": "Dated archive, 2025. Photograph credit @nyxianyx. Post authored by @lx.nsty. Printed dates are in the past. They are not a schedule for this website.",
            "es": "Archivo fechado, 2025. Crédito de la fotografía: @nyxianyx. Publicación de @lx.nsty. Las fechas impresas ya pasaron. No son un calendario de este sitio.",
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
        loading = match.group(2) or "lazy"
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
        "Preview draft. Not an event announcement. Wording on these pages is awaiting approval."
        if lang == "en"
        else "Borrador de previsualización. No anuncia un evento. El texto de estas páginas espera aprobación."
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
        "Tickets, mixes, email, venue, and upcoming dates are not published. Those words are not links."
        if lang == "en"
        else "Entradas, mezclas, correo, sala y fechas próximas no están publicadas. Esas palabras no son enlaces."
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
<a class="brand" href="{home}"><img src="/assets/img/nsty-wordmark.svg" alt="" width="930" height="420"><span class="visually-hidden">{hidden}</span></a>
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


ARCHIVE_LINES = """
<ul class="plain-list stack">
<li>31.05.2025 — German Fetish Ball, Berlin, DE</li>
<li>04.07.2025 — BERLINA, Imperial Club, Barcelona, ES</li>
<li>12.07.2025 — DeSade Festival, Barcelona, ES</li>
<li>27.09.2025 — Manifest, Copenhagen, DNK</li>
</ul>
"""

BODIES = {
    "en": {
        "home": """
<section class="hero"><div class="wrap"><p class="kicker">Nights preview</p><h1>NSTY</h1><p class="lede">This is a working preview of nstynights.com. It is not a calendar, a ticket office, or a shop.</p></div></section>
<section class="band"><div class="wrap">{fig:runway:eager}</div></section>
<section class="band band-metal"><div class="wrap prose"><p class="section-index">01 — What is public</p><h2>One verified profile</h2><p>The only verified public address is Instagram @lx.nsty. That profile describes latex clothing made in Barcelona and asks people to send a direct message about orders. This website is the nights preview. It does not sell garments, and it does not confirm a night.</p><p>Photographs here come from posts authored or co-authored by that account. A post that only tags the account is not used. Marks already printed inside a photograph are left as they were.</p></div></section>
<section class="band"><div class="wrap split">{fig:outdoor-latex}<div class="prose"><p class="section-index">02 — Still unpublished</p><h2>Blanks stay blank</h2><dl class="status-list"><dt>Dates</dt><dd>Not published</dd><dt>Venue</dt><dd>Not published</dd><dt>Line-up</dt><dd>Not published</dd><dt>Tickets</dt><dd>Not published. There is no sales link.</dd><dt>Mixes</dt><dd>Not published</dd><dt>Email</dt><dd>Not published</dd><dt>Age and admission</dt><dd>Not decided in this preview</dd></dl></div></div></section>
<section class="band band-metal"><div class="wrap split reverse"><div class="prose"><p class="section-index">03 — Drafts</p><h2>Read the proposals</h2><p>The manifesto, house notes, dress notes, and questions are drafts waiting for approval. They are not door policy.</p><div class="link-row"><a href="/test/manifest/">Manifest</a><a href="/test/rules/">Rules</a><a href="/test/dress-code/">Dress code</a><a href="/test/faq/">FAQ</a></div></div>{fig:monochrome-portrait}</div></section>
<section class="band"><div class="wrap split">{fig:backstage-latex}<div class="prose"><p class="section-index">04 — Account media</p><h2>Frames from the account</h2><p>The gallery holds co-authored photographs. A 2025 poster with a printed date list stays in the dated archive. It is not a future announcement.</p><div class="link-row"><a href="/test/photos/">Photos</a><a href="/test/contact/">Contact</a></div></div></div></section>
""",
        "manifest": """
<section class="page-hero"><div class="wrap"><p class="kicker">Draft awaiting approval</p><h1>Manifest</h1><p class="lede">A proposal for the tone of NSTY nights. It is not a promise of an event.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p class="section-index">01</p><h2>A night, not a counter</h2><p>NSTY on this domain names a night that has not been announced. The Instagram account beside it is public as a Barcelona latex clothing practice that takes orders by direct message. Sharing a name does not turn this website into a catalogue. Garments are not listed here. Nights are not scheduled here.</p></div></section>
<section class="band"><div class="wrap prose"><p class="section-index">02</p><h2>Silence is not a guest list</h2><p>An empty date, an empty room, and an empty ticket line mean those facts are not published. They do not mean a guest list is open, a room is held, or a lineup is settled. When a night is real, it will be stated with a date and a place. Until then, a blank is a blank.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p class="section-index">03</p><h2>Conduct before costume</h2><p>A dress proposal can sit on its own page without being a rule of entry. How people treat one another will matter more than what they wear, and the house notes for that are still a draft. This preview does not invent an age limit, a search policy, or a right of admission and then pretend it is already in force.</p></div></section>
""",
        "rules": """
<section class="page-hero"><div class="wrap"><p class="kicker">Draft, not in force</p><h1>Rules</h1><p class="lede">Proposed house notes. Anything operational that has not been decided is marked TBD.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>Proposed notes</h2><ol class="stack"><li>This text is a draft for approval, not a condition of entry.</li><li>No date on this website is an invitation.</li><li>A message to the clothing account is not a confirmed way to reserve a place at a night.</li><li>A dress suggestion is not a dress code until it is approved as one.</li><li>People can refuse attention, touch, and photographs of themselves. How that is enforced is TBD.</li></ol></div></section>
<section class="band"><div class="wrap prose"><h2>Not decided</h2><dl class="status-list"><dt>Minimum age and ID</dt><dd>TBD</dd><dt>Admission, refusal, and removal</dt><dd>TBD</dd><dt>Search and prohibited items</dt><dd>TBD</dd><dt>Cameras and phones</dt><dd>TBD</dd><dt>Intoxication and care</dt><dd>TBD</dd><dt>Access of the room</dt><dd>TBD</dd><dt>Staffing</dt><dd>TBD</dd></dl></div></section>
""",
        "photos": """
<section class="page-hero"><div class="wrap"><p class="kicker">Account media</p><h1>Photos</h1><p class="lede">Frames from posts authored or co-authored by @lx.nsty. Tagged-only posts stay out. Nothing here is a forthcoming bill.</p></div></section>
<section class="band"><div class="wrap"><ul class="gallery"><li>{fig:outdoor-latex}</li><li>{fig:backstage-latex}</li><li>{fig:monochrome-portrait}</li><li>{fig:runway}</li><li>{fig:white-latex}</li></ul></div></section>
<section class="band band-metal" id="archive"><div class="wrap prose"><p class="section-index">Dated archive</p><h2>2025 poster</h2><p>This poster is a record of what it already prints. It is not a future schedule. The headline on the poster reads “SEE LX NSTY ON THE RUNWAY”. The wordmark in the header of this preview is NSTY only.</p>{fig:archive-2025-poster}<h3>Lines printed on the poster</h3>"""
        + ARCHIVE_LINES
        + """<p>These dates are in 2025. They record appearances already printed, not nights this website is announcing. This preview does not say that NSTY nights organised those events.</p></div></section>
""",
        "dress": """
<section class="page-hero"><div class="wrap"><p class="kicker">Draft, not an entry rule</p><h1>Dress code</h1><p class="lede">Categories and photographs from the account. Nothing below is required for admission, because admission itself is not defined.</p></div></section>
<section class="band"><div class="wrap category-grid"><article class="split">{fig:outdoor-latex}<div class="prose"><h2>Latex</h2><p>The public clothing profile is associated with latex made in Barcelona. That describes the account. It is not a rule that latex must be worn to a night.</p></div></article><article class="split reverse"><div class="prose"><h2>Dark latex, backstage light</h2><p>Another account photograph. It shows a material and a room. It does not set a door.</p></div>{fig:backstage-latex}</article><article class="split">{fig:white-latex}<div class="prose"><h2>Light latex, printed mark left in frame</h2><p>The event mark visible in this photograph belongs to that event. It is not evidence that NSTY nights organises it, and the mark was not painted out.</p></div></article><article class="split reverse"><div class="prose"><h2>Fur, harness, shine</h2><p>A further draft reference. Covered or ordinary dark clothing is not forbidden by this page, because this page forbids nothing.</p></div>{fig:monochrome-portrait}</article></div></section>
""",
        "faq": """
<section class="page-hero"><div class="wrap"><p class="kicker">Draft answers</p><h1>FAQ</h1><p class="lede">These replies describe the preview. They are not an approved house policy.</p></div></section>
<section class="band"><div class="wrap"><details class="faq-item"><summary>Is a night announced?</summary><div class="answer"><p>No. This preview does not publish a date, a venue, or a lineup.</p></div></details><details class="faq-item"><summary>Can I buy a ticket?</summary><div class="answer"><p>No sales link is published. There is no checkout on this site.</p></div></details><details class="faq-item"><summary>How do I reach you?</summary><div class="answer"><p>The only verified destination is the Instagram profile @lx.nsty. Its public text is about latex clothing and direct messages for orders. This preview has no form and no email address. The contact page holds the link.</p></div></details><details class="faq-item"><summary>Is member access open?</summary><div class="answer"><p>No. The access page explains that no login exists yet.</p></div></details><details class="faq-item"><summary>What is the age limit?</summary><div class="answer"><p>TBD. This draft does not state one.</p></div></details><details class="faq-item"><summary>What should I wear?</summary><div class="answer"><p>See the dress-code draft. It is not an entry requirement.</p></div></details><details class="faq-item"><summary>Which photographs are shown?</summary><div class="answer"><p>Only files supplied from posts authored or co-authored by @lx.nsty. Posts where the account is only tagged stay out. A house rule for cameras inside a night is TBD.</p></div></details><details class="faq-item"><summary>Are older posters a list of upcoming nights?</summary><div class="answer"><p>No. The 2025 poster is in the dated archive, with the lines it prints. It is not a future schedule.</p></div></details><details class="faq-item"><summary>Do you set cookies?</summary><div class="answer"><p>This preview does not set cookies and does not load analytics or remote fonts.</p></div></details><details class="faq-item"><summary>Is the wording final?</summary><div class="answer"><p>No. Manifesto, rules, dress notes, questions, and the legal page are drafts awaiting approval.</p></div></details></div></section>
""",
        "contact": f"""
<section class="page-hero"><div class="wrap"><p class="kicker">One destination</p><h1>Contact</h1><p class="lede">There is no form on this page, and nothing here reports that a message was sent.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p>The verified destination is the Instagram profile <a class="external" href="{IG}" rel="noreferrer noopener">@lx.nsty</a>.</p><p>Its public text describes latex clothing made in Barcelona and asks for a direct message about orders. Writing to that account reaches the operator of that profile. This preview cannot confirm that a message will be read as a nights enquiry.</p><p>There is no published email, no ticket desk, and no member login.</p></div></section>
""",
        "access": """
<section class="page-hero"><div class="wrap"><p class="kicker">Not enabled</p><h1>Access</h1><p class="lede">Member access is not enabled. This server has no account system.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p>There is no password field, no registration, and no account to sign in to. When a real gate exists, this page will be replaced. Until then, there is nothing to submit.</p><div class="link-row"><a href="/test/">Preview home</a><a href="/test/contact/">Contact</a></div></div></section>
""",
        "legal": """
<section class="page-hero"><div class="wrap"><p class="kicker">Draft, not a statutory notice</p><h1>Legal notice</h1><p class="lede">The operator’s legal name, address, identifier, and contact have not been supplied. The blanks below are missing facts.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>Operator, pending</h2><dl class="pending-fields"><dt>Legal name</dt><dd>Pending — not supplied</dd><dt>Tax or company number</dt><dd>Pending — not supplied</dd><dt>Postal address</dt><dd>Pending — not supplied</dd><dt>Email</dt><dd>Pending — not supplied</dd><dt>Registry data</dt><dd>Pending — not supplied</dd></dl><p class="callout">A notice for a site aimed at Spain usually names the person or company responsible. That name has not been given. This page does not invent one.</p></div></section>
<section class="band"><div class="wrap prose"><h2>What this build does</h2><p>This is a static preview. It announces no event and sells nothing. It does not run a member login. It sets no cookies, loads no analytics, and sends no form, because there is no form. That sentence describes the build. It is not a registered privacy policy.</p><p>The only outbound link is the Instagram profile @lx.nsty. This site does not control that profile.</p><p>The NSTY wordmark in the header is an angular reconstruction of the lower lettering of the account mark, with the upper LX line omitted. It is not claimed as a pixel-perfect trace. Photographs are included only when supplied as account-authored or co-authored posts. Marks inside those photographs were not painted out.</p><p>A dedicated host for this domain is being prepared. This page does not name a data controller or a hosting party as if the record were complete.</p><p>Court, company, and governing law are for the operator to state with counsel. This draft chooses none of them. Replace this page before anyone presents it as a statutory notice.</p></div></section>
""",
    }
}

# Spanish bodies mirror the English claims.
BODIES["es"] = {
    "home": """
<section class="hero"><div class="wrap"><p class="kicker">Previsualización de noches</p><h1>NSTY</h1><p class="lede">Esto es una previsualización de trabajo de nstynights.com. No es un calendario, ni una taquilla, ni una tienda.</p></div></section>
<section class="band"><div class="wrap">{fig:runway:eager}</div></section>
<section class="band band-metal"><div class="wrap prose"><p class="section-index">01 — Lo que es público</p><h2>Un perfil verificado</h2><p>La única dirección pública verificada es Instagram @lx.nsty. Ese perfil describe ropa de látex hecha en Barcelona y pide un mensaje directo para pedidos. Este sitio es la previsualización de las noches. No vende prendas y no confirma una noche.</p><p>Las fotografías salen de publicaciones de autoría o coautoría de esa cuenta. Una publicación que solo etiqueta la cuenta no se usa. Las marcas ya impresas dentro de una fotografía se dejan como están.</p></div></section>
<section class="band"><div class="wrap split">{fig:outdoor-latex}<div class="prose"><p class="section-index">02 — Sigue sin publicarse</p><h2>El vacío sigue vacío</h2><dl class="status-list"><dt>Fechas</dt><dd>No publicadas</dd><dt>Sala</dt><dd>No publicada</dd><dt>Cartel</dt><dd>No publicado</dd><dt>Entradas</dt><dd>No publicadas. No hay enlace de venta.</dd><dt>Mezclas</dt><dd>No publicadas</dd><dt>Correo</dt><dd>No publicado</dd><dt>Edad y acceso</dt><dd>Sin decidir en esta previsualización</dd></dl></div></div></section>
<section class="band band-metal"><div class="wrap split reverse"><div class="prose"><p class="section-index">03 — Borradores</p><h2>Leer las propuestas</h2><p>El manifiesto, las notas de sala, las notas de vestimenta y las preguntas son borradores a la espera de aprobación. No son política de puerta.</p><div class="link-row"><a href="/test/es/manifiesto/">Manifiesto</a><a href="/test/es/normas/">Normas</a><a href="/test/es/dress-code/">Dress code</a><a href="/test/es/faq/">FAQ</a></div></div>{fig:monochrome-portrait}</div></section>
<section class="band"><div class="wrap split">{fig:backstage-latex}<div class="prose"><p class="section-index">04 — Medios de la cuenta</p><h2>Imágenes de la cuenta</h2><p>La galería reúne fotografías en coautoría. Un cartel de 2025 con fechas impresas permanece en el archivo fechado. No es un anuncio futuro.</p><div class="link-row"><a href="/test/es/fotos/">Fotos</a><a href="/test/es/contacto/">Contacto</a></div></div></div></section>
""",
    "manifest": """
<section class="page-hero"><div class="wrap"><p class="kicker">Borrador a la espera de aprobación</p><h1>Manifiesto</h1><p class="lede">Una propuesta de tono para las noches NSTY. No es la promesa de un evento.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p class="section-index">01</p><h2>Una noche, no un mostrador</h2><p>NSTY en este dominio nombra una noche que no se ha anunciado. La cuenta de Instagram que lo acompaña es pública como un trabajo de ropa de látex en Barcelona que toma pedidos por mensaje directo. Compartir un nombre no convierte este sitio en un catálogo. Aquí no se listan prendas. Aquí no se calendan noches.</p></div></section>
<section class="band"><div class="wrap prose"><p class="section-index">02</p><h2>El silencio no es una lista</h2><p>Una fecha vacía, una sala vacía y una línea de entradas vacía significan que esos datos no están publicados. No significan que haya lista abierta, sala reservada o cartel cerrado. Cuando una noche sea real, se dirá con fecha y lugar. Hasta entonces, un vacío es un vacío.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p class="section-index">03</p><h2>El trato antes del traje</h2><p>Una propuesta de vestimenta puede ocupar su página sin ser norma de entrada. Cómo se trata la gente importará más que lo que lleve puesto, y las notas de sala siguen en borrador. Esta previsualización no inventa un límite de edad, un cacheo o un derecho de admisión para fingir que ya rigen.</p></div></section>
""",
    "rules": """
<section class="page-hero"><div class="wrap"><p class="kicker">Borrador, no vigente</p><h1>Normas</h1><p class="lede">Notas de sala propuestas. Lo operativo que no está decidido figura como TBD.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>Notas propuestas</h2><ol class="stack"><li>Este texto es un borrador para aprobación, no una condición de entrada.</li><li>Ninguna fecha de este sitio es una invitación.</li><li>Un mensaje a la cuenta de ropa no es una forma confirmada de reservar plaza en una noche.</li><li>Una sugerencia de vestimenta no es un código hasta que se apruebe como tal.</li><li>Cada persona puede negar atención, contacto y fotografías de sí misma. Cómo se hace valer eso es TBD.</li></ol></div></section>
<section class="band"><div class="wrap prose"><h2>Sin decidir</h2><dl class="status-list"><dt>Edad mínima e identificación</dt><dd>TBD</dd><dt>Admisión, negativa y salida</dt><dd>TBD</dd><dt>Cacheo y objetos no admitidos</dt><dd>TBD</dd><dt>Cámaras y teléfonos</dt><dd>TBD</dd><dt>Intoxicación y cuidado</dt><dd>TBD</dd><dt>Acceso de la sala</dt><dd>TBD</dd><dt>Equipo</dt><dd>TBD</dd></dl></div></section>
""",
    "photos": """
<section class="page-hero"><div class="wrap"><p class="kicker">Medios de la cuenta</p><h1>Fotos</h1><p class="lede">Imágenes de publicaciones de autoría o coautoría de @lx.nsty. Las que solo etiquetan la cuenta quedan fuera. Nada de esto es un cartel futuro.</p></div></section>
<section class="band"><div class="wrap"><ul class="gallery"><li>{fig:outdoor-latex}</li><li>{fig:backstage-latex}</li><li>{fig:monochrome-portrait}</li><li>{fig:runway}</li><li>{fig:white-latex}</li></ul></div></section>
<section class="band band-metal" id="archive"><div class="wrap prose"><p class="section-index">Archivo fechado</p><h2>Cartel de 2025</h2><p>Este cartel es el registro de lo que ya imprime. No es un calendario futuro. El titular impreso dice “SEE LX NSTY ON THE RUNWAY”. La marca de la cabecera de esta previsualización es solo NSTY.</p>{fig:archive-2025-poster}<h3>Líneas impresas en el cartel</h3>"""
    + ARCHIVE_LINES
    + """<p>Las fechas son de 2025. Registran apariciones ya impresas, no noches que este sitio anuncie. Esta previsualización no dice que NSTY nights organizara esos eventos.</p></div></section>
""",
    "dress": """
<section class="page-hero"><div class="wrap"><p class="kicker">Borrador, no es norma de entrada</p><h1>Dress code</h1><p class="lede">Categorías y fotografías de la cuenta. Nada de lo siguiente es requisito de admisión, porque la admisión no está definida.</p></div></section>
<section class="band"><div class="wrap category-grid"><article class="split">{fig:outdoor-latex}<div class="prose"><h2>Látex</h2><p>El perfil público de ropa se asocia al látex hecho en Barcelona. Eso describe la cuenta. No es una norma de que haya que llevar látex a una noche.</p></div></article><article class="split reverse"><div class="prose"><h2>Látex oscuro, luz de camerino</h2><p>Otra fotografía de la cuenta. Muestra un material y una sala. No fija una puerta.</p></div>{fig:backstage-latex}</article><article class="split">{fig:white-latex}<div class="prose"><h2>Látex claro, marca impresa sin borrar</h2><p>La marca de evento visible en esta fotografía pertenece a ese evento. No prueba que NSTY nights lo organice, y la marca no se ha tapado.</p></div></article><article class="split reverse"><div class="prose"><h2>Pelo, arnés, brillo</h2><p>Otra referencia de borrador. La ropa oscura cubierta u ordinaria no queda prohibida por esta página, porque esta página no prohíbe nada.</p></div>{fig:monochrome-portrait}</article></div></section>
""",
    "faq": """
<section class="page-hero"><div class="wrap"><p class="kicker">Respuestas en borrador</p><h1>FAQ</h1><p class="lede">Estas respuestas describen la previsualización. No son una política de sala aprobada.</p></div></section>
<section class="band"><div class="wrap"><details class="faq-item"><summary>¿Hay una noche anunciada?</summary><div class="answer"><p>No. Esta previsualización no publica fecha, sala ni cartel.</p></div></details><details class="faq-item"><summary>¿Puedo comprar una entrada?</summary><div class="answer"><p>No hay enlace de venta. En este sitio no hay pago.</p></div></details><details class="faq-item"><summary>¿Cómo os escribo?</summary><div class="answer"><p>El único destino verificado es el perfil de Instagram @lx.nsty. Su texto público habla de ropa de látex y de mensajes directos para pedidos. Esta previsualización no tiene formulario ni correo. La página de contacto tiene el enlace.</p></div></details><details class="faq-item"><summary>¿El acceso de miembros está abierto?</summary><div class="answer"><p>No. La página de acceso explica que todavía no hay inicio de sesión.</p></div></details><details class="faq-item"><summary>¿Cuál es el límite de edad?</summary><div class="answer"><p>TBD. Este borrador no fija ninguno.</p></div></details><details class="faq-item"><summary>¿Qué hay que llevar?</summary><div class="answer"><p>Mira el borrador de dress code. No es un requisito de entrada.</p></div></details><details class="faq-item"><summary>¿Qué fotografías se muestran?</summary><div class="answer"><p>Solo archivos aportados de publicaciones de autoría o coautoría de @lx.nsty. Las publicaciones en las que la cuenta solo está etiquetada quedan fuera. Una norma de cámaras dentro de una noche es TBD.</p></div></details><details class="faq-item"><summary>¿Los carteles antiguos anuncian noches próximas?</summary><div class="answer"><p>No. El cartel de 2025 está en el archivo fechado, con las líneas que imprime. No es un calendario futuro.</p></div></details><details class="faq-item"><summary>¿Usáis cookies?</summary><div class="answer"><p>Esta previsualización no pone cookies y no carga analítica ni tipografías remotas.</p></div></details><details class="faq-item"><summary>¿El texto es definitivo?</summary><div class="answer"><p>No. Manifiesto, normas, notas de vestimenta, preguntas y la página legal son borradores a la espera de aprobación.</p></div></details></div></section>
""",
    "contact": f"""
<section class="page-hero"><div class="wrap"><p class="kicker">Un destino</p><h1>Contacto</h1><p class="lede">En esta página no hay formulario, y nada de aquí dice que un mensaje se haya enviado.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p>El destino verificado es el perfil de Instagram <a class="external" href="{IG}" rel="noreferrer noopener">@lx.nsty</a>.</p><p>Su texto público describe ropa de látex hecha en Barcelona y pide un mensaje directo para pedidos. Escribir a esa cuenta llega a quien opera ese perfil. Esta previsualización no puede confirmar que un mensaje se lea como consulta de noches.</p><p>No hay correo publicado, ni taquilla, ni acceso de miembros.</p></div></section>
""",
    "access": """
<section class="page-hero"><div class="wrap"><p class="kicker">No habilitado</p><h1>Acceso</h1><p class="lede">El acceso de miembros no está habilitado. Este servidor no tiene sistema de cuentas.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p>No hay campo de contraseña, ni registro, ni cuenta con la que entrar. Cuando exista una puerta real, esta página se sustituirá. Hasta entonces no hay nada que enviar.</p><div class="link-row"><a href="/test/es/">Inicio de la previsualización</a><a href="/test/es/contacto/">Contacto</a></div></div></section>
""",
    "legal": """
<section class="page-hero"><div class="wrap"><p class="kicker">Borrador, no es un aviso legal vigente</p><h1>Aviso legal</h1><p class="lede">No se han facilitado el nombre legal, el domicilio, el identificador ni el contacto de quien opera el sitio. Los huecos de abajo son datos que faltan.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>Titular, pendiente</h2><dl class="pending-fields"><dt>Denominación</dt><dd>Pendiente — no facilitada</dd><dt>NIF, CIF u otro número</dt><dd>Pendiente — no facilitado</dd><dt>Domicilio</dt><dd>Pendiente — no facilitado</dd><dt>Correo</dt><dd>Pendiente — no facilitado</dd><dt>Datos registrales</dt><dd>Pendiente — no facilitados</dd></dl><p class="callout">Un aviso para un sitio orientado a España suele nombrar a la persona o sociedad responsable. Ese nombre no se ha dado. Esta página no lo inventa.</p></div></section>
<section class="band"><div class="wrap prose"><h2>Qué hace esta versión</h2><p>Es una previsualización estática. No anuncia un evento y no vende nada. No tiene acceso de miembros. No pone cookies, no carga analítica y no envía ningún formulario, porque no hay formulario. Esa frase describe la versión. No es una política de privacidad inscrita.</p><p>El único enlace de salida es el perfil de Instagram @lx.nsty. Este sitio no controla ese perfil.</p><p>La marca NSTY de la cabecera es una reconstrucción angular de la línea inferior de la marca de la cuenta, sin la línea superior LX. No se presenta como un calco exacto al píxel. Las fotografías entran solo si se aportan como publicaciones de autoría o coautoría. Las marcas dentro de esas fotografías no se han tapado.</p><p>Se está preparando un alojamiento dedicado para este dominio. Esta página no nombra un responsable ni un alojador como si el registro estuviera completo.</p><p>El fuero, la sociedad y la ley aplicable los tiene que fijar quien opere el sitio, con asesoramiento. Este borrador no elige ninguno. Hay que sustituir esta página antes de presentarla como aviso legal.</p></div></section>
""",
}


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
<img src="/assets/img/nsty-wordmark.svg" alt="NSTY" title="NSTY" width="930" height="420">
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
