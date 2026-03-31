# Brain Scott — Seu Segundo Cerebro com IA

> Um comando. Um segundo cerebro completo com IA embutida.
> 156 agentes especializados. 27 skills. 18 templates. Tudo rodando dentro do Obsidian + Claude Code.

---

## O que e isso?

Brain Scott e um sistema open-source que transforma o [Obsidian](https://obsidian.md) no seu **segundo cerebro** — e conecta ele ao [Claude Code](https://docs.anthropic.com/en/docs/claude-code), a IA mais poderosa disponivel via terminal.

A IA passa a te conhecer. Ela sabe quem voce e, seus projetos, seus clientes, suas prioridades. E ela **lembra** de tudo entre conversas.

### O que vem incluso

```
 27 skills (comandos prontos)
 27 agentes core com persona
144 agentes especializados em 12 squads
120 tasks pre-configuradas
 24 workflows automatizados
 18 templates profissionais
 10 regras de orquestracao
  1 orquestrador inteligente
```

---

## Pra quem e isso?

| Perfil | O que voce ganha |
|--------|-----------------|
| **Dono de negocio** | IA que entende seu negocio, seus clientes e suas metas |
| **Freelancer / Consultor** | Organizacao de deals, clientes e projetos com contexto |
| **Criador de conteudo** | Producao rapida mantendo sua voz e estilo |
| **Dev solo** | Documentacao, decisoes e contexto entre sessoes |
| **Time pequeno** | 12 squads de IA como extensao da equipe |

---

## Quick Start (5 minutos)

### 1. Pre-requisitos

- [Obsidian](https://obsidian.md) — gratuito, roda em qualquer sistema
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — CLI do Claude (precisa de conta Anthropic)

### 2. Clone e configure

```bash
# Crie a pasta do seu segundo cerebro
mkdir ~/meu-cerebro && cd ~/meu-cerebro

# Clone o repo
git clone https://github.com/ImScottDev/brain-scott.git

# Copie tudo pro seu segundo cerebro
cp -r brain-scott/.claude ~/meu-cerebro/
cp -r brain-scott/squads ~/meu-cerebro/
```

### 3. Rode o setup

```bash
claude
```

Dentro do Claude Code:

```
/vault-setup
```

A IA te faz algumas perguntas sobre quem voce e e o que faz. Responda em texto livre. Ela monta tudo: estrutura de pastas, identidade, comandos e memoria.

**Pronto.** Abra a pasta no Obsidian e comece a usar.

---

## Os 12 Squads de IA

Cada squad e um time completo de agentes especializados que trabalham juntos. O **orquestrador** identifica automaticamente quais squads chamar pra cada pedido.

```
                         +-----------------------+
                         |     Orquestrador      |
                         |  (roteamento auto)    |
                         +-----------+-----------+
                                     |
          +----------+----------+----+----+----------+----------+
          |          |          |         |          |          |
     +----+----+ +---+---+ +---+---+ +---+---+ +---+---+ +----+----+
     | Hormozi | | Copy  | | Brand | |Traffic| | Story | | Design  |
     | Squad   | | Squad | | Squad | |Masters| |telling| | Squad   |
     |16 agents| |23 agt | |15 agt | |16 agt | |12 agt | | 8 agt   |
     +---------+ +-------+ +-------+ +-------+ +-------+ +---------+
          |          |          |         |          |          |
     +----+----+ +---+---+ +---+---+ +---+---+ +---+---+ +----+----+
     |Advisory | |C-Level| | Data  | | Cyber | |Claude | |Movement |
     | Board   | | Squad | | Squad | |Security| |Mastery| |  Squad  |
     |11 agents| | 6 agt | | 7 agt | |15 agt | | 8 agt | | 7 agt   |
     +---------+ +-------+ +-------+ +-------+ +-------+ +---------+
```

| Squad | Agentes | Foco |
|-------|---------|------|
| **Hormozi Squad** | 16 | Frameworks $100M Offers — vendas, pricing, launch, scaling |
| **Copy Squad** | 23 | Elite de copywriting — Gary Halbert, Ogilvy, Schwartz, Dan Kennedy... |
| **Brand Squad** | 15 | Marca e posicionamento — Aaker, Al Ries, Byron Sharp, StoryBrand |
| **Traffic Masters** | 16 | Trafego pago — Pedro Sobral, Kasim Aslam, Molly Pittman... |
| **Storytelling** | 12 | Narrativa — Joseph Campbell, Dan Harmon, Nancy Duarte, Oren Klaff |
| **Design Squad** | 8 | UI/UX e design systems — Brad Frost, Dan Mall |
| **Advisory Board** | 11 | Conselho estrategico — Ray Dalio, Charlie Munger, Naval, Peter Thiel |
| **C-Level Squad** | 6 | C-suite virtual completa (CEO, COO, CMO, CTO, CIO, CAIO) |
| **Data Squad** | 7 | Analytics e growth — Avinash Kaushik, Sean Ellis, Peter Fader |
| **Cybersecurity** | 15 | Seguranca — pentest, red team, blue team, AppSec |
| **Claude Code Mastery** | 8 | Dominio do Claude Code — hooks, skills, MCP |
| **Movement** | 7 | Construir movimentos que transcendem produtos |

---

## 27 Skills (Comandos)

### Gestao do Segundo Cerebro

| Comando | O que faz |
|---------|-----------|
| `/vault-setup` | Configura tudo do zero |
| `/vault-diario` | Briefing do dia: prioridades, deals, pendencias |
| `/vault-tldr` | Salva resumo da sessao automaticamente |
| `/vault-deal` | Contexto completo de uma oportunidade |
| `/vault-reuniao` | Processa transcricao de reuniao — extrai tudo |
| `/vault-conteudo` | Desenvolve ideia de conteudo na sua voz |
| `/diario` | Cria nota diaria com checagem de inbox |
| `/tldr` | Resumo rapido + salva na pasta certa |
| `/projeto` | Carrega contexto de um projeto |

### Criacao de Conteudo

| Comando | O que faz |
|---------|-----------|
| `/ghostwriter` | Escreve na voz de qualquer creator |
| `/youtube-remaker` | Pipeline completo: thumb + transcricao + reescrita + slides |
| `/transcribe` | Transcreve video de qualquer URL |
| `/nanobanana` | Gera slides e imagens com IA |
| `/kling-motion` | Anima imagens em video |
| `/thumb` | Baixa thumbnail HD do YouTube |

### Desenvolvimento e Arquitetura

| Comando | O que faz |
|---------|-----------|
| `/architect-first` | Validacao de arquitetura com checklists |
| `/checklist-runner` | Execucao automatizada de checklists |
| `/coderabbit-review` | Code review automatizado |
| `/mcp-builder` | Guia pra criar MCP servers |
| `/skill-creator` | Cria novas skills com validacao |
| `/synapse` | Engine de contexto inteligente |
| `/tech-search` | Pesquisa tecnica profunda |

---

## 27 Agentes Core

Agentes com persona que voce ativa com `@nome`:

```
  Desenvolvimento          Orquestradores           Especializados
  +-----------+           +-----------+            +-----------+
  | @dev      |           | @copy     |            | @brad     |
  | @qa       |           |  -chief   |            |  -frost   |
  | @architect|           | @design   |            | @dan-mall |
  | @pm       |           |  -chief   |            | @dave     |
  | @po       |           | @story    |            |  -malouf  |
  | @sm       |           |  -chief   |            | @db-sage  |
  | @analyst  |           | @data     |            | @design   |
  | @data     |           |  -chief   |            |  -system  |
  | -engineer |           | @cyber    |            | @legal    |
  | @ux       |           |  -chief   |            |  -chief   |
  | @devops   |           | @traffic  |            | @sop      |
  +-----------+           |  -chief   |            | -extractor|
                          | @squad    |            +-----------+
                          |  -chief   |
                          +-----------+
```

---

## 18 Templates Profissionais

Templates prontos pra gerar documentos padronizados:

| Template | Uso |
|----------|-----|
| PRD | Product Requirements Document |
| Brownfield PRD | PRD pra projeto existente |
| Architecture | Documento de arquitetura |
| Fullstack Architecture | Arquitetura full stack |
| Frontend Spec | Especificacao de frontend |
| Story | Story de desenvolvimento |
| Project Brief | Brief de projeto |
| Database Schema | Schema de banco (full e lite) |
| QA Gate | Quality gate |
| Competitor Analysis | Analise de concorrente |
| Market Research | Pesquisa de mercado |
| Brainstorming Output | Output de brainstorm |

---

## Workflows Automatizados

O sistema vem com 4 workflows principais que coordenam os agentes:

```
 Story Development Cycle          QA Loop
 @sm cria -> @po valida ->        @qa review -> fix -> re-review
 @dev implementa -> @qa testa     (max 5 iteracoes automaticas)

 Spec Pipeline                    Brownfield Discovery
 Requisitos -> Arquitetura ->     10 fases de assessment
 Pesquisa -> Spec -> Review       pra codebases existentes
```

---

## Estrutura do Repo

```
.claude/
  skills/          27 skills (comandos prontos)
  agents/          27 agentes core com persona
  templates/       18 templates profissionais
  rules/           10 regras de orquestracao

squads/
  advisory-board/    11 agentes — conselho estrategico
  brand-squad/       15 agentes — marca e posicionamento
  c-level-squad/      6 agentes — C-suite virtual
  claude-code-mastery/ 8 agentes — dominio Claude Code
  copy-squad/        23 agentes — copywriting lendario
  cybersecurity/     15 agentes — seguranca
  data-squad/         7 agentes — analytics e growth
  design-squad/       8 agentes — UI/UX e design systems
  hormozi-squad/     16 agentes — frameworks de scaling
  movement/           7 agentes — movimentos culturais
  storytelling/      12 agentes — narrativa
  traffic-masters/   16 agentes — trafego e marketing
  orquestrador.md    protocolo de roteamento inteligente

site/                landing page
CLAUDE.md.template   template de referencia
```

---

## Como funciona por baixo

1. **Voce faz um pedido** em linguagem natural
2. **O orquestrador** classifica, identifica os squads certos e monta um pipeline
3. **Os agentes trabalham em cadeia** — cada um agrega valor ao output do anterior
4. **O resultado** volta compilado, revisado e no tom da sua marca
5. **Tudo fica salvo** no seu segundo cerebro com contexto e conexoes

---

## Licenca

MIT — use, modifique e distribua livremente.

---

**Feito por [@ImScottDev](https://github.com/ImScottDev)**
