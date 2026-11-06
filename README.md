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
- `assets/eduardo-hero.jpg` (foto em pé, usada no início) e `assets/eduardo-profissional.jpg` (foto sentado, usada em "O profissional"): fotos do médico.
- `assets/img/`: fotos do consultório, recortadas em pixels nativos das originais (cerca de 1060 px de largura). Para trocar, mantenha os nomes:
  - `hero-bg.jpg`, `parallax-cards.jpg`, `parallax-cta.jpg`, `head-*.jpg`: faixas horizontais (16:9). Quanto maior a largura, mais nítidas em telas grandes.
  - `welcome.jpg`: foto vertical (4:5) da recepção, na página inicial.
  - `post-1.jpg`, `post-2.jpg`, `post-3.jpg`: cards "Fique por dentro" (4:3).
- `vendor/phosphor/`: ícones (subconjunto local da fonte Phosphor).

## Dados usados (Instagram @dreduardorocha.endocrino)

- CRM-RS 60761 | RQE 49186
- WhatsApp: (51) 98228-3389
- E-mail: dreduardoaarocha@gmail.com
- Endereço: Av. José Loureiro da Silva, 2025, Sala 1001, Centro, Gravataí/RS, CEP 94010-001
