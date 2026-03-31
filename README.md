# Brain Scott - Seu Segundo Cerebro com IA

**by Scott Studio**

> Imagina abrir o computador e a IA ja saber quem voce e, o que voce faz, seus projetos, seus clientes, suas prioridades do dia.
>
> Isso e o Brain Scott.

---

## O problema

Voce tem anotacoes espalhadas em 5 apps diferentes. Nenhuma IA te conhece de verdade. Toda conversa com ChatGPT comeca do zero. Voce perde contexto, perde tempo, perde oportunidades.

## A solucao

Brain Scott transforma o [Obsidian](https://obsidian.md) (app gratuito) no seu **segundo cerebro** — e conecta ele ao [Claude Code](https://docs.anthropic.com/en/docs/claude-code), a IA mais avancada do mercado.

Com **um unico comando**, voce ganha:

- Um segundo cerebro organizado e personalizado pro seu perfil
- IA que te conhece desde a primeira conversa
- Comandos prontos pra rotina: briefing do dia, resumo de reuniao, gestao de deals
- Memoria entre sessoes — a IA lembra tudo que voce ja conversou

**Funciona pra qualquer perfil:** dono de negocio, freelancer, criador de conteudo, consultor, dev, estudante.

---

## Como comecar (5 minutos)

### 1. Instale o necessario

- [Obsidian](https://obsidian.md) — gratuito, roda em qualquer sistema
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — CLI do Claude (precisa de conta Anthropic)

### 2. Crie a pasta do seu segundo cerebro

```bash
mkdir ~/meu-cerebro && cd ~/meu-cerebro
```

### 3. Baixe o Brain Scott

```bash
git clone https://github.com/ImScottDev/brain-scott.git
cp -r brain-scott/.claude ~/meu-cerebro/
```

### 4. Rode o setup

```bash
claude
```

Dentro do Claude Code, digite:

```
/vault-setup
```

A IA vai te fazer algumas perguntas sobre quem voce e e o que faz. Responda naturalmente — pode ser em poucas frases. Ela monta tudo automaticamente.

**Pronto.** Seu segundo cerebro esta configurado.

---

## O que voce ganha

| Recurso | O que faz |
|---|---|
| **Segundo cerebro organizado** | Estrutura de pastas pensada pro seu perfil — sem bagunca |
| **IA personalizada** | O Claude sabe quem voce e, seus projetos e como voce trabalha |
| **Comandos de produtividade** | Briefing diario, resumo de reuniao, gestao de deals, conteudo |
| **Memoria persistente** | A IA lembra de conversas anteriores — sem repetir contexto |

---

## Comandos disponiveis

### Essenciais (ja vem instalados)

| Comando | O que faz |
|---|---|
| `/vault-setup` | Configura seu segundo cerebro do zero |
| `/vault-diario` | Comeca o dia com contexto: deals, prioridades, pendencias |
| `/vault-tldr` | Salva resumo da sessao automaticamente |
| `/vault-deal` | Puxa contexto completo de uma oportunidade ou parceria |
| `/vault-reuniao` | Processa transcricao de reuniao — extrai pessoas, decisoes, proximos passos |
| `/vault-conteudo` | Desenvolve ideia de conteudo na sua voz |

### Extras (instale os que quiser)

| Comando | O que faz | Precisa de |
|---|---|---|
| `/ghostwriter` | Escreve conteudo imitando a voz de qualquer creator | Perfil de voz configurado |
| `/transcribe` | Transcreve video de qualquer plataforma | `yt-dlp`, `faster-whisper`, `ffmpeg` |
| `/youtube-remaker` | Pega video gringo e reescreve na sua voz com thumbs | `yt-dlp`, `faster-whisper`, Gemini API |
| `/nanobanana` | Gera slides e imagens com IA | Gemini API key |
| `/thumb` | Baixa thumbnail HD do YouTube | `yt-dlp` |
| `/kling-motion` | Anima imagens em video | Kling API keys |

Para instalar um extra:

```bash
cp -r brain-scott/.claude/skills/transcribe ~/meu-cerebro/.claude/skills/
```

---

## Pra quem e isso?

- **Donos de negocio** que querem IA que entende o contexto da empresa
- **Freelancers e consultores** que precisam organizar clientes, deals e projetos
- **Criadores de conteudo** que querem produzir mais rapido sem perder a voz
- **Devs** que querem documentar decisoes e manter contexto entre sessoes
- **Qualquer pessoa** cansada de IA que nao lembra de nada

---

## Estrutura do projeto

```
.claude/skills/          Todos os comandos disponiveis
  vault-setup/           Configurador do segundo cerebro
  vault-diario/          Briefing diario
  vault-tldr/            Resumo de sessao
  vault-conteudo/        Producao de conteudo
  vault-deal/            Gestao de deals
  vault-reuniao/         Processamento de reunioes
  ghostwriter/           Ghostwriter multi-creator
  transcribe/            Transcricao de video
  youtube-remaker/       Remake de video do YouTube
  nanobanana/            Gerador de slides com IA
  thumb/                 Download de thumbnails
  kling-motion/          Animacao de imagens
site/                    Landing page
CLAUDE.md.template       Template de referencia
```

---

## Licenca

MIT — use, modifique e distribua livremente.

---

**Feito por [Scott Studio](https://github.com/ImScottDev)**
