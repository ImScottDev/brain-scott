# Brain Scott - Segundo Cerebro com Claude Code + Obsidian

**by Scott Studio**

> Um comando. Um vault Obsidian completo com IA embutida.
> Estrutura de pastas, `CLAUDE.md`, slash commands e memoria persistente — tudo configurado automaticamente.

---

## O que e isso?

Brain Scott e um kit open-source que transforma o [Obsidian](https://obsidian.md) em um segundo cerebro turbinado com IA. Usando o [Claude Code](https://docs.anthropic.com/en/docs/claude-code), voce roda um unico comando e ganha:

- Vault Obsidian estruturado e personalizado pro seu perfil
- `CLAUDE.md` — o Claude te conhece desde a primeira conversa
- Slash commands prontos (`/diario`, `/tldr`, `/deal`, `/reuniao`...)
- Memoria persistente entre sessoes — preferencias, contexto, decisoes

Funciona pra qualquer perfil: dono de negocio, dev, criador de conteudo, consultor, estudante.

---

## Quick Start

### 1. Pre-requisitos

- [Obsidian](https://obsidian.md) (gratis)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (CLI do Claude)

### 2. Crie a pasta do vault

```bash
mkdir ~/meu-vault && cd ~/meu-vault
```

### 3. Copie as skills para o vault

```bash
# Clone o repo
git clone https://github.com/ImScottDev/brain-scott.git

# Copie a pasta de skills pro seu vault
cp -r brain-scott/.claude ~/meu-vault/
```

### 4. Rode o setup no Claude Code

```bash
claude
```

Dentro do Claude Code, rode:

```
/vault-setup
```

O Claude vai te perguntar quem voce e e o que faz. Responda em texto livre — algumas frases bastam. Ele monta tudo automaticamente.

---

## O que e criado

| Item | Descricao |
|---|---|
| **Estrutura de pastas** | Personalizada pro seu perfil |
| **CLAUDE.md** | Sua identidade pro Claude — contexto permanente |
| **Slash commands** | `/diario`, `/tldr` e comandos especificos do seu perfil |
| **Memoria** | O Claude lembra entre conversas — preferencias, contexto, decisoes |

---

## Skills incluidas

### Core (instaladas pelo /vault-setup)

| Skill | O que faz |
|---|---|
| `/vault-setup` | Configura o vault do zero |
| `/vault-diario` | Comeca o dia com contexto — deals, prioridades, pendencias |
| `/vault-tldr` | Salva resumo da sessao na pasta certa |
| `/vault-deal` | Puxa contexto completo de um deal/oportunidade |
| `/vault-reuniao` | Processa transcricao de reuniao — extrai pessoas, deals, acoes |
| `/vault-conteudo` | Desenvolve ideia de conteudo na sua voz |

### Extras (instale as que quiser)

| Skill | O que faz | Dependencias |
|---|---|---|
| `/ghostwriter` | Escreve conteudo na voz de qualquer creator | Perfil de voz em `live skills/` |
| `/transcribe` | Transcreve video de qualquer URL | `yt-dlp`, `faster-whisper`, `ffmpeg` |
| `/youtube-remaker` | Pega video gringo, reescreve na sua voz, gera thumbs | `yt-dlp`, `faster-whisper`, Gemini API |
| `/nanobanana` | Gera slides e imagens com IA | Gemini API key |
| `/thumb` | Baixa thumbnail HD do YouTube | `yt-dlp` |
| `/kling-motion` | Anima imagens em video (estilo keynote) | Kling API keys |

### Instalando uma skill extra

Copie a pasta da skill para `.claude/skills/` no seu vault:

```bash
cp -r .claude/skills/transcribe ~/meu-vault/.claude/skills/
```

Para skills com dependencias, rode o install wizard:
```
/transcribe install
```

---

## Estrutura do repo

```
.claude/skills/          Todas as skills disponiveis
  vault-setup/           O prompt principal de setup
  vault-diario/          Skill de briefing diario
  vault-tldr/            Skill de resumo de sessao
  vault-conteudo/        Skill de conteudo
  vault-deal/            Skill de deals
  vault-reuniao/         Skill de reunioes
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

## Creditos

Projeto original: [cellovault](https://github.com/celoia/cellovault) por [@celoia](https://instagram.com/celoia)

Adaptado e mantido por **Scott Studio** — [@ImScottDev](https://github.com/ImScottDev)

---

## Licenca

MIT
