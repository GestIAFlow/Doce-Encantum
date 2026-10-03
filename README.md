# Doce Encantum Floricultura — site institucional

Site estático (HTML + CSS + JS puro) para o GitHub Pages. Floricultura em Caxias do Sul.

## Páginas

| Arquivo | Página |
|---|---|
| `index.html` | Home: chamada principal, caminhos rápidos, "Flores para cada momento da vida", serviços, portfólio, depoimentos |
| `quem-somos.html` | Nossa história, essência e estrutura |
| `eventos.html` | Casamentos, 15 anos, formaturas, aniversários, corporativos, bodas e noivados |
| `decoracao-floral.html` | O que fazemos no evento: arranjos, altares, arcos, mesas, cenários |
| `noivas.html` | Buquê de noiva, madrinhas, daminhas, lapelas, acessórios, cerimônia |
| `presentes.html` | Buquês, arranjos, plantas e orquídeas, cestas e kits, corporativos, botão da loja virtual |
| `homenagens.html` | Coroas e flores para despedidas (visual sóbrio) |
| `portfolio.html` | "Histórias que floresceram" com filtros e "Histórias de clientes" |
| `inspiracoes.html` | Paletas para noivas, significado das flores, cuidados, datas especiais |
| `contato.html` | Formulário de orçamento (envia pelo WhatsApp), contatos, endereço, mapa |

## Configuração rápida (`script.js`, no topo)

- `whatsappNumero`: número com DDI + DDD (ex.: `5554999999999`). Com ele, o formulário abre o WhatsApp com a mensagem pronta.
- `lojaVirtual`: endereço do e-commerce. Todos os botões "Loja virtual" passam a apontar para ele.
  (Até lá, eles levam ao WhatsApp do catálogo.)

## Conteúdo a preencher antes de publicar

Procure por `[` nos arquivos HTML. Os textos entre colchetes são espaços reservados:

- **Depoimentos**: `index.html` e `portfolio.html`
- **História real** da floricultura: `quem-somos.html`
- **Endereço e horários**: `contato.html` (troque também o `q=` do mapa pelo endereço completo)

**Fotos.** Os blocos coloridos com legenda em itálico (`<div class="ph">`) são espaços para fotos reais.
Coloque as imagens em `assets/` e troque cada bloco por:

```html
<img src="assets/portfolio/casamento-01.jpg" alt="Descrição da foto" loading="lazy">
```

No portfólio, mantenha o `<figure class="projeto" data-cat="...">` para os filtros continuarem funcionando.

## Editar menu, rodapé ou várias páginas (opcional)

As páginas são geradas a partir de `_fonte/`. Cabeçalho, menu e rodapé ficam em `_fonte/build.py`,
e o conteúdo de cada página em `_fonte/paginas/`. Depois de editar, rode:

```
python _fonte/build.py
```

Pequenas correções de texto também podem ser feitas direto nos `.html` da raiz. Só lembre que
rodar o build depois sobrescreve essas edições.

## Publicar no GitHub Pages

1. Crie um repositório no GitHub e envie os arquivos desta pasta para a branch `main`.
2. **Settings → Pages → Build and deployment**: *Deploy from a branch*, `main`, `/ (root)` → **Save**.
3. Em alguns minutos o site fica em `https://SEU-USUARIO.github.io/NOME-DO-REPO/`.

Para domínio próprio (ex.: `www.doceencantum.com.br`): **Settings → Pages → Custom domain**.
