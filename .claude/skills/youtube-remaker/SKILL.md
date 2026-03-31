---
name: youtube-remaker
description: Recebe URL do YouTube, baixa thumb, transcreve, reescreve na sua voz, gera 3 thumbs com clone, monta slides e organiza tudo em um canvas Obsidian.
---

## Workflow

### 1. Receber a URL

O argumento é a URL do YouTube. Se não vier, perguntar.

### 2. Extrair metadados e thumbnail

```bash
yt-dlp --print title --print thumbnail --skip-download "URL"
```

Baixar a thumbnail original:
```bash
yt-dlp --write-thumbnail --skip-download --convert-thumbnails png -o "OUTPUT_PATH/thumb-original" "URL"
```

Salvar tudo em uma pasta de trabalho: `conteudo/yt-remake/YYYY-MM-DD-slug-do-titulo/`

### 3. Transcrever o vídeo

Usar o script de transcrição existente:
```bash
python3 <vault>/.claude/skills/transcribe/scripts/transcribe_url.py "URL" --timestamps
```

Salvar a transcrição em `conteudo/yt-remake/YYYY-MM-DD-slug/transcricao.md`

### 4. Reescrever na sua voz

Ler o guia de voz em `conteudo/voz-usuario.md` e reescrever o conteudo do video:

- Manter os pontos principais e insights do video original
- Adaptar 100% para a sua voz (usar o guia de voz como referencia de tom, expressoes e estilo)
- Usar a estrutura de hook definida no guia de voz (cenario hipotetico, contraste, analogia inedita)
- NAO usar: tom de professor, listas numeradas narradas, linguagem formal, hook forcado
- Incluir onde voce adicionaria sua experiencia pessoal (casos reais, contexto proprio)
- Formato: roteiro completo pronto pra gravar

Salvar em `conteudo/yt-remake/YYYY-MM-DD-slug/roteiro-usuario.md`

### 5. Gerar 3 thumbnails com clone

#### Carregar referências
1. Ler a thumbnail original baixada no passo 2
2. Ler TODAS as imagens da pasta `refs/clone-usuario/` — essas sao fotos de referencia do usuario

#### Gerar via Gemini (NanoBanana)

Para cada uma das 3 variações, montar um prompt que:
- Descreve o layout e estilo visual da thumb original (cores, composição, elementos gráficos, texto)
- Substitui a pessoa original pelo usuario (usando as fotos de referencia como guia de aparencia)
- Se a thumb original nao tinha pessoa, adiciona o usuario integrado ao layout
- Mantém o formato 16:9 (1280x720)
- Cada variação muda algo: ângulo, expressão, composição ou destaque visual

**API call com imagem de referência:**

```bash
# Primeiro, converter imagens para base64
CLONE_B64=$(base64 -i "refs/clone-usuario/PRIMEIRA_FOTO.png")
THUMB_B64=$(base64 -i "thumb-original.png")

curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {"text": "PROMPT_DA_THUMB"},
        {"inlineData": {"mimeType": "image/png", "data": "THUMB_B64_AQUI"}},
        {"inlineData": {"mimeType": "image/png", "data": "CLONE_B64_AQUI"}}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "candidateCount": 1,
      "temperature": 0.8
    }
  }' | python3 -c "
import sys, json, base64
resp = json.load(sys.stdin)
for part in resp['candidates'][0]['content']['parts']:
    if 'inlineData' in part:
        img_data = base64.b64decode(part['inlineData']['data'])
        with open('OUTPUT_PATH', 'wb') as f:
            f.write(img_data)
        print('Thumb salva')
    elif 'text' in part:
        print(part['text'])
"
```

**Prompt base para cada thumb:**
```
Crie uma thumbnail de YouTube 16:9 (1280x720).

REFERÊNCIA VISUAL: a primeira imagem é a thumbnail original. Mantenha o mesmo estilo visual:
cores, composição, elementos gráficos, textos sobrepostos e mood geral.

PESSOA: a segunda imagem e a foto de referencia do usuario. Substitua a pessoa da thumb original
pelo usuario (ou adicione-o se nao havia pessoa). Mantenha a aparencia fiel: rosto, cabelo, estilo.

VARIAÇÃO [1/2/3]: [descrever a variação específica — ângulo, expressão, composição]

A thumbnail deve ser chamativa, com alto contraste e texto legível.
```

Salvar como:
- `thumb-v1.png`
- `thumb-v2.png`
- `thumb-v3.png`

### 6. Montar slides de contexto

Gerar 3-4 slides que dão o contexto/introdução do vídeo usando NanoBanana com o branding padrão:

Ler branding em `conteudo/live-2026-03-19/ref/branding-nanobanana.md` se existir, senão usar:
- Fundo gradiente escuro navy/purple (#1a1a2e → #16213e)
- Título em serif branca (Playfair Display)
- Visual minimalista, muito espaço negativo

Slides sugeridos:
1. **Titulo** — nome do video reescrito no tom do usuario
2. **Problema/contexto** — qual dor ou curiosidade o vídeo resolve
3. **Sacada principal** — o insight mais forte do conteúdo
4. **CTA** — chamada para ação (se inscrever, comentar, link)

Salvar como `slide-01.png`, `slide-02.png`, etc.

### 7. Montar canvas Obsidian

Criar um arquivo `.canvas` (formato JSON do Obsidian) que organiza tudo visualmente:

```json
{
  "nodes": [
    {"id": "1", "type": "file", "file": "PATH/thumb-original.png", "x": 0, "y": 0, "width": 400, "height": 225},
    {"id": "2", "type": "file", "file": "PATH/thumb-v1.png", "x": 450, "y": 0, "width": 400, "height": 225},
    {"id": "3", "type": "file", "file": "PATH/thumb-v2.png", "x": 450, "y": 260, "width": 400, "height": 225},
    {"id": "4", "type": "file", "file": "PATH/thumb-v3.png", "x": 450, "y": 520, "width": 400, "height": 225},
    {"id": "5", "type": "file", "file": "PATH/roteiro-usuario.md", "x": 900, "y": 0, "width": 500, "height": 400},
    {"id": "6", "type": "file", "file": "PATH/transcricao.md", "x": 900, "y": 440, "width": 500, "height": 300},
    {"id": "7", "type": "file", "file": "PATH/slide-01.png", "x": 0, "y": 300, "width": 400, "height": 225},
    {"id": "8", "type": "file", "file": "PATH/slide-02.png", "x": 0, "y": 560, "width": 400, "height": 225}
  ],
  "edges": [
    {"id": "e1", "fromNode": "1", "toNode": "2", "fromSide": "right", "toSide": "left", "label": "variações"},
    {"id": "e2", "fromNode": "1", "toNode": "5", "fromSide": "right", "toSide": "left", "label": "roteiro"}
  ]
}
```

Salvar como `conteudo/yt-remake/YYYY-MM-DD-slug/remake.canvas`

### 8. Resumo final

Apresentar ao usuário:
```
YouTube Remaker — Concluído

  Vídeo: [título original]
  Pasta: conteudo/yt-remake/YYYY-MM-DD-slug/

  Arquivos gerados:
  - thumb-original.png (baixada)
  - thumb-v1.png, thumb-v2.png, thumb-v3.png (com clone)
  - transcricao.md (transcrição completa)
  - roteiro-usuario.md (reescrito na sua voz)
  - slide-01.png ... slide-0X.png (slides de contexto)
  - remake.canvas (visualização no Obsidian)

  Abra o canvas no Obsidian para ver tudo organizado.
```

## Regras

- Sempre ler `conteudo/voz-usuario.md` antes de reescrever — é o DNA do roteiro
- Sempre ler TODAS as fotos em `refs/clone-usuario/` para referência visual
- Se `refs/clone-usuario/` estiver vazia → avisar o usuário para adicionar fotos antes de gerar thumbs
- Manter estrutura de pastas limpa: uma pasta por remake
- O canvas deve referenciar caminhos relativos ao vault (sem path absoluto)
