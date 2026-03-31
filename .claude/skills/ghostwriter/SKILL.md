---
name: ghostwriter
description: Escreve roteiro de conteúdo imitando a voz de qualquer creator — lê perfil de voz da pasta "live skills/" e gera reel, YouTube ou post no estilo exato da pessoa.
---

## Workflow

### 1. Identificar o creator

Se o argumento mencionar o nome de um creator (ex: "thiago finch", "hormozi"), procurar o perfil de voz correspondente em `live skills/voz-*.md`.

Se não encontrar perfil de voz:
→ Perguntar: "Não tenho o perfil de voz desse creator. Quer me passar URLs de vídeos dele para eu extrair? Use `/transcribe` primeiro."

Se não mencionar creator:
→ Perguntar: "Para qual creator você quer que eu escreva?"

### 2. Carregar o perfil de voz

Ler o arquivo `live skills/voz-{nome}.md` completo. Este é o DNA do roteiro — tom, estrutura, recursos retóricos, padrões de frase, o que o creator faz e NÃO faz.

### 3. Identificar o tema

Extrair o tema do argumento do usuário. Exemplos:
- "thiago finch falar da greve dos caminhoneiros e gasolina alta" → tema: greve dos caminhoneiros + gasolina alta
- "hormozi sobre precificação" → tema: precificação

Se o tema precisar de contexto atual (notícia, evento, polêmica):
→ Fazer uma busca rápida na web para pegar dados, números e fatos recentes sobre o tema. Isso dá munição real pro roteiro e evita achismo.

### 4. Escolher formato

Se o argumento não especificar formato, perguntar:
- **Reel (30-60s)** — hook + uma sacada + punchline
- **YouTube (5-15min)** — estrutura completa com lista/narrativa
- **Post/carrossel** — texto para legenda ou slides

### 5. Gerar o roteiro

Escrever o roteiro **100% na voz do creator**, seguindo:

- A estrutura exata que o creator usa (extraída do perfil de voz)
- Os recursos retóricos que ele usa (analogias, perguntas retóricas, polarização, etc.)
- Os padrões de frase dele
- O que ele NÃO faz (respeitar os limites do estilo)
- Adaptar o tema com dados reais pesquisados

**Formato de saída do roteiro:**

```
# [CREATOR] — [TEMA]
## Formato: [Reel/YouTube/Post]

---

[ROTEIRO AQUI — escrito como se fosse o creator falando, pronto para gravar]

---

## Notas de produção
- Duração estimada: X min
- Tom dominante: [ex: provocador, inspiracional, técnico]
- Referências usadas: [fontes dos dados]
```

### 6. Salvar

Salvar o roteiro em `live skills/roteiro-{creator}-{tema-curto}.md`

## Regras

- NUNCA quebre o personagem — o roteiro inteiro deve soar como se o creator tivesse escrito
- Use dados e fatos reais, não invente estatísticas
- Se o perfil de voz diz que o creator NÃO faz algo, não faça
- Adapte a complexidade ao formato (reel = 1 sacada, YouTube = estrutura completa)
