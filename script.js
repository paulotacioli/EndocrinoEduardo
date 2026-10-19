(function () {
  var nav = document.querySelector('.nav');

  // Toda pagina abre no topo (sem herdar a posicao de rolagem da pagina anterior),
  // exceto quando a URL traz uma ancora (#diabetes, #telemedicina...)
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  if (!location.hash) {
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    window.addEventListener('pageshow', function () {
      if (!location.hash) window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    });
  }

  // Menu mobile
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      toggle.querySelector('i').className = open ? 'ph ph-x' : 'ph ph-list';
    });
  }

  // Cabecalho solido ao rolar (sem listener de scroll)
  var sentinel = document.createElement('div');
  sentinel.style.cssText = 'position:absolute;top:0;height:1px;width:1px;';
  document.body.prepend(sentinel);
  if ('IntersectionObserver' in window && nav) {
    new IntersectionObserver(function (entries) {
      nav.classList.toggle('is-scrolled', !entries[0].isIntersecting);
    }, { rootMargin: '40px 0px 0px 0px' }).observe(sentinel);
  }

  // Escalonamento: cada item de uma lista recebe um indice (--i)
  document.querySelectorAll('.strip, .cards, .tiles, .steps, .posts, .areas, .pillars, .contato-band, .two-col, .welcome__inner')
    .forEach(function (parent) {
      Array.prototype.forEach.call(parent.children, function (el, i) {
        el.style.setProperty('--i', String(i % 6));
      });
    });

  // Aparicao ao rolar: o CSS usa animation-timeline quando ha suporte;
  // caso contrario, IntersectionObserver (respeita prefers-reduced-motion)
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var scrollTimeline = window.CSS && CSS.supports && CSS.supports('animation-timeline: view()');
  if (!reduce && !scrollTimeline && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('js-reveal');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  }

  var ano = document.getElementById('ano');
  if (ano) ano.textContent = String(new Date().getFullYear());
})();
