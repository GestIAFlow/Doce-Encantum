/* =========================================================
   CONFIGURAÇÃO — edite aqui
   ========================================================= */
const CONFIG = {
  // Número do WhatsApp com DDI + DDD, só dígitos (ex.: '5554999999999').
  // Com o número preenchido, o formulário de orçamento abre o WhatsApp
  // já com a mensagem escrita. Sem ele, a mensagem é copiada e o
  // link de orçamentos é aberto para o cliente colar.
  whatsappNumero: '',

  // Link de orçamentos usado quando o número acima está vazio.
  whatsappOrcamento: 'https://wa.me/message/QSQCAVRW7TUVM1',

  // Endereço da loja virtual (e-commerce). Todos os botões
  // "Loja virtual" do site passam a apontar para cá.
  lojaVirtual: ''
};

/* ---------- Loja virtual ---------- */
if (CONFIG.lojaVirtual) {
  document.querySelectorAll('.js-loja').forEach((a) => { a.href = CONFIG.lojaVirtual; });
}

/* ---------- Menu ---------- */
const menuBtn = document.querySelector('.menu-btn');
const nav = document.getElementById('menu');

function fecharMenu() {
  nav.classList.remove('aberto');
  menuBtn.setAttribute('aria-expanded', 'false');
  menuBtn.setAttribute('aria-label', 'Abrir menu');
  document.body.style.overflow = '';
}

menuBtn.addEventListener('click', () => {
  const aberto = nav.classList.toggle('aberto');
  menuBtn.setAttribute('aria-expanded', String(aberto));
  menuBtn.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
  document.body.style.overflow = aberto ? 'hidden' : '';
});

// Submenus: botão de seta abre/fecha (teclado no desktop, toque no celular)
document.querySelectorAll('.nav__item--sub').forEach((item) => {
  const toggle = item.querySelector('.sub-toggle');
  toggle.addEventListener('click', () => {
    const aberto = item.classList.toggle('aberto');
    toggle.setAttribute('aria-expanded', String(aberto));
    document.querySelectorAll('.nav__item--sub.aberto').forEach((outro) => {
      if (outro !== item) {
        outro.classList.remove('aberto');
        outro.querySelector('.sub-toggle').setAttribute('aria-expanded', 'false');
      }
    });
  });
  item.addEventListener('focusout', (e) => {
    if (!item.contains(e.relatedTarget) && window.innerWidth > 1120) {
      item.classList.remove('aberto');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
});

nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', fecharMenu));
document.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape') return;
  fecharMenu();
  document.querySelectorAll('.nav__item--sub.aberto').forEach((item) => {
    item.classList.remove('aberto');
    item.querySelector('.sub-toggle').setAttribute('aria-expanded', 'false');
  });
});

/* ---------- Ano no rodapé ---------- */
document.querySelectorAll('.js-ano').forEach((el) => { el.textContent = new Date().getFullYear(); });

/* ---------- Filtro do portfólio ---------- */
const filtros = document.querySelectorAll('.filtro');
if (filtros.length) {
  const projetos = document.querySelectorAll('.projeto');
  const aplicar = (cat) => {
    filtros.forEach((f) => f.setAttribute('aria-pressed', String(f.dataset.filtro === cat)));
    projetos.forEach((p) => { p.hidden = cat !== 'todos' && !p.dataset.cat.split(' ').includes(cat); });
  };
  filtros.forEach((f) => f.addEventListener('click', () => {
    aplicar(f.dataset.filtro);
    history.replaceState(null, '', f.dataset.filtro === 'todos' ? location.pathname : '#' + f.dataset.filtro);
  }));
  const inicial = location.hash.slice(1);
  if ([...filtros].some((f) => f.dataset.filtro === inicial)) aplicar(inicial);
}

/* ---------- Formulário de orçamento ---------- */
const form = document.getElementById('form-orcamento');
if (form) {
  // Pré-seleciona o tipo vindo do link (ex.: contato.html?tipo=casamento)
  const tipo = new URLSearchParams(location.search).get('tipo');
  if (tipo) {
    const opcao = form.querySelector(`input[name="tipo"][value="${CSS.escape(tipo)}"]`);
    if (opcao) opcao.checked = true;
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;

    const d = new FormData(form);
    const rotulo = form.querySelector('input[name="tipo"]:checked')?.dataset.rotulo || 'Outro';
    const dataEvento = d.get('data') ? new Date(d.get('data') + 'T12:00').toLocaleDateString('pt-BR') : '';

    const linhas = [
      'Olá, Doce Encantum! Gostaria de solicitar um orçamento.',
      '',
      `*Orçamento para:* ${rotulo}`,
      `*Nome:* ${d.get('nome')}`,
      dataEvento && `*Data do evento:* ${dataEvento}`,
      d.get('local') && `*Local:* ${d.get('local')}`,
      d.get('convidados') && `*Convidados (aprox.):* ${d.get('convidados')}`,
      `*WhatsApp:* ${d.get('whatsapp')}`,
      d.get('email') && `*E-mail:* ${d.get('email')}`,
      d.get('mensagem') && `\n*Mensagem:* ${d.get('mensagem')}`
    ].filter(Boolean);
    const texto = linhas.join('\n');

    if (CONFIG.whatsappNumero) {
      window.open(`https://wa.me/${CONFIG.whatsappNumero}?text=${encodeURIComponent(texto)}`, '_blank', 'noopener');
      return;
    }

    const aviso = form.querySelector('.form__aviso');
    try {
      await navigator.clipboard.writeText(texto);
      aviso.textContent = 'Sua mensagem foi copiada! Na conversa do WhatsApp que abriu, é só colar e enviar.';
    } catch {
      aviso.textContent = 'Abrimos o WhatsApp para você. Conte para nós os detalhes do seu orçamento por lá.';
    }
    aviso.classList.add('visivel');
    window.open(CONFIG.whatsappOrcamento, '_blank', 'noopener');
  });
}

/* ---------- Animação suave ao rolar ---------- */
if ('IntersectionObserver' in window) {
  const alvos = document.querySelectorAll('.secao__cabeca, .card, .card-foto, .momento, .passos li, .depoimento, .projeto, .bloco__grid > *, .duas-colunas > *, .paleta, .cta');
  const obs = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
      if (!entrada.isIntersecting) return;
      const el = entrada.target;
      el.classList.add('visivel');
      obs.unobserve(el);
      // libera os efeitos de hover depois da animação
      setTimeout(() => el.classList.remove('revelar', 'visivel'), 800);
    });
  }, { threshold: 0.1 });
  alvos.forEach((el) => { el.classList.add('revelar'); obs.observe(el); });
}
