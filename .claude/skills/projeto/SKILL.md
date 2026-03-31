# /projeto — Carregar contexto completo de um projeto

Base directory for this skill: o diretorio atual do vault

## O que fazer

1. Se o usuário não especificou qual projeto, listar projetos ativos de `projetos/` e perguntar
2. Carregar todas as notas relacionadas ao projeto:
   - Nota principal em `projetos/`
   - Decisões relacionadas em `decisoes/`
   - Clientes envolvidos em `clientes/`
   - Sistemas/automações conectados em `sistemas/`
   - Menções em `diario/` (últimas 5 entradas relevantes)
3. Apresentar resumo:
   - Status atual
   - Últimas atividades
   - Decisões pendentes
   - Próximas ações
4. Perguntar: "O que quer fazer nesse projeto?"
