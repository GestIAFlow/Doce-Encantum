import json, re, pathlib

AQUI = pathlib.Path(__file__).parent
SAIDA = AQUI.parent

WA = "https://wa.me/message/Z3OEXFNQ4N6IN1"
WA_ORC = "https://wa.me/message/QSQCAVRW7TUVM1"
IG = "https://www.instagram.com/doce_encantum/"
LOJA = WA  # substituído via CONFIG.lojaVirtual no script.js

CHEVRON = '<svg aria-hidden="true" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

MENU = [
    ("home", "Home", "index.html", None),
    ("quem-somos", "Quem somos", "quem-somos.html", None),
    ("eventos", "Eventos", "eventos.html", [
        ("Casamentos", "eventos.html#casamentos"),
        ("15 Anos", "eventos.html#15-anos"),
        ("Formaturas", "eventos.html#formaturas"),
        ("Aniversários e Celebrações", "eventos.html#aniversarios"),
        ("Corporativos", "eventos.html#corporativos"),
        ("Bodas e Noivados", "eventos.html#bodas-noivados"),
        ("Decoração Floral", "decoracao-floral.html"),
    ]),
    ("noivas", "Noivas", "noivas.html", [
        ("Buquês de Noiva", "noivas.html#buque-noiva"),
        ("Flores para Madrinhas", "noivas.html#madrinhas"),
        ("Lapelas", "noivas.html#lapelas"),
        ("Acessórios Florais", "noivas.html#acessorios"),
        ("Inspirações para Noivas", "inspiracoes.html#noivas"),
    ]),
    ("presentes", "Presentes", "presentes.html", [
        ("Buquês", "presentes.html#buques"),
        ("Arranjos", "presentes.html#arranjos"),
        ("Plantas e Orquídeas", "presentes.html#plantas-orquideas"),
        ("Cestas e Kits", "presentes.html#cestas-kits"),
        ("Presentes Corporativos", "presentes.html#corporativos"),
        ("Homenagens e Despedidas", "homenagens.html"),
    ]),
    ("portfolio", "Portfólio", "portfolio.html", None),
    ("inspiracoes", "Inspirações", "inspiracoes.html", None),
    ("contato", "Contato", "contato.html", None),
]


def menu_html(ativo):
    itens = []
    for chave, rotulo, href, sub in MENU:
        cur = ' aria-current="page"' if chave == ativo else ""
        if not sub:
            itens.append(f'<li class="nav__item"><a class="nav__link" href="{href}"{cur}>{rotulo}</a></li>')
            continue
        subs = "".join(f'<li><a href="{h}">{r}</a></li>' for r, h in sub)
        itens.append(
            f'<li class="nav__item nav__item--sub">'
            f'<a class="nav__link" href="{href}"{cur}>{rotulo}</a>'
            f'<button class="sub-toggle" aria-expanded="false" aria-controls="sub-{chave}" aria-label="Abrir submenu {rotulo}">{CHEVRON}</button>'
            f'<ul class="sub" id="sub-{chave}">{subs}</ul></li>'
        )
    return "\n          ".join(itens)


ICONES = (AQUI / "icones.svg").read_text(encoding="utf-8")

LAYOUT = """<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#560B70">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Doce Encantum Floricultura">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="assets/logo-og.jpg">
  <meta property="og:locale" content="pt_BR">
  <link rel="icon" type="image/png" href="assets/favicon.png">
  <link rel="apple-touch-icon" href="assets/favicon.png">
  <link rel="stylesheet" href="style.css">
</head>
<body{body}>

  <a class="skip" href="#conteudo">Pular para o conteúdo</a>

  <header class="topo" id="topo">
    <div class="container topo__inner">
      <a href="index.html" class="topo__logo" aria-label="Doce Encantum Floricultura — página inicial">
        <img src="assets/logo.jpg" alt="Doce Encantum Floricultura" width="640" height="447">
      </a>

      <button class="menu-btn" aria-expanded="false" aria-controls="menu" aria-label="Abrir menu">
        <span></span><span></span><span></span>
      </button>

      <nav class="nav" id="menu" aria-label="Menu principal">
        <ul class="nav__lista">
          {menu}
        </ul>
        <a class="btn btn--amarelo btn--sm js-loja" href="{loja}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-carrinho"/></svg>
          Loja virtual
        </a>
      </nav>
    </div>
  </header>

  <main id="conteudo">
{conteudo}
  </main>

  <footer class="rodape">
    <div class="container">
      <div class="rodape__grid">
        <div class="rodape__marca">
          <img src="assets/logo.jpg" alt="Doce Encantum Floricultura" width="640" height="447" loading="lazy">
          <p>Floricultura em Caxias do Sul. Flores para presentear, celebrar, decorar e homenagear.</p>
        </div>
        <div>
          <h2>Navegue</h2>
          <ul>
            <li><a href="quem-somos.html">Quem somos</a></li>
            <li><a href="portfolio.html">Portfólio</a></li>
            <li><a href="inspiracoes.html">Inspirações</a></li>
            <li><a href="portfolio.html#historias">Histórias de clientes</a></li>
            <li><a href="contato.html">Contato</a></li>
          </ul>
        </div>
        <div>
          <h2>Serviços</h2>
          <ul>
            <li><a href="eventos.html">Eventos</a></li>
            <li><a href="noivas.html">Noivas</a></li>
            <li><a href="decoracao-floral.html">Decoração floral</a></li>
            <li><a href="presentes.html">Flores e presentes</a></li>
            <li><a href="homenagens.html">Homenagens e despedidas</a></li>
          </ul>
        </div>
        <div>
          <h2>Contato</h2>
          <ul>
            <li><a href="{wa}" target="_blank" rel="noopener">WhatsApp — pedidos</a></li>
            <li><a href="{wa_orc}" target="_blank" rel="noopener">WhatsApp — orçamentos</a></li>
            <li><a href="{ig}" target="_blank" rel="noopener">Instagram @doce_encantum</a></li>
            <li><a class="js-loja" href="{loja}" target="_blank" rel="noopener">Loja virtual</a></li>
            <li>Caxias do Sul · RS</li>
          </ul>
        </div>
      </div>
      <div class="rodape__base">
        <span>© <span class="js-ano">2026</span> Doce Encantum Floricultura · Caxias do Sul, RS</span>
        <a href="#topo">Voltar ao topo ↑</a>
      </div>
    </div>
  </footer>

  <a class="whats-float" href="{wa}" target="_blank" rel="noopener" aria-label="Falar pelo WhatsApp">
    <svg aria-hidden="true"><use href="#i-whatsapp"/></svg>
  </a>

{icones}

  <script src="script.js"></script>
</body>
</html>
"""


def topo_pagina(m):
    """Bloco padrão de cabeçalho das páginas internas, montado a partir dos metadados."""
    if "h1" not in m:
        return ""
    crumb = f'<nav class="migalhas" aria-label="Você está em"><a href="index.html">Home</a><span>/</span>{m["crumb"]}</nav>'
    subnav = ""
    if m.get("subnav"):
        subnav = '<nav class="subnav" aria-label="Nesta página">' + "".join(
            f'<a href="{h}">{r}</a>' for r, h in m["subnav"]) + "</nav>"
    return f"""
    <section class="pagina-topo">
      <img class="canto canto--sup" src="assets/flor-canto-sup.jpg" alt="" aria-hidden="true">
      <img class="canto canto--inf" src="assets/flor-canto-inf.jpg" alt="" aria-hidden="true">
      <div class="container">
        {crumb}
        <span class="eyebrow">{m["eyebrow"]}</span>
        <h1>{m["h1"]}</h1>
        <p class="lead">{m["lead"]}</p>
        {subnav}
      </div>
    </section>
"""


for arq in sorted((AQUI / "paginas").glob("*.html")):
    bruto = arq.read_text(encoding="utf-8")
    meta_txt, corpo = re.match(r"<!--(.*?)-->\n(.*)", bruto, re.S).groups()
    m = json.loads(meta_txt)
    corpo = corpo.replace("{WA}", WA).replace("{WA_ORC}", WA_ORC).replace("{IG}", IG).replace("{LOJA}", LOJA)
    html = LAYOUT.format(
        title=m["title"], desc=m["desc"],
        body=f' class="{m["body"]}"' if m.get("body") else "",
        menu=menu_html(m["nav"]), loja=LOJA, wa=WA, wa_orc=WA_ORC, ig=IG,
        conteudo=topo_pagina(m) + corpo.rstrip(), icones=ICONES,
    )
    (SAIDA / arq.name).write_text(html, encoding="utf-8", newline="\n")
    print("ok", arq.name)
