---
tags:
  - squad
  - ia
  - agentes
  - claude-code
  - skills
  - hooks
  - mcp
aliases:
  - Claude Code Mastery Squad
  - claude-code-mastery
  - Squad Claude Code
---

# Claude Code Mastery Squad

> Expertise completa em Claude Code: hooks, skills, subagentes, MCP, plugins, times de agentes, customizacao, integracao e acompanhamento de roadmap.

**Versao:** 1.0.0 | **Criado:** 2026-03-01 | **Total:** 8 agentes, 6.741 linhas

## Arquitetura do Squad

```
                        Orion (Orchestrator)
                     claude-mastery-chief [Tier 0]
                              |
            ┌─────────┬───────┴───────┬──────────┐
            |         |               |          |
    ┌───────┴──┐  ┌───┴────┐  ┌──────┴───┐  ┌───┴──────┐
    |  Latch   |  | Piper  |  |  Nexus   |  |  Sigil   |
    |  Hooks   |  |  MCP   |  |  Swarm   |  |  Config  |
    | Tier 1   |  | Tier 1 |  |  Tier 1  |  |  Tier 1  |
    └──────────┘  └────────┘  └──────────┘  └──────────┘
            |         |               |
    ┌───────┴──┐  ┌───┴────┐  ┌──────┴───┐
    |  Anvil   |  | Conduit|  |  Vigil   |
    |  Skills  |  | Project|  | Roadmap  |
    | Tier 2   |  | Tier 2 |  |  Tier 2  |
    └──────────┘  └────────┘  └──────────┘
```

## Agentes

| Tier | Agente | Persona | Baseado Em | Linhas | Foco |
|------|--------|---------|------------|--------|------|
| 0 | claude-mastery-chief | Orion | Original | 554 | Triagem, roteamento, conhecimento transversal |
| 1 | hooks-architect | Latch | disler (IndyDevDan) | 1.013 | 17 eventos de hook, automacao, controle de danos |
| 1 | mcp-integrator | Piper | Peter Steinberger (@steipete) | 791 | Servidores MCP, descoberta de tools, budget de contexto |
| 1 | swarm-orchestrator | Nexus | Kieran Klaassen + Reuven Cohen | 1.008 | Times de agentes, subagentes, execucao paralela |
| 1 | config-engineer | Sigil | SuperClaude-Org | 663 | Configuracoes, permissoes, CLAUDE.md, sandbox |
| 2 | skill-craftsman | Anvil | BMAD-CODE-ORG | 1.046 | Skills, plugins, comandos, engenharia de contexto |
| 2 | project-integrator | Conduit | Daniel Miessler (PAI) | 959 | Integracao de projeto, CI/CD, bridge AIOS |
| 2 | roadmap-sentinel | Vigil | Boris Cherny | 707 | Roadmap, changelog, adocao de features |

## Inicio Rapido

### Ativar o Orquestrador
```
@claude-code-mastery:claude-mastery-chief
```
Ou use a ativacao AIOS:
```
/AIOS:agents:claude-mastery-chief
```

### Acesso Direto a Especialistas
```
/AIOS:agents:hooks-architect        # Automacao de hooks
/AIOS:agents:mcp-integrator         # Servidores MCP
/AIOS:agents:swarm-orchestrator     # Orquestracao multi-agente
/AIOS:agents:config-engineer        # Configuracoes & permissoes
/AIOS:agents:skill-craftsman        # Skills & plugins
/AIOS:agents:project-integrator     # Integracao de projeto
/AIOS:agents:roadmap-sentinel       # Atualizacoes & roadmap
```

## Cobertura de Features

| Feature do Claude Code | Especialista | Comandos Principais |
|------------------------|-------------|---------------------|
| Hooks (17 eventos) | Latch | `*create-hook`, `*audit-hooks`, `*hook-patterns` |
| Integracao MCP | Piper | `*add-server`, `*audit-mcp`, `*create-mcp-server` |
| Subagentes & Times | Nexus | `*create-agent`, `*create-team`, `*orchestrate` |
| Configuracoes & Permissoes | Sigil | `*configure`, `*permission-strategy`, `*sandbox-setup` |
| Skills & Plugins | Anvil | `*create-skill`, `*create-plugin`, `*context-strategy` |
| Integracao de Projeto | Conduit | `*integrate-project`, `*brownfield-setup`, `*ci-cd-setup` |
| Roadmap & Atualizacoes | Vigil | `*update-knowledge`, `*feature-radar`, `*migration-guide` |
| Bridge AIOS | Orion + Conduit | `*aios-bridge`, `*aios-guide` |

## Atribuicao de Pesquisa — Mentes de Elite

Este squad foi criado atraves de pesquisa iterativa com validacao de advogado do diabo (3 iteracoes). Cada agente e baseado em pessoas/projetos reais com frameworks documentados:

| Mente | Contribuicao | Fonte |
|-------|-------------|-------|
| **disler** (IndyDevDan) | Framework Hooks Mastery, padroes meta-agent, controle de danos | [GitHub](https://github.com/disler/claude-code-hooks-mastery) |
| **Peter Steinberger** (@steipete) | claude-code-mcp, workflow multi-instancia, filosofia CLI-first | [Blog](https://steipete.me/), [GitHub](https://github.com/steipete/claude-code-mcp) |
| **Kieran Klaassen** | Descoberta TeammateTool, documentacao de padroes swarm | [Gists](https://gist.github.com/kieranklaassen) |
| **Reuven Cohen** (ruvnet) | Plataforma de orquestracao Ruflo, 54+ agentes, kernels WASM | [GitHub](https://github.com/ruvnet/ruflo) |
| **SuperClaude-Org** | 9 personas cognitivas, 5 modos comportamentais, config puro .md | [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework) |
| **BMAD-CODE-ORG** | Metodo BMAD, 21 agentes, 50+ workflows, desenvolvimento orientado a spec | [Docs](https://docs.bmad-method.org/) |
| **Daniel Miessler** | Infraestrutura Pessoal de IA (PAI), filosofia Unix para IA | [Blog](https://danielmiessler.com/), [GitHub](https://github.com/danielmiessler/Personal_AI_Infrastructure) |
| **Boris Cherny** | Criador do Claude Code, metodologia plan-first, instancias paralelas | [Blog](https://boristane.com/), [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built) |

## Integracao AIOS-Core

Este squad entende tanto as capacidades nativas do Claude Code QUANTO o framework AIOS-core:

| Conceito AIOS | Equivalente Claude Code | Agente Bridge |
|--------------|------------------------|---------------|
| Agents (@dev, @qa...) | Subagentes (.claude/agents/) | Nexus |
| Tasks (.aios-core/tasks/) | Skills (.claude/skills/) | Anvil |
| Workflows | Sessoes multi-etapa | Nexus + Orion |
| core-config.yaml | .claude/settings.json | Sigil |
| Python hooks (monitor/) | Hooks nativos (command/http/prompt/agent) | Latch |
| Quality gates | Validacao baseada em hooks | Latch + Sigil |
| Entity registry | Tool Search + registro MCP | Piper |

## Estrutura de Diretorios

```
squads/claude-code-mastery/
├── config.yaml                    # Configuracao do squad e arquitetura de tiers
├── README.md                      # Este arquivo
├── agents/
│   ├── claude-mastery-chief.md    # Tier 0: Orquestrador (Orion)
│   ├── hooks-architect.md         # Tier 1: Hooks (Latch)
│   ├── mcp-integrator.md          # Tier 1: MCP (Piper)
│   ├── swarm-orchestrator.md      # Tier 1: Subagentes/Times (Nexus)
│   ├── config-engineer.md         # Tier 1: Configuracoes (Sigil)
│   ├── skill-craftsman.md         # Tier 2: Skills/Plugins (Anvil)
│   ├── project-integrator.md      # Tier 2: Integracao (Conduit)
│   └── roadmap-sentinel.md        # Tier 2: Roadmap (Vigil)
├── tasks/                         # Tasks especificas do squad
├── workflows/                     # Workflows multi-fase
├── templates/                     # Templates de saida
├── data/                          # Dados de referencia
├── scripts/                       # Scripts utilitarios
└── outputs/
    └── minds/                     # Extracoes de DNA mental
```

## Metricas de Qualidade

| Metrica | Valor |
|---------|-------|
| Total de agentes | 8 |
| Total de linhas | 6.741 |
| Media de linhas/agente | 843 |
| Cobertura Tier 0 | 1 orquestrador |
| Cobertura Tier 1 | 4 especialistas core |
| Cobertura Tier 2 | 3 especialistas estrategicos |
| Mentes clonadas | 8 (de 7 fontes distintas) |
| Iteracoes de pesquisa | 3 (com advogado do diabo) |
| Colisoes de nomes corrigidas | 2 (Piper, Sigil) |

---

*Claude Code Mastery Squad v1.0 — Criado pelo Squad Architect*
*Filosofia: "Domine a ferramenta para dominar o oficio."*

## Links

- [[squads/squads|Squads IA]] — Hub principal
- [[skills-agentes/skills-vault]] — Mapa de skills
- Contexto da sua empresa
