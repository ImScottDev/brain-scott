---
tags:
  - squads
  - ia
  - orquestrador
  - automacao
aliases:
  - Orquestrador
  - Orchestrator
  - Squad Router
---

# Orquestrador — Protocolo de Roteamento Inteligente

> Quando o usuario faz um pedido, este documento define como identificar, mobilizar e encadear os squads e agentes certos para entregar o melhor resultado.

O orquestrador nao e um agente separado — e o **protocolo que o Claude segue** para transformar qualquer solicitacao em um pipeline de execucao multi-agente.

---

## Protocolo de Execucao

### Fase 1 — Entender (30s)
Ao receber um pedido:
1. **Classificar o tipo** de solicitacao (ver Matriz de Roteamento abaixo)
2. **Identificar gaps** — que informacao falta pra executar bem?
3. **Perguntar o minimo** — 2-4 perguntas rapidas e diretas, so o que nao da pra inferir
4. **Confirmar o plano** — "Vou chamar X pra fazer isso, Y pra aquilo, Z pra finalizar. Bora?"

### Fase 2 — Mobilizar
1. **Carregar contexto** — ler notas relevantes do vault (projeto, produto, pessoa, decisao)
2. **Selecionar agentes** — escolher os squads/agentes pela Matriz de Roteamento
3. **Definir sequencia** — quem faz o que, em que ordem, o que passa pro proximo
4. **Executar em cadeia** — cada agente recebe o output do anterior + contexto do vault

### Fase 3 — Sintetizar
1. **Compilar resultado** — juntar todas as contribuicoes num entregavel coeso
2. **Revisar consistencia** — tom de voz da sua marca, dados corretos, sem contradicao
3. **Entregar** — resultado final formatado, pronto pra uso
4. **Registrar no vault** — se relevante, atualizar nota do projeto/decisao/diario

---

## Matriz de Roteamento

### Projetos Web (paginas, LPs, sites)

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. Estrategia | `@hormozi-chief` + `@hormozi-offers` | Definir angulo, oferta, ICP, posicionamento da pagina |
| 2. Diagnostico | `@hormozi-audit` | Se tem pagina existente: rodar diagnostico mental, mapear problemas |
| 3. Copy | `@copy-chief` → delega pro especialista certo | Escrever headline, subhead, CTA, body, prova social |
| 4. Estrutura | `@design-chief` | Definir wireframe, secoes, hierarquia, fluxo de conversao |
| 5. Design | `@design-chief` | Layout, UI, identidade visual, responsividade |
| 6. Review | `@brand-chief` | Garantir consistencia de marca e posicionamento |
| 7. Implementacao | Claude (dev) | Codigo, deploy |

### Melhoria de Prompts / IA SDR

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. Analise | `@hormozi-chief` | Ler prompts atuais, identificar gaps |
| 2. Framework | `@hormozi-closer` + `@hormozi-offers` | Refinar CLOSER, oferta, objecoes |
| 3. Copy | `@copy-chief` → email/conversao specialist | Tom, persuasao, linguagem natural |
| 4. Storytelling | `@story-chief` | Narrativa, ganchos, sequencia emocional |
| 5. Data | `@data-chief` | Metricas de conversao, o que otimizar |
| 6. Sintese | `@hormozi-chief` | Compilar tudo no formato do prompt final |

### Prospeccao e Vendas

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. ICP | `@hormozi-leads` | Definir/refinar perfil ideal |
| 2. Pesquisa | `@hormozi-leads` | Analisar nicho, encontrar angulos |
| 3. Abordagem | `@hormozi-closer` + `@copy-chief` | Script de primeiro contato |
| 4. diagnostico | `@hormozi-audit` | Diagnostico da LP do prospect |
| 5. Proposta | `@hormozi-offers` + `@hormozi-pricing` | Construir oferta irresistivel |
| 6. Objecoes | `@hormozi-closer` | Mapa de objecoes e respostas |

### Conteudo (Instagram, YouTube, posts)

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. Ideia | `@hormozi-chief` + `@hormozi-content` | Tema, angulo, gancho |
| 2. Narrativa | `@story-chief` → especialista por formato | Estrutura narrativa (reel, carrossel, video) |
| 3. Copy | `@copy-chief` → `@dan-koe` ou `@ben-settle` | Texto, CTA, legendas |
| 4. Visual | `@design-chief` | Thumbnails, slides, identidade |
| 5. Review | `@brand-chief` | Consistencia de marca |

### Estrategia e Decisoes de Negocio

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. Contexto | `@hormozi-chief` | Levantar dados do vault |
| 2. Analise | `@board-chair` → advisors relevantes | Perspectivas multiplas |
| 3. Financeiro | `@vision-chief` (CFO) | Impacto financeiro |
| 4. Risco | `@board-chair` → `@charlie-munger` | Inversao, o que pode dar errado |
| 5. Decisao | Sintese de todos | Recomendacao fundamentada |

### Branding e Posicionamento

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. Diagnostico | `@brand-chief` | Audit de marca atual |
| 2. Posicionamento | `@al-ries` + `@byron-sharp` | Diferenciacao, categoria |
| 3. Narrativa | `@donald-miller` + `@story-chief` | StoryBrand, narrativa de marca |
| 4. Identidade | `@alina-wheeler` | Sistema visual, guidelines |
| 5. Naming | `@naming-strategist` | Nomes, taglines |

### Seguranca e Infra

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. Audit | `@cyber-chief` | Scan de vulnerabilidades |
| 2. Analise | Especialista por area | Pentest, AppSec, rede |
| 3. Fix | Claude (dev) | Implementar correcoes |
| 4. Validacao | `@cyber-chief` | Confirmar fix |

### Analise de Dados e Growth

| Etapa | Quem | O que faz |
|-------|------|-----------|
| 1. Setup | `@data-chief` → `@avinash-kaushik` | GA4, metricas, dashboards |
| 2. Analise | `@peter-fader` | CLV, cohorts, retencao |
| 3. Growth | `@sean-ellis` | Experimentos, activation, referral |
| 4. Comunidade | `@david-spinks` | Community-led growth |

---

## Regras do Orquestrador

1. **Minimo de perguntas** — so perguntar o que nao da pra inferir do contexto/vault
2. **Sempre carregar contexto** — nunca executar sem ler as notas relevantes do vault
3. **Tom consistente da sua marca** — resultado final sempre no tom da marca
4. **Registrar no vault** — se a execucao gerou decisao, insight ou entregavel relevante, salvar
5. **Compor, nao repetir** — cada agente agrega valor; se dois fariam a mesma coisa, so chamar um
6. **Transparencia** — sempre dizer pro usuario quem vai ser chamado e por que
7. **Adaptar** — se o pedido nao encaixa em nenhuma categoria, montar pipeline custom

---

## Squads Disponiveis

| Squad | Agentes | Foco |
|-------|---------|------|
| [[squads/advisory-board/advisory-board\|Advisory Board]] | 11 | Decisoes estrategicas |
| [[squads/hormozi-squad/hormozi-squad\|Hormozi Squad]] | 16 | Vendas, offers, scaling |
| [[squads/copy-squad/copy-squad\|Copy Squad]] | 23 | Copywriting por especialidade |
| [[squads/traffic-masters/traffic-masters\|Traffic Masters]] | 16 | Trafego pago |
| [[squads/brand-squad/brand-squad\|Brand Squad]] | 15 | Marca e posicionamento |
| [[squads/storytelling/storytelling\|Storytelling]] | 12 | Narrativa |
| [[squads/design-squad/design-squad\|Design Squad]] | 8 | UI/UX, design systems |
| [[squads/data-squad/data-squad\|Data Squad]] | 7 | Analytics, growth, CLV |
| [[squads/c-level-squad/c-level-squad\|C-Level Squad]] | 6 | Gestao executiva |
| [[squads/cybersecurity/cybersecurity\|Cybersecurity]] | 15 | Seguranca |
| [[squads/claude-code-mastery/claude-code-mastery\|Claude Code Mastery]] | 8 | Claude Code, hooks, MCPs |
| [[squads/movement/movement\|Movement]] | 7 | Movimentos culturais |

---

## Links

- [[squads/squads|Squads IA]] — Indice de todos os squads
