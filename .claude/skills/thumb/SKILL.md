---
name: thumb
description: Recebe uma URL do YouTube, baixa a thumbnail em alta resolução e salva em assets/thumbnails/. Usa yt-dlp.
---

Baixa a thumbnail de um vídeo do YouTube e salva em `assets/thumbnails/`.

## Uso

O usuário chama `/thumb` passando uma URL do YouTube como argumento.

Exemplo: `/thumb https://www.youtube.com/watch?v=dQw4w9WgXcQ`

## Fluxo

1. Recebe a URL do YouTube do primeiro argumento
2. Verifica se a URL foi fornecida (se não, pede ao usuário)
3. Cria a pasta `assets/thumbnails/` se não existir
4. Usa `yt-dlp` para baixar a thumbnail em alta resolução
5. Converte para JPG
6. Informa o caminho do arquivo salvo

## Comando

```bash
yt-dlp --skip-download --write-thumbnail --convert-thumbnails jpg -o "assets/thumbnails/%(title)s.%(ext)s" "URL_AQUI"
```

## Dependências

- `yt-dlp` (instalado via `brew install yt-dlp`)

## Onde salvar

- Pasta: `assets/thumbnails/`
- Padrão de nome: título do vídeo (gerado automaticamente pelo yt-dlp)
