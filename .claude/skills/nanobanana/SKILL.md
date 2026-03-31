---
name: nanobanana
description: Gera slides e imagens via NanoBanana Pro API (Gemini 3.1 Flash Image) — usa branding e conteúdo das pastas do projeto.
---

Gera imagens/slides usando a API do NanoBanana (Nano Banana 2 — modelo `gemini-3.1-flash-image-preview`).

## Fluxo

1. Perguntar ao Marcelo: **"Qual bloco ou tema quer gerar?"** (ex: fundamentos, skills, cases, monetização, comunidade, ou tema livre)
2. Ler o arquivo de branding em `conteudo/live-2026-03-19/ref/branding-nanobanana.md` para pegar o estilo visual
3. Ler o conteúdo do bloco correspondente (ex: `conteudo/live-2026-03-19/01-fundamentos/o-que-e-ide.md`)
4. Ler referências visuais em `conteudo/live-2026-03-19/ref/` se houver imagens relevantes
5. Montar o prompt combinando branding + conteúdo + referências
6. Chamar a API para gerar a imagem
7. Salvar o resultado na pasta do bloco correspondente

## API — Nano Banana 2 (modelo mais recente)

**Modelo:** `gemini-3.1-flash-image-preview`
**Endpoint:** `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent`
**API Key:** variável de ambiente `GEMINI_API_KEY`

### Chamada via curl

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "PROMPT_AQUI"
      }]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "candidateCount": 1,
      "temperature": 0.7
    }
  }' | python3 -c "
import sys, json, base64
resp = json.load(sys.stdin)
for part in resp['candidates'][0]['content']['parts']:
    if 'inlineData' in part:
        img_data = base64.b64decode(part['inlineData']['data'])
        with open('OUTPUT_PATH', 'wb') as f:
            f.write(img_data)
        print('Imagem salva em OUTPUT_PATH')
    elif 'text' in part:
        print(part['text'])
"
```

### Importante
- `responseModalities` DEVE incluir `["TEXT", "IMAGE"]` — só `["IMAGE"]` causa erro
- O response retorna a imagem em base64 dentro de `inlineData.data`
- Decodificar com base64 e salvar como `.png`

## Montagem do prompt

Combinar o branding com o conteúdo do slide:

```
Crie um slide de apresentação 16:9.

ESTILO VISUAL:
- Fundo gradiente escuro (navy/purple: #1a1a2e → #16213e)
- Glow sutil laranja e azul nos cantos inferiores
- Título em fonte serif branca grande, centralizado no topo
- Imagem centralizada abaixo com bordas arredondadas
- Visual minimalista com muito espaço negativo

CONTEÚDO DO SLIDE:
- Título: "[TÍTULO DO SLIDE]"
- Imagem/elemento visual: [DESCRIÇÃO DO VISUAL]

Não colocar texto demais. Manter limpo e impactante.
```

## Onde salvar

Salvar as imagens geradas na pasta do bloco:
- `conteudo/live-2026-03-19/01-fundamentos/slide-ide.png`
- `conteudo/live-2026-03-19/01-fundamentos/slide-claude-code.png`
- etc.

Padrão de nome: `slide-[tema-curto].png`
