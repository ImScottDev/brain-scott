---
tags:
  - squad
  - ia
  - agentes
  - copywriting
  - direct-response
  - sales-letter
  - email
aliases:
  - Copy Squad
  - copy-squad
  - Squad de Copy
---

# Copy Squad

Squad de elite com 23 agentes de copywriting — 22 copywriters lendarios + 1 orquestrador (Copy Chief).

## Inicio Rapido

```
@copy-chief     # Ativar o orquestrador
*diagnose       # Triagem do seu pedido de copy
*full-copy-project  # Workflow completo de projeto de copy
```

## Arquitetura de Tiers

| Tier | Nome | Agentes | Foco |
|------|------|---------|------|
| **0** | Orquestracao | copy-chief | Roteia demandas, revisa entregas, media |
| **1A** | Lendas de Resposta Direta | gary-halbert, eugene-schwartz, claude-hopkins, gary-bencivenga, robert-collier, john-carlton, jim-rutz | Long-form, impresso, mala direta |
| **1B** | Copy Moderno & Funis | dan-kennedy, frank-kern, russell-brunson, todd-brown, stefan-georgi, jon-benson, ry-schwartz | VSLs, funis, webinarios, lancamentos |
| **1C** | Email & Relacionamento | ben-settle, andre-chaperon, dan-koe | Sequencias de email, emails diarios, nurture |
| **1D** | Ofertas & Paginas de Venda | joe-sugarman, david-ogilvy, clayton-makepeace, parris-lampropoulos, david-deutsch | Arquitetura de oferta, anuncios impressos, financeiro/saude |

## Matriz de Roteamento

O Copy Chief roteia automaticamente seu pedido para o melhor especialista:

| Tipo de Pedido | Primario | Secundario |
|---------------|----------|------------|
| Headline | eugene-schwartz | gary-halbert |
| Carta de vendas / long-form | gary-halbert | john-carlton |
| Sequencia de email | andre-chaperon | ben-settle |
| VSL / video de vendas | stefan-georgi | jon-benson |
| Roteiro de webinario | russell-brunson | todd-brown |
| Criacao de oferta | dan-kennedy | joe-sugarman |
| Copy de funil | russell-brunson | frank-kern |
| Big idea / conceito de campanha | todd-brown | eugene-schwartz |
| Bullet points / fascinacoes | gary-bencivenga | clayton-makepeace |
| Emails diarios / engajamento | ben-settle | dan-koe |
| Carta de vendas classica / mala direta | robert-collier | jim-rutz |
| Copy financeiro / saude | clayton-makepeace | parris-lampropoulos |
| Copy de marca / premium | david-ogilvy | david-deutsch |
| Copy de anuncio / ads pagos | dan-kennedy | frank-kern |
| Copy de lancamento | frank-kern | russell-brunson |
| Copy de marca pessoal | dan-koe | ry-schwartz |
| Revisao / critica de copy | copy-chief | eugene-schwartz |

## Componentes

- **23 agentes** — 1 orquestrador + 22 especialistas
- **13 tasks** — write-headline, write-sales-letter, write-vsl-script, write-email-sequence, write-ad-copy, write-landing-page, write-bullets, create-funnel-copy, create-offer, analyze-copy, critique-copy, diagnose, review
- **2 workflows** — full-copy-project, copy-review-cycle
- **1 checklist** — output-quality (gate de qualidade para entregas)
- **2 arquivos de dados** — routing-catalog, copy-frameworks

## Workflows

### Projeto de Copy Completo (`*full-copy-project`)
Ponta a ponta: briefing > diagnostico > atribuir especialista > escrever > revisar > entregar.

### Ciclo de Revisao de Copy (`*copy-review-cycle`)
Loop iterativo de escrita-critica-revisao (max 3 iteracoes).

## Requisitos

- AIOS >= 4.0.0

## Links

- [[squads/squads|Squads IA]] — Hub principal
- [[skills-agentes/skills-vault]] — Mapa de skills
- Contexto da sua empresa
