# -*- coding: utf-8 -*-
"""Gera as paginas HTML do site a partir de um cabecalho e rodape comuns.

Uso:  python build_pages.py
Edite o conteudo em PAGES / AREAS e rode o script para regravar os .html.
As imagens em assets/img sao provisorias (fotos genericas): troque pelos
arquivos definitivos mantendo os mesmos nomes.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
WA = ("https://wa.me/5551982283389?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20"
      "consulta%20com%20o%20Dr.%20Eduardo%20Rocha.")
MAPS = ("https://www.google.com/maps/search/?api=1&query=Av.+Jos%C3%A9+Loureiro+da+Silva,"
        "+2025,+Centro,+Gravata%C3%AD+-+RS,+94010-001")
MAP_EMBED = ("https://www.google.com/maps?q=Av.+Jos%C3%A9+Loureiro+da+Silva,+2025,+Centro,"
             "+Gravata%C3%AD+-+RS,+94010-001&output=embed")
IG = "https://www.instagram.com/dreduardorocha.endocrino/"
IG_HL_DIABETES = "https://www.instagram.com/stories/highlights/17994834278301123/"
IG_HL_EXERCICIO = "https://www.instagram.com/stories/highlights/18192440029203830/"
PRONOVA = "https://pronovatech.com.br/"
PRONOVA_LOGO = """<span class="pronova__logo" aria-hidden="true"><span class="pronova__mark"><svg width="20" height="20" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><polygon points="2,3 38,3 20,20" fill="#FFFFFF"/><polygon points="2,37 38,37 20,20" fill="#5BAEE8"/><line x1="2" y1="20" x2="38" y2="20" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/></svg></span><span class="pronova__word"><span class="pronova__pro">Pro</span><span class="pronova__nova">nova</span></span></span>"""

NAV = [
    ("index.html", "Página inicial"),
    ("profissional.html", "O profissional"),
    ("atuacao.html", "Atuação"),
    ("consulta.html", "A consulta"),
    ("contato.html", "Contato"),
]

# slug, icone, nome, descricao
AREAS = [
    ("diabetes", "drop", "Diabetes mellitus",
     "Acompanhamento do diabetes tipo 1, tipo 2 e do pré-diabetes, com foco no controle da glicemia, "
     "na prevenção de complicações e na escolha do tratamento mais adequado para cada pessoa, "
     "incluindo as novas classes de medicamentos e a monitorização contínua da glicose."),
    ("bombas-de-insulina", "pulse", "Bombas de insulina",
     "A bomba de insulina é uma opção para pessoas com diabetes tipo 1. O dispositivo faz a infusão "
     "contínua de insulina basal e as doses em bolus nas refeições. O acompanhamento inclui a "
     "indicação, a instalação, o ajuste das configurações e a educação para o uso no dia a dia."),
    ("tireoide", "butterfly", "Doenças da tireoide",
     "Diagnóstico e tratamento de hipotireoidismo, hipertireoidismo, tireoidites e nódulos de "
     "tireoide, com interpretação cuidadosa dos exames e ajuste do tratamento ao longo do tempo."),
    ("obesidade", "scales", "Obesidade e emagrecimento",
     "Avaliação individualizada e abordagem integral do peso, considerando histórico, hábitos, "
     "exames e condições associadas. O plano combina orientação alimentar, atividade física e, "
     "quando indicado, tratamento medicamentoso, com metas realistas e acompanhamento."),
    ("menopausa", "flower", "Menopausa",
     "Avaliação dos sintomas do climatério e da menopausa, orientação sobre saúde óssea e "
     "cardiovascular nessa fase e indicação de terapia hormonal quando apropriada e segura."),
    ("osteoporose", "bone", "Osteoporose",
     "Avaliação da saúde óssea, interpretação da densitometria e dos exames laboratoriais, "
     "prevenção de fraturas e tratamento medicamentoso quando indicado."),
    ("colesterol", "heartbeat", "Colesterol",
     "Diagnóstico e tratamento das dislipidemias, com avaliação do risco cardiovascular e "
     "definição de metas e de tratamento conforme o perfil de cada pessoa."),
    ("hipofise-adrenal", "brain", "Hipófise e adrenal",
     "Investigação e acompanhamento de alterações hormonais da hipófise e das adrenais, como "
     "alterações de prolactina, cortisol, hormônio do crescimento e nódulos adrenais."),
]


def head(title, desc, active):
    links = "\n".join(
        f'        <a href="{href}"{" class=\"is-active\" aria-current=\"page\"" if href == active else ""}>{label}</a>'
        for href, label in NAV)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#7FA653">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="assets/eduardo-hero.jpg">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=Inter:wght@700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="vendor/phosphor/phosphor.css">
  <link rel="stylesheet" href="styles.css">
</head>
<body data-page="{active}">
  <a class="skip" href="#conteudo">Ir para o conteúdo</a>

  <header class="nav">
    <div class="container nav__inner">
      <a class="brand" href="index.html" aria-label="Eduardo Rocha, página inicial">
        <span class="brand__mark" aria-hidden="true">ER</span>
        <span class="brand__text">
          <strong>Eduardo Rocha</strong>
          <span>Endocrinologista e Metabologista</span>
        </span>
      </a>

      <nav class="nav__links" id="menu" aria-label="Principal">
{links}
      </nav>

      <a class="btn btn--solid nav__cta" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>

      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="menu" aria-label="Abrir menu">
        <i class="ph ph-list" aria-hidden="true"></i>
      </button>
    </div>
  </header>

  <main id="conteudo">
"""


FOOT = f"""  </main>

  <footer class="footer">
    <div class="band band--dark">
      <div class="container contato-band">
        <div class="contato-band__col reveal">
          <h2 class="h-light">Endereço</h2>
          <p>Av. José Loureiro da Silva, 2025, Sala 1001<br>Centro, Gravataí/RS<br>CEP 94010-001</p>
          <a class="link" href="{MAPS}" target="_blank" rel="noopener">Ver no mapa</a>
        </div>
        <div class="contato-band__col reveal">
          <h2 class="h-light">Agende a consulta</h2>
          <p>WhatsApp e telefone<br><a class="link" href="https://wa.me/5551982283389" target="_blank" rel="noopener">(51) 98228-3389</a></p>
          <p><a class="link" href="mailto:dreduardoaarocha@gmail.com">dreduardoaarocha@gmail.com</a></p>
          <a class="btn btn--solid" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>
        </div>
        <div class="contato-band__col contato-band__social reveal">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram do Dr. Eduardo Rocha">
            <i class="ph ph-instagram-logo" aria-hidden="true"></i>
            <span>@dreduardorocha.endocrino</span>
          </a>
        </div>
      </div>
    </div>
    <div class="container footer__inner">
      <span>© <span id="ano">2026</span> Eduardo Rocha</span>
      <span>Endocrinologista e Metabologista</span>
      <span>CRM-RS 60761 | RQE 73103</span>
      <a class="pronova pronova--footer" href="{PRONOVA}" target="_blank" rel="noopener" aria-label="Assinante da plataforma Pronova Tech">
        <span class="pronova__label">Assinante da plataforma</span>{PRONOVA_LOGO}
      </a>
    </div>
  </footer>

  <script src="script.js" defer></script>
</body>
</html>
"""


def page_head(title, intro, image):
    return f"""    <section class="page-head" style="--bg: url('assets/img/{image}')">
      <div class="page-head__bg" aria-hidden="true"></div>
      <div class="container page-head__inner">
        <h1 class="h-upper">{title}</h1>
        <p>{intro}</p>
      </div>
    </section>
"""


CTA_BAND = f"""    <section class="parallax parallax--cta" style="--bg: url('assets/img/parallax-cta.jpg')">
      <div class="parallax__bg" aria-hidden="true"></div>
      <div class="container parallax__inner reveal">
        <h2 class="h-upper">Agende sua consulta</h2>
        <p>Atendimento presencial em Gravataí/RS ou por telemedicina para todo o Brasil.</p>
        <div class="actions actions--center">
          <a class="btn btn--solid" href="{WA}" target="_blank" rel="noopener">Agendar pelo WhatsApp</a>
          <a class="btn btn--outline-light" href="contato.html">Ver contato</a>
        </div>
      </div>
    </section>
"""


def tiles(link_prefix):
    return "\n".join(
        f'''          <li class="reveal"><a class="tile" href="{link_prefix}#{slug}"><i class="ph ph-{icon}" aria-hidden="true"></i><span>{name}</span></a></li>'''
        for slug, icon, name, _ in AREAS)


# ---------------------------------------------------------------- paginas

INDEX = f"""    <section class="hero" style="--bg: url('assets/img/hero-bg.jpg')">
      <div class="hero__bg" aria-hidden="true"></div>
      <div class="container hero__inner">
        <div class="hero__copy">
          <p class="eyebrow">Endocrinologista e Metabologista</p>
          <h1>Eduardo Rocha</h1>
          <p class="hero__lead">Cuidado com diabetes, tireoide, obesidade e saúde hormonal, com tratamento baseado em evidências. Consultório em Gravataí/RS e telemedicina para todo o Brasil.</p>
          <div class="actions">
            <a class="btn btn--solid" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>
            <a class="btn btn--outline-light" href="profissional.html">Conheça o Dr. Eduardo</a>
          </div>
          <p class="hero__crm">CRM-RS 60761 | RQE 73103</p>
        </div>
        <figure class="hero__figure">
          <div class="hero__frame">
            <img src="assets/eduardo-hero.jpg" width="410" height="640" alt="Dr. Eduardo Rocha, médico endocrinologista, sorrindo em seu consultório" fetchpriority="high">
          </div>
        </figure>
      </div>
    </section>

    <section class="strip-wrap">
      <div class="container">
        <ul class="strip">
          <li class="reveal"><i class="ph ph-users" aria-hidden="true"></i><span>Atendimento de adultos</span></li>
          <li class="reveal"><i class="ph ph-house-line" aria-hidden="true"></i><span>Consultório no centro de Gravataí</span></li>
          <li class="reveal"><i class="ph ph-video-camera" aria-hidden="true"></i><span>Telemedicina para todo o Brasil</span></li>
          <li class="reveal"><i class="ph ph-flask" aria-hidden="true"></i><span>Tratamento com base científica</span></li>
        </ul>
      </div>
    </section>

    <section class="section welcome">
      <div class="container welcome__inner">
        <figure class="welcome__figure reveal">
          <img src="assets/img/welcome.jpg" width="900" height="1100" alt="Ambiente de consultório, imagem provisória" loading="lazy">
        </figure>
        <div class="welcome__text reveal">
          <h2 class="h-light">Olá, seja bem-vindo(a)!</h2>
          <p>Sou Eduardo Rocha, Médico Endocrinologista e Metabologista, com atuação em adultos. Cuido de diabetes, doenças da tireoide, obesidade e alterações hormonais e metabólicas, sempre com uma avaliação ampla da saúde, não apenas do exame alterado.</p>
          <p>Cada decisão de tratamento é explicada e construída junto com você, com base científica e acompanhamento próximo.</p>
          <div class="actions">
            <a class="btn btn--outline" href="profissional.html">Conheça o Dr. Eduardo</a>
            <a class="btn btn--outline" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>
          </div>
        </div>
      </div>
    </section>

    <section class="parallax parallax--cards" style="--bg: url('assets/img/parallax-cards.jpg')">
      <div class="parallax__bg" aria-hidden="true"></div>
      <div class="container">
        <ul class="cards">
          <li class="card reveal">
            <i class="ph ph-stethoscope" aria-hidden="true"></i>
            <h3>Consulta em Endocrinologia e Metabologia</h3>
            <p>Avaliação completa com foco em diabetes, obesidade, saúde da tireoide, alterações metabólicas e equilíbrio hormonal, com plano individualizado e acompanhamento.</p>
            <a class="btn btn--outline" href="consulta.html">Saiba mais</a>
          </li>
          <li class="card reveal">
            <i class="ph ph-drop" aria-hidden="true"></i>
            <h3>Diabetes e novas tecnologias</h3>
            <p>Acompanhamento do diabetes tipo 1 e tipo 2, incluindo bombas de insulina, monitorização contínua da glicose e orientação sobre exercício físico.</p>
            <a class="btn btn--outline" href="atuacao.html#diabetes">Saiba mais</a>
          </li>
          <li class="card reveal">
            <i class="ph ph-video-camera" aria-hidden="true"></i>
            <h3>Presencial ou por telemedicina</h3>
            <p>Consultas no consultório em Gravataí/RS ou on-line para pacientes de todo o Brasil. Retornos e ajustes do tratamento também podem ser feitos a distância.</p>
            <a class="btn btn--outline" href="consulta.html#telemedicina">Saiba mais</a>
          </li>
        </ul>
      </div>
    </section>

    <section class="section band band--green">
      <div class="container atuacao">
        <h2 class="h-upper reveal">Atuação</h2>
        <p class="atuacao__intro reveal">Confira as áreas de atuação do Dr. Eduardo. Clique na opção desejada para saber mais.</p>
        <ul class="tiles">
{tiles("atuacao.html")}
        </ul>
        <div class="actions actions--center reveal">
          <a class="btn btn--outline-dark" href="atuacao.html">Ver atuação completa</a>
          <a class="btn btn--solid" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container consulta">
        <div class="consulta__intro reveal">
          <h2 class="h-light">Como funciona a consulta</h2>
          <p>A consulta começa por entender a sua história: sintomas, hábitos, medicamentos em uso e exames anteriores. A partir disso, o plano de tratamento é definido com você, com explicações sobre cada escolha.</p>
          <div class="actions">
            <a class="btn btn--outline" href="consulta.html">Saiba mais sobre a consulta</a>
          </div>
        </div>
        <ol class="steps">
          <li class="reveal"><span class="steps__n">01</span><div><h3>Avaliação</h3><p>Histórico, sintomas, hábitos e exames revisados em conjunto, sem pressa.</p></div></li>
          <li class="reveal"><span class="steps__n">02</span><div><h3>Diagnóstico</h3><p>Exames necessários e interpretação dos resultados no contexto de cada pessoa.</p></div></li>
          <li class="reveal"><span class="steps__n">03</span><div><h3>Plano individualizado</h3><p>Tratamento definido com você, com metas realistas e orientações práticas.</p></div></li>
          <li class="reveal"><span class="steps__n">04</span><div><h3>Acompanhamento</h3><p>Retornos para ajustar o tratamento conforme a resposta e os novos exames.</p></div></li>
        </ol>
      </div>
    </section>

    <section class="section band band--soft">
      <div class="container">
        <h2 class="h-upper center reveal">Fique por dentro</h2>
        <p class="center muted reveal">Conteúdos do Dr. Eduardo no Instagram.</p>
        <ul class="posts">
          <li class="reveal">
            <a class="post" href="{IG_HL_DIABETES}" target="_blank" rel="noopener">
              <img src="assets/img/post-1.jpg" width="800" height="600" alt="" loading="lazy">
              <span class="post__title">Tópicos sobre diabetes</span>
              <span class="post__more">Ver no Instagram <i class="ph ph-arrow-up-right" aria-hidden="true"></i></span>
            </a>
          </li>
          <li class="reveal">
            <a class="post" href="{IG_HL_EXERCICIO}" target="_blank" rel="noopener">
              <img src="assets/img/post-2.jpg" width="800" height="600" alt="" loading="lazy">
              <span class="post__title">Exercício físico e diabetes tipo 1</span>
              <span class="post__more">Ver no Instagram <i class="ph ph-arrow-up-right" aria-hidden="true"></i></span>
            </a>
          </li>
          <li class="reveal">
            <a class="post" href="{IG}" target="_blank" rel="noopener">
              <img src="assets/img/post-3.jpg" width="800" height="600" alt="" loading="lazy">
              <span class="post__title">Novidades do consultório</span>
              <span class="post__more">Seguir no Instagram <i class="ph ph-arrow-up-right" aria-hidden="true"></i></span>
            </a>
          </li>
        </ul>
      </div>
    </section>

""" + CTA_BAND

PROFISSIONAL = page_head("O profissional", "Conheça o Dr. Eduardo Rocha.", "head-profissional.jpg") + f"""
    <section class="section">
      <div class="container welcome__inner">
        <figure class="welcome__figure reveal">
          <img src="assets/eduardo-hero.jpg" width="410" height="640" alt="Dr. Eduardo Rocha, médico endocrinologista e metabologista" loading="lazy">
        </figure>
        <div class="welcome__text reveal">
          <h2 class="h-light">Dr. Eduardo Augusto Andrade da Rocha</h2>
          <p class="sub">Médico Endocrinologista e Metabologista<br>CRM-RS 60761 | RQE 73103</p>
          <p>Olá! Sou o Dr. Eduardo Augusto Andrade da Rocha, médico graduado pela Universidade Federal de Sergipe (UFS).</p>
          <p>Ao longo da minha formação, realizei Residência Médica em Clínica Médica pelo Hospital do Servidor Público Estadual (IAMSPE), em São Paulo, e, na sequência, um ano opcional de Clínica Médica pela Universidade Federal de São Paulo (UNIFESP). Dei continuidade à minha formação com a Residência em Endocrinologia e Metabologia, também pela UNIFESP, e obtive o Título de Especialista em Endocrinologia e Metabologia pela Sociedade Brasileira de Endocrinologia e Metabologia (SBEM).</p>
          <p>É um prazer poder cuidar da sua saúde com dedicação e atenção em cada etapa do seu tratamento.</p>
          <ul class="facts">
            <li><strong>Graduação</strong><span>Universidade Federal de Sergipe (UFS)</span></li>
            <li><strong>Residências</strong><span>Clínica Médica (IAMSPE e UNIFESP) e Endocrinologia e Metabologia (UNIFESP)</span></li>
            <li><strong>Título</strong><span>Especialista pela SBEM</span></li>
            <li><strong>Registro</strong><span>CRM-RS 60761 | RQE 73103</span></li>
            <li><strong>Público</strong><span>Adultos</span></li>
            <li><strong>Atendimento</strong><span>Presencial em Gravataí/RS e telemedicina</span></li>
          </ul>
          <a class="pronova pronova--card" href="{PRONOVA}" target="_blank" rel="noopener">
            <span class="pronova__label">Assinante da plataforma</span>{PRONOVA_LOGO}
            <span class="pronova__desc">Prontuário com inteligência artificial e transcrição automática da consulta, para mais atenção ao paciente durante o atendimento.</span>
          </a>
          <div class="actions">
            <a class="btn btn--solid" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>
            <a class="btn btn--outline" href="atuacao.html">Ver atuação</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section band band--soft">
      <div class="container">
        <h2 class="h-upper center reveal">Como trabalho</h2>
        <ul class="pillars">
          <li class="reveal"><i class="ph ph-clipboard-text" aria-hidden="true"></i><h3>Avaliação ampla</h3><p>O ponto de partida é a sua história completa, não apenas o exame alterado.</p></li>
          <li class="reveal"><i class="ph ph-flask" aria-hidden="true"></i><h3>Base científica</h3><p>Tratamentos com base nas melhores evidências disponíveis, explicados com clareza.</p></li>
          <li class="reveal"><i class="ph ph-chats-circle" aria-hidden="true"></i><h3>Acompanhamento próximo</h3><p>Retornos e ajustes ao longo do tempo, presencialmente ou a distância.</p></li>
        </ul>
      </div>
    </section>

""" + CTA_BAND

ATUACAO = page_head("Atuação", "Confira a atuação do Dr. Eduardo. Clique na opção desejada para saber mais.", "head-atuacao.jpg") + f"""
    <section class="section band band--green">
      <div class="container atuacao">
        <ul class="tiles tiles--top">
{tiles("")}
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container areas">
{chr(10).join(f'''        <article class="area reveal" id="{slug}">
          <i class="ph ph-{icon}" aria-hidden="true"></i>
          <div>
            <h2 class="h-light">{name}</h2>
            <p>{desc}</p>
          </div>
        </article>''' for slug, icon, name, desc in AREAS)}
      </div>
    </section>

""" + CTA_BAND

CONSULTA = page_head("A consulta", "Como funciona o atendimento com o Dr. Eduardo.", "head-consulta.jpg") + f"""
    <section class="section">
      <div class="container consulta">
        <div class="consulta__intro reveal">
          <h2 class="h-light">Uma avaliação ampla da sua saúde</h2>
          <p>A consulta começa por entender a sua história: sintomas, hábitos, medicamentos em uso, exames anteriores e condições associadas. A partir disso, o diagnóstico e o plano de tratamento são definidos com você, com explicações sobre cada escolha.</p>
          <p>O objetivo é um plano claro, com base científica e que caiba na sua rotina.</p>
        </div>
        <ol class="steps">
          <li class="reveal"><span class="steps__n">01</span><div><h3>Avaliação</h3><p>Histórico, sintomas, hábitos e exames revisados em conjunto, sem pressa.</p></div></li>
          <li class="reveal"><span class="steps__n">02</span><div><h3>Diagnóstico</h3><p>Solicitação dos exames necessários e interpretação dos resultados no contexto de cada pessoa.</p></div></li>
          <li class="reveal"><span class="steps__n">03</span><div><h3>Plano individualizado</h3><p>Tratamento definido com você, com metas realistas e orientações práticas.</p></div></li>
          <li class="reveal"><span class="steps__n">04</span><div><h3>Acompanhamento</h3><p>Retornos para ajustar o tratamento conforme a resposta e os novos exames.</p></div></li>
        </ol>
      </div>
    </section>

    <section class="section band band--soft">
      <div class="container two-col">
        <div class="reveal">
          <i class="ph ph-clipboard-text icon-lg" aria-hidden="true"></i>
          <h2 class="h-light">O que levar na consulta</h2>
          <ul class="list">
            <li>Exames recentes, de sangue e de imagem, mesmo os de outras especialidades.</li>
            <li>Lista dos medicamentos e suplementos em uso, com as doses.</li>
            <li>Registros de glicemia ou dados do sensor, para quem tem diabetes.</li>
            <li>Suas dúvidas anotadas, para que nada fique sem resposta.</li>
          </ul>
        </div>
        <div class="reveal" id="telemedicina">
          <i class="ph ph-video-camera icon-lg" aria-hidden="true"></i>
          <h2 class="h-light">Telemedicina</h2>
          <p>As consultas também podem ser feitas on-line, na modalidade de teleconsulta, para pacientes de todo o Brasil. A primeira consulta, os retornos e os ajustes do tratamento podem acontecer a distância, com a mesma atenção do atendimento presencial.</p>
          <p>Ao agendar, informe se prefere o atendimento presencial em Gravataí/RS ou por telemedicina.</p>
        </div>
      </div>
    </section>

""" + CTA_BAND

CONTATO = page_head("Contato", "Entre em contato pelo WhatsApp ou telefone. Se preferir, envie um e-mail.", "head-contato.jpg") + f"""
    <section class="section">
      <div class="container contato">
        <div class="contato__info reveal">
          <ul class="contato__list">
            <li>
              <i class="ph ph-map-pin" aria-hidden="true"></i>
              <div>
                <strong>Endereço</strong>
                <span>Av. José Loureiro da Silva, 2025, Sala 1001<br>Centro, Gravataí/RS, CEP 94010-001</span>
                <a class="link link--green" href="{MAPS}" target="_blank" rel="noopener">Ver no mapa</a>
              </div>
            </li>
            <li>
              <i class="ph ph-whatsapp-logo" aria-hidden="true"></i>
              <div>
                <strong>WhatsApp e telefone</strong>
                <a href="https://wa.me/5551982283389" target="_blank" rel="noopener">(51) 98228-3389</a>
              </div>
            </li>
            <li>
              <i class="ph ph-envelope-simple" aria-hidden="true"></i>
              <div>
                <strong>E-mail</strong>
                <a href="mailto:dreduardoaarocha@gmail.com">dreduardoaarocha@gmail.com</a>
              </div>
            </li>
            <li>
              <i class="ph ph-instagram-logo" aria-hidden="true"></i>
              <div>
                <strong>Instagram</strong>
                <a href="{IG}" target="_blank" rel="noopener">@dreduardorocha.endocrino</a>
              </div>
            </li>
          </ul>
          <a class="btn btn--solid" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>
        </div>
        <div class="contato__map reveal">
          <iframe
            title="Mapa do consultório do Dr. Eduardo Rocha em Gravataí"
            src="{MAP_EMBED}"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen></iframe>
        </div>
      </div>
    </section>
"""

PAGES = {
    "index.html": ("Eduardo Rocha | Endocrinologista e Metabologista | Gravataí",
                   "Dr. Eduardo Rocha, médico endocrinologista e metabologista em Gravataí/RS. Diabetes, tireoide, obesidade e saúde hormonal. Atendimento presencial e por telemedicina.",
                   INDEX),
    "profissional.html": ("O profissional | Dr. Eduardo Rocha",
                          "Conheça o Dr. Eduardo Rocha, médico endocrinologista e metabologista em Gravataí/RS. CRM-RS 60761 | RQE 73103.",
                          PROFISSIONAL),
    "atuacao.html": ("Atuação | Dr. Eduardo Rocha",
                     "Áreas de atuação do Dr. Eduardo Rocha: diabetes, bombas de insulina, tireoide, obesidade, menopausa, osteoporose, colesterol, hipófise e adrenal.",
                     ATUACAO),
    "consulta.html": ("A consulta | Dr. Eduardo Rocha",
                      "Como funciona a consulta com o Dr. Eduardo Rocha: avaliação ampla, plano individualizado, acompanhamento, atendimento presencial em Gravataí e por telemedicina.",
                      CONSULTA),
    "contato.html": ("Contato | Dr. Eduardo Rocha",
                     "Endereço, WhatsApp, e-mail e Instagram do Dr. Eduardo Rocha, endocrinologista em Gravataí/RS.",
                     CONTATO),
}

if __name__ == "__main__":
    for fname, (title, desc, body) in PAGES.items():
        html = head(title, desc, fname) + body + FOOT
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print("gravado", fname)
