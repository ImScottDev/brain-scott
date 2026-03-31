---
name: vault-setup
description: Configurador interativo de vault Obsidian. Pergunta ao usuário sobre si mesmo em texto livre, depois constrói uma estrutura de vault personalizada, CLAUDE.md e slash commands diretamente no diretório atual.
---

# Vault Setup — Configurador Obsidian

Execute de DENTRO da pasta que você quer que se torne seu vault Obsidian.

## PASSO 1 — Uma pergunta, texto livre

Exiba esta mensagem exatamente, depois aguarde a resposta:

---

**Me conte um pouco sobre você para eu montar o seu vault.**

Responda na ordem que preferir:

- O que você faz no trabalho?
- O que mais escapa — o que você gostaria de acompanhar melhor?
- Só trabalho, ou vida pessoal também?
- Tem arquivos existentes para importar? (PDFs, docs, slides)

Não precisa ser formal. Algumas frases já bastam.

---

## PASSO 2 — Inferir e mostrar prévia, sem perguntas adicionais

A partir da resposta em texto livre, inferir:
- O papel do usuário (dono de negócio / desenvolvedor / consultor / criador / estudante)
- O principal ponto de dor
- Escopo (só trabalho / trabalho + pessoal / sistema de vida completo)
- Se tem arquivos existentes

Depois mostrar prévia do vault. NÃO fazer perguntas de esclarecimento. Fazer inferências inteligentes.

```
Aqui está o seu vault — pronto para construir quando quiser.

📁 [nome do diretório atual]
├── inbox/          Zona de entrada — tudo novo cai aqui primeiro
├── diario/         Capturas rápidas e descargas mentais do dia
├── [pasta]/        [propósito baseado no papel do usuário]
├── [pasta]/        [propósito baseado no papel do usuário]
├── [pasta]/        [propósito baseado no papel do usuário]
├── projetos/       Trabalho ativo com status e próximas ações
└── arquivo/        Trabalho concluído — nunca deletado, só movido

Slash commands:
  /diario   — começar o dia com contexto do vault
  /tldr     — salvar qualquer sessão na pasta certa
  /[papel]  — [descrição específica do papel]

Digite "construir" para criar isso, ou me diga o que mudar.
```

Aguardar confirmação antes de construir qualquer coisa.

## PASSO 3 — Construir após confirmação

Quando disserem "construir", "sim", "vai", "parece bom", ou similar:

### Criar pastas
```bash
mkdir -p inbox diario [pastas do papel] projetos arquivo scripts \
  .claude/skills/diario .claude/skills/tldr .claude/skills/[comando-do-papel]
```

Conjuntos de pastas por papel:
- Dono de Negócio → `pessoas/ operacoes/ decisoes/`
- Desenvolvedor → `pesquisa/ clientes/`
- Consultor → `clientes/ pesquisa/`
- Criador → `conteudo/ pesquisa/ clientes/`
- Estudante → `notas/ pesquisa/`

Se escopo pessoal → também `pessoal/`

### Abrir no Obsidian
```bash
open -a Obsidian "$(pwd)"
```

### Escrever CLAUDE.md
Escrever diretamente no `CLAUDE.md` no diretório atual:

```markdown
# CLAUDE.md — Segundo Cérebro de [papel inferido]

## Quem Sou
[2-3 frases baseadas no que contaram — específico, pessoal, escrito em primeira pessoa como Claude descrevendo seu dono]

## Estrutura do Meu Vault
[árvore de pastas com uma linha de propósito por pasta]

## Como Trabalho
[3-4 pontos inferidos das respostas — estilo de captura, principal ponto de dor, escopo, o que querem da IA]

## Regras de Contexto
Quando mencionar uma decisão → verificar [decisoes ou pasta relevante] primeiro
Quando mencionar uma pessoa/cliente/projeto → procurar em [pasta relevante]
Quando pedir para escrever → ler notas recentes de diario/ para combinar com minha voz
Quando algo cair no inbox/ → perguntar se quero organizar agora
```

### Escrever arquivos de skill

**`.claude/skills/diario/SKILL.md`:**
Ler a nota diária de hoje ou criar uma. Verificar inbox/ para arquivos não processados. Destacar as 3 principais prioridades. Perguntar: "No que vamos trabalhar hoje?"

**`.claude/skills/tldr/SKILL.md`:**
Resumir esta conversa: decisões, coisas a lembrar, próximas ações. Salvar na pasta mais relevante. Atualizar memory.md.

**Skill específica do papel:**
- Dono de Negócio → `.claude/skills/standup/SKILL.md` — briefing sobre projetos, decisões, pessoas
- Desenvolvedor → `.claude/skills/projeto/SKILL.md` — carregar contexto completo de um projeto
- Consultor → `.claude/skills/cliente/SKILL.md` — carregar contexto completo de um cliente
- Criador → `.claude/skills/conteudo/SKILL.md` — ler pasta de conteúdo, calibrar voz, desenvolver ideia
- Estudante → `.claude/skills/pesquisa/SKILL.md` — reunir todas as notas sobre um tópico, sintetizar

### Escrever memory.md
```markdown
# Memória

## Registro de Sessões
[Atualizado pelo Claude Code após cada sessão]

## Minhas Preferências
[Adicionado conforme o Claude aprende]
```

## PASSO 4 — Pergunta sobre injeção de contexto

Após construir, perguntar:

```
Uma última coisa — como você quer que o contexto do vault seja carregado no Claude Code?

1. Global (recomendado) — adiciona uma linha ao ~/.claude/CLAUDE.md para que o contexto
   do vault carregue automaticamente em toda sessão do Claude Code nesta máquina
2. Manual — eu te dou a linha para colar em projetos específicos quando precisar
3. Só o vault — funciona automaticamente quando você roda o claude de dentro desta pasta
```

**Se global:** Adicionar ao `~/.claude/CLAUDE.md` (criar se necessário):
```
## Meu Contexto Pessoal
No início de cada sessão, leia [caminho absoluto do vault]/CLAUDE.md para contexto sobre quem sou, meu trabalho e minhas convenções.
```

## PASSO 5 — Saída final

```
Pronto. Seu vault está ativo no Obsidian.

Um passo manual restante:
  Obsidian → Configurações → Geral → Habilitar Interface de Linha de Comando

Seus slash commands:
  /diario   — rode isso amanhã de manhã
  /tldr     — rode no final de qualquer sessão
  /[papel]  — [descrição em uma linha]

Tem arquivos para importar?
  python scripts/process_docs_to_obsidian.py ~/seus-arquivos inbox/
  Depois: "Organize tudo no inbox/ nas pastas certas"
```
