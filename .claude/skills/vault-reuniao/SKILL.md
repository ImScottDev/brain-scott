---
name: reuniao
description: Processa transcrição de reunião — extrai pessoas, deals, decisões e próximas ações, salva em reunioes/.
---

Receber a transcrição colada pelo usuario (ou arquivo ja carregado do inbox/ via Fathom sync).

Processar e extrair:
1. **Participantes** — quem são, empresa, papel
2. **Contexto** — sobre o que foi a reunião
3. **Pontos principais** — o que foi discutido, em tópicos
4. **Decisões tomadas** — o que foi definido
5. **Próximas ações** — quem faz o quê e até quando
6. **Deals/oportunidades mencionados** — qualquer oportunidade de negócio
7. **Informações novas sobre pessoas** — contexto para atualizar `pessoas/`

## Nomenclatura do arquivo

Salvar em `reunioes/` usando o padrão:

```
YYYY-MM-DD-[pessoa-principal]-[contexto-curto].md
```

Regras:
- Máximo 4-5 "palavras" após a data
- Usar o nome da pessoa principal da reuniao (nao o usuario)
- Contexto curto = empresa ou tema central (1-2 palavras)
- Tudo em minúsculas, sem acentos, separado por hífen

Exemplos corretos:
- `2026-03-16-contato-a-reuniao.md`
- `2026-03-12-contato-b-projeto.md`
- `2026-03-16-contato-c-parceria.md`

Exemplos incorretos (evitar):
- `2026-03-16-contato-a-reuniao-contato-b-projeto.md` ← longo demais
- `2026-03-16-impromptu-google-meet-meeting.md` ← nome genérico do Fathom

## Fluxo padrão — sempre executar automaticamente

Após salvar a reunião em `reunioes/`, **sem perguntar**, executar:

1. **`pessoas/`** — criar ou atualizar arquivo para cada participante e pessoa relevante mencionada
2. **`deals/`** — criar ou atualizar arquivo para cada oportunidade identificada
3. **`empresas/`** — criar ou atualizar arquivo para empresas com informações novas
4. Atualizar próximos passos em deals existentes relacionados

Só avisar o que foi criado/atualizado ao final.
