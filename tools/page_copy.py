"""Proposed nightlife copy. Drafts, not confirmed door policy."""

BODIES = {
    "en": {
        "home": """
<section class="hero"><div class="wrap"><p class="kicker">After dark</p><h1>NSTY</h1><p class="lede">Latex, low light, and the long walk onto the floor. The night is still being written. The date comes later.</p></div></section>
<section class="band"><div class="wrap">{fig:runway:eager}</div></section>
<section class="band band-metal"><div class="wrap prose"><h2>Shine, then shadow</h2><p>A glove past the wrist. A collar that catches the lamp. Feather against a hard shine. NSTY nights takes its temperature from that look: dressed, deliberate, and close to the music.</p><p>What you see here is the mood. The room, the lineup, and the door are coming soon.</p></div></section>
<section class="band"><div class="wrap split">{fig:outdoor-latex}<div class="prose"><h2>Cut in latex</h2><p>Black, brown, and a flash of metal. Clothes that hold the light and give it back. This is the wardrobe the night is leaning toward, not a list of what you must wear.</p><div class="link-row"><a href="/test/dress-code/">Dress code</a><a href="/test/photos/">Photos</a></div></div></div></section>
<section class="band band-metal"><div class="wrap split reverse"><div class="prose"><h2>Coming soon</h2><dl class="status-list"><dt>Date</dt><dd>Coming soon</dd><dt>Room</dt><dd>Coming soon</dd><dt>Line-up</dt><dd>Coming soon</dd><dt>Tickets</dt><dd>Coming soon</dd></dl><div class="link-row"><a href="/test/manifest/">Manifest</a><a href="/test/contact/">Contact</a></div></div>{fig:monochrome-portrait}</div></section>
<section class="band"><div class="wrap">{fig:backstage-latex}</div></section>
""",
        "manifest": """
<section class="page-hero"><div class="wrap"><p class="kicker">Proposed</p><h1>Manifest</h1><p class="lede">A working text for the night. It sets a tone. It does not open a door.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>After the lights drop</h2><p>The good hour is the one where the room gets quieter in the head and louder in the body. People arrive already decided: latex, tailoring, or something darker and simpler. The point is to be present, not to be explained.</p></div></section>
<section class="band"><div class="wrap prose"><h2>Material before myth</h2><p>Latex is a surface. It takes fingerprints of light and keeps a shape. Around it: hardware, feather, a clean black line. NSTY is that palette, stretched into a night. The clothing is made in Barcelona. The night itself has not been given a room yet.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>The floor stays unfinished</h2><p>Until a date is printed, there is no guest list hiding in the silence. A manifesto can want a room. It cannot pretend the room is already booked.</p></div></section>
""",
        "rules": """
<section class="page-hero"><div class="wrap"><p class="kicker">Proposed, not in force</p><h1>Rules</h1><p class="lede">Short notes for a night that has no door yet.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><ol class="stack"><li>Nothing on this site is an invitation by itself.</li><li>A note about clothes is not a condition of entry.</li><li>Another person’s body is not a photograph you are owed.</li></ol></div></section>
<section class="band"><div class="wrap prose"><h2>Not set</h2><dl class="status-list"><dt>Age</dt><dd>Not set</dd><dt>Admission</dt><dd>Not set</dd><dt>Cameras</dt><dd>Not set</dd><dt>Care</dt><dd>Not set</dd></dl></div></section>
""",
        "photos": """
<section class="page-hero"><div class="wrap"><p class="kicker">Looks</p><h1>Photos</h1><p class="lede">Latex, runway, and the hour backstage. The archive at the bottom is a past poster, not the next date.</p></div></section>
<section class="band"><div class="wrap"><ul class="gallery"><li>{fig:outdoor-latex}</li><li>{fig:backstage-latex}</li><li>{fig:monochrome-portrait}</li><li>{fig:runway}</li><li>{fig:white-latex}</li></ul></div></section>
<section class="band band-metal" id="archive"><div class="wrap prose"><h2>Archive</h2><p>A past poster. Not a coming date.</p>{fig:archive-2025-poster}</div></section>
""",
        "dress": """
<section class="page-hero"><div class="wrap"><p class="kicker">Proposed</p><h1>Dress code</h1><p class="lede">A direction, not a rule of entry. Wear the night, or wear black and mean it.</p></div></section>
<section class="band"><div class="wrap category-grid"><article class="split">{fig:outdoor-latex}<div class="prose"><h2>Latex</h2><p>The house color is shine: black, brown, and the hard highlight along a seam. Gloves and a collar belong in the same sentence.</p></div></article><article class="split reverse"><div class="prose"><h2>Backstage black</h2><p>Dark latex, a mask, the corridor before the light. Useful if you want the night without a costume speech.</p></div>{fig:backstage-latex}</article><article class="split">{fig:white-latex}<div class="prose"><h2>Pale latex</h2><p>White with a black graphic, a long drape, a boot with height. The mark in that photograph belongs to the event that printed it.</p></div></article><article class="split reverse"><div class="prose"><h2>Fur and hardware</h2><p>A coat with weight, a harness, a collar. Texture against shine. Plain dark clothes are welcome too. This page does not turn anyone away.</p></div>{fig:monochrome-portrait}</article></div></section>
""",
        "faq": """
<section class="page-hero"><div class="wrap"><p class="kicker">Short answers</p><h1>FAQ</h1></div></section>
<section class="band"><div class="wrap"><details class="faq-item"><summary>When is the next night?</summary><div class="answer"><p>Coming soon. No date is posted.</p></div></details><details class="faq-item"><summary>Where is it?</summary><div class="answer"><p>Coming soon. No room is posted.</p></div></details><details class="faq-item"><summary>Can I buy a ticket?</summary><div class="answer"><p>Coming soon. There is no sales link.</p></div></details><details class="faq-item"><summary>How do I write to you?</summary><div class="answer"><p>Instagram, on the contact page. There is no form here.</p></div></details><details class="faq-item"><summary>Is there an age limit?</summary><div class="answer"><p>Not set.</p></div></details><details class="faq-item"><summary>What should I wear?</summary><div class="answer"><p>See the dress page. It is a proposal, not a condition of entry.</p></div></details><details class="faq-item"><summary>Is the 2025 poster a future date?</summary><div class="answer"><p>No. It sits in the photo archive as a past record.</p></div></details><details class="faq-item"><summary>Is member access open?</summary><div class="answer"><p>No. There is nothing to sign in to.</p></div></details></div></section>
""",
        "contact": """
<section class="page-hero"><div class="wrap"><p class="kicker">Write</p><h1>Contact</h1><p class="lede">One door, and it is not a form.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p><a class="external" href="https://www.instagram.com/lx.nsty/" rel="noreferrer noopener">Instagram · @lx.nsty</a></p><p>The profile is the clothing line: latex made in Barcelona, orders by direct message. For the night, that is also the only published way to write. Nothing on this page confirms that a message was sent.</p></div></section>
""",
        "access": """
<section class="page-hero"><div class="wrap"><p class="kicker">Closed</p><h1>Access</h1><p class="lede">Member access is not open.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p>There is no sign-in on this preview, and no password to give. When a real door exists, this page will change.</p><div class="link-row"><a href="/test/">Home</a><a href="/test/contact/">Contact</a></div></div></section>
""",
        "legal": """
<section class="page-hero"><div class="wrap"><p class="kicker">Draft</p><h1>Legal notice</h1><p class="lede">The operator’s name, address, and contact are not published yet.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><dl class="pending-fields"><dt>Legal name</dt><dd>Not yet published</dd><dt>Identifier</dt><dd>Not yet published</dd><dt>Address</dt><dd>Not yet published</dd><dt>Email</dt><dd>Not yet published</dd></dl></div></section>
<section class="band"><div class="wrap prose"><p>This preview does not sell tickets, does not open accounts, and does not set cookies. The only outside link is Instagram @lx.nsty. Replace this page before it is treated as a statutory notice.</p></div></section>
""",
    }
}

BODIES["es"] = {
    "home": """
<section class="hero"><div class="wrap"><p class="kicker">Después de oscurecer</p><h1>NSTY</h1><p class="lede">Látex, poca luz y el camino largo hasta la pista. La noche todavía se está escribiendo. La fecha llega después.</p></div></section>
<section class="band"><div class="wrap">{fig:runway:eager}</div></section>
<section class="band band-metal"><div class="wrap prose"><h2>Brillo, luego sombra</h2><p>Un guante más allá de la muñeca. Un collar que toma la lámpara. Pluma contra un brillo duro. Las noches NSTY salen de esa imagen: vestidas, deliberadas, cerca de la música.</p><p>Esto es el clima. La sala, el cartel y la puerta están por llegar.</p></div></section>
<section class="band"><div class="wrap split">{fig:outdoor-latex}<div class="prose"><h2>Cortado en látex</h2><p>Negro, marrón y un destello de metal. Ropa que guarda la luz y la devuelve. Es el vestuario hacia el que se inclina la noche, no una lista de lo obligatorio.</p><div class="link-row"><a href="/test/es/dress-code/">Dress code</a><a href="/test/es/fotos/">Fotos</a></div></div></div></section>
<section class="band band-metal"><div class="wrap split reverse"><div class="prose"><h2>Próximamente</h2><dl class="status-list"><dt>Fecha</dt><dd>Próximamente</dd><dt>Sala</dt><dd>Próximamente</dd><dt>Cartel</dt><dd>Próximamente</dd><dt>Entradas</dt><dd>Próximamente</dd></dl><div class="link-row"><a href="/test/es/manifiesto/">Manifiesto</a><a href="/test/es/contacto/">Contacto</a></div></div>{fig:monochrome-portrait}</div></section>
<section class="band"><div class="wrap">{fig:backstage-latex}</div></section>
""",
    "manifest": """
<section class="page-hero"><div class="wrap"><p class="kicker">Propuesta</p><h1>Manifiesto</h1><p class="lede">Un texto de trabajo para la noche. Marca un tono. No abre una puerta.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>Cuando cae la luz</h2><p>La buena hora es aquella en que la sala se calla en la cabeza y sube en el cuerpo. La gente llega ya decidida: látex, sastrería, o algo más oscuro y simple. La idea es estar, no explicarse.</p></div></section>
<section class="band"><div class="wrap prose"><h2>Materia antes que mito</h2><p>El látex es una superficie. Recoge la luz y guarda una forma. Alrededor: metal, pluma, una línea negra limpia. NSTY es esa paleta estirada hasta una noche. La ropa se hace en Barcelona. A la noche todavía no se le ha dado una sala.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><h2>La pista sigue abierta</h2><p>Hasta que se imprima una fecha, el silencio no esconde una lista. Un manifiesto puede desear una sala. No puede fingir que la sala ya está reservada.</p></div></section>
""",
    "rules": """
<section class="page-hero"><div class="wrap"><p class="kicker">Propuesta, no vigente</p><h1>Normas</h1><p class="lede">Notas breves para una noche que todavía no tiene puerta.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><ol class="stack"><li>Nada en este sitio es, por sí solo, una invitación.</li><li>Una nota sobre la ropa no es una condición de entrada.</li><li>El cuerpo de otra persona no es una fotografía debida.</li></ol></div></section>
<section class="band"><div class="wrap prose"><h2>Sin fijar</h2><dl class="status-list"><dt>Edad</dt><dd>Sin fijar</dd><dt>Admisión</dt><dd>Sin fijar</dd><dt>Cámaras</dt><dd>Sin fijar</dd><dt>Cuidado</dt><dd>Sin fijar</dd></dl></div></section>
""",
    "photos": """
<section class="page-hero"><div class="wrap"><p class="kicker">Imágenes</p><h1>Fotos</h1><p class="lede">Látex, pasarela y la hora del camerino. El archivo de abajo es un cartel pasado, no la próxima fecha.</p></div></section>
<section class="band"><div class="wrap"><ul class="gallery"><li>{fig:outdoor-latex}</li><li>{fig:backstage-latex}</li><li>{fig:monochrome-portrait}</li><li>{fig:runway}</li><li>{fig:white-latex}</li></ul></div></section>
<section class="band band-metal" id="archive"><div class="wrap prose"><h2>Archivo</h2><p>Un cartel pasado. No es una fecha que viene.</p>{fig:archive-2025-poster}</div></section>
""",
    "dress": """
<section class="page-hero"><div class="wrap"><p class="kicker">Propuesta</p><h1>Dress code</h1><p class="lede">Una dirección, no una norma de entrada. Viste la noche, o viste de negro y que se note.</p></div></section>
<section class="band"><div class="wrap category-grid"><article class="split">{fig:outdoor-latex}<div class="prose"><h2>Látex</h2><p>El color de la casa es el brillo: negro, marrón y el filo de luz en una costura. Los guantes y el collar van en la misma frase.</p></div></article><article class="split reverse"><div class="prose"><h2>Negro de camerino</h2><p>Látex oscuro, una máscara, el pasillo antes de la luz. Sirve si quieres la noche sin un discurso de disfraz.</p></div>{fig:backstage-latex}</article><article class="split">{fig:white-latex}<div class="prose"><h2>Látex claro</h2><p>Blanco con un gráfico negro, una caída larga, una bota con altura. La marca de esa fotografía pertenece al evento que la imprimió.</p></div></article><article class="split reverse"><div class="prose"><h2>Pelo y metal</h2><p>Un abrigo con peso, un arnés, un collar. Textura contra brillo. La ropa oscura sencilla también cabe. Esta página no echa a nadie.</p></div>{fig:monochrome-portrait}</article></div></section>
""",
    "faq": """
<section class="page-hero"><div class="wrap"><p class="kicker">Respuestas breves</p><h1>FAQ</h1></div></section>
<section class="band"><div class="wrap"><details class="faq-item"><summary>¿Cuándo es la próxima noche?</summary><div class="answer"><p>Próximamente. No hay fecha publicada.</p></div></details><details class="faq-item"><summary>¿Dónde es?</summary><div class="answer"><p>Próximamente. No hay sala publicada.</p></div></details><details class="faq-item"><summary>¿Puedo comprar una entrada?</summary><div class="answer"><p>Próximamente. No hay enlace de venta.</p></div></details><details class="faq-item"><summary>¿Cómo os escribo?</summary><div class="answer"><p>Por Instagram, en la página de contacto. Aquí no hay formulario.</p></div></details><details class="faq-item"><summary>¿Hay un límite de edad?</summary><div class="answer"><p>Sin fijar.</p></div></details><details class="faq-item"><summary>¿Qué hay que llevar?</summary><div class="answer"><p>Mira la página de vestimenta. Es una propuesta, no una condición de entrada.</p></div></details><details class="faq-item"><summary>¿El cartel de 2025 es una fecha futura?</summary><div class="answer"><p>No. Está en el archivo de fotos como un registro pasado.</p></div></details><details class="faq-item"><summary>¿El acceso de miembros está abierto?</summary><div class="answer"><p>No. No hay dónde entrar.</p></div></details></div></section>
""",
    "contact": """
<section class="page-hero"><div class="wrap"><p class="kicker">Escribir</p><h1>Contacto</h1><p class="lede">Una puerta, y no es un formulario.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p><a class="external" href="https://www.instagram.com/lx.nsty/" rel="noreferrer noopener">Instagram · @lx.nsty</a></p><p>El perfil es la línea de ropa: látex hecho en Barcelona, pedidos por mensaje directo. Para la noche, es también la única vía publicada. Nada en esta página confirma que un mensaje se haya enviado.</p></div></section>
""",
    "access": """
<section class="page-hero"><div class="wrap"><p class="kicker">Cerrado</p><h1>Acceso</h1><p class="lede">El acceso de miembros no está abierto.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><p>En esta previsualización no hay inicio de sesión ni contraseña que dar. Cuando exista una puerta de verdad, esta página cambiará.</p><div class="link-row"><a href="/test/es/">Inicio</a><a href="/test/es/contacto/">Contacto</a></div></div></section>
""",
    "legal": """
<section class="page-hero"><div class="wrap"><p class="kicker">Borrador</p><h1>Aviso legal</h1><p class="lede">El nombre, el domicilio y el contacto de quien opera el sitio todavía no se publican.</p></div></section>
<section class="band band-metal"><div class="wrap prose"><dl class="pending-fields"><dt>Denominación</dt><dd>Sin publicar</dd><dt>Identificador</dt><dd>Sin publicar</dd><dt>Domicilio</dt><dd>Sin publicar</dd><dt>Correo</dt><dd>Sin publicar</dd></dl></div></section>
<section class="band"><div class="wrap prose"><p>Esta previsualización no vende entradas, no abre cuentas y no pone cookies. El único enlace exterior es Instagram @lx.nsty. Hay que sustituir esta página antes de tratarla como un aviso legal.</p></div></section>
""",
}
