# Site Dr. Eduardo Rocha | Endocrinologista

Site estático com cinco páginas (HTML, CSS e JS puros), sem build.

## Rodar localmente

```bash
python -m http.server 5173 --bind 127.0.0.1
```

Depois abra http://localhost:5173.

## Estrutura

- `index.html`, `profissional.html`, `atuacao.html`, `consulta.html`, `contato.html`: as páginas do site.
- `build_pages.py`: gera as cinco páginas a partir de um cabeçalho e rodapé comuns. Para alterar textos ou o menu, edite este arquivo e rode `python build_pages.py`.
- `styles.css`: estilos (Jost, caixa alta espaçada, botões retos, faixas com imagem em parallax, cartões sobrepostos), paleta #99CD85 e #7FA653, modo claro e escuro automático.
- `script.js`: menu mobile, cabeçalho transparente que fica sólido ao rolar e revelação escalonada ao rolar.
- `assets/eduardo-hero.jpg`: foto do médico (recorte de vídeo, 410x640; trocar por foto em alta resolução).
- `assets/img/`: imagens geradas por IA (ambientes de consultório, sem pessoas) como base. Para trocar por fotos reais, mantenha os nomes:
  - `hero-bg.jpg` (fundo do hero, 1800x1100), `parallax-cards.jpg` e `parallax-cta.jpg` (faixas com parallax, 1800x1000)
  - `welcome.jpg` (foto do consultório, 900x1100), `head-*.jpg` (topo das páginas internas, 1800x800)
  - `post-1.jpg`, `post-2.jpg`, `post-3.jpg` (cards "Fique por dentro", 800x600)
- `vendor/phosphor/`: ícones (subconjunto local da fonte Phosphor).

## Dados usados (Instagram @dreduardorocha.endocrino)

- CRM-RS 60761 | RQE 73103
- WhatsApp: (51) 98228-3389
- E-mail: dreduardoaarocha@gmail.com
- Endereço: Av. José Loureiro da Silva, 2025, Sala 1001, Centro, Gravataí/RS, CEP 94010-001
