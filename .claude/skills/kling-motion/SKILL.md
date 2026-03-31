Anima slides e imagens em vídeo usando Kling 3.0 (image-to-video). Envia imagem de referência e retorna vídeo MP4 com motion sutil estilo keynote.

## Install

Se o usuário disser `/kling-motion install` ou `/kling-motion setup`, rodar o wizard:

### Step 1: Check Python 3 + dependências

```bash
python3 --version
pip3 show PyJWT 2>/dev/null && echo "OK: PyJWT" || echo "MISSING: PyJWT"
pip3 show requests 2>/dev/null && echo "OK: requests" || echo "MISSING: requests"
```

Instalar se faltar:
```bash
pip3 install PyJWT requests
```

### Step 2: Check API Keys

```bash
echo "KLING_ACCESS_KEY: ${KLING_ACCESS_KEY:-(NÃO DEFINIDA)}"
echo "KLING_SECRET_KEY: ${KLING_SECRET_KEY:-(NÃO DEFINIDA)}"
```

Se não estiverem definidas, orientar:
1. Acesse https://app.klingai.com/global/dev
2. Crie um par AccessKey + SecretKey
3. Adicione no seu shell profile (~/.zshrc):
```bash
export KLING_ACCESS_KEY="sua-access-key"
export KLING_SECRET_KEY="sua-secret-key"
```

### Step 3: Resumo

```
Kling Motion — Install Summary

  Python:         [OK/MISSING]
  PyJWT:          [OK/MISSING]
  requests:       [OK/MISSING]
  KLING_ACCESS_KEY: [OK/MISSING]
  KLING_SECRET_KEY: [OK/MISSING]
  Status:         [Pronto / X itens pendentes]

Teste: /kling-motion <caminho-da-imagem>
```

---

## Invocation

O usuário pode invocar de várias formas:

### Forma simples — uma imagem
```
/kling-motion <caminho_da_imagem>
```

### Com prompt customizado
```
/kling-motion <caminho_da_imagem> --prompt "Camera slowly zooms into the text"
```

### Batch — múltiplas imagens (ex: slides de um vídeo)
```
/kling-motion batch <pasta_com_imagens>
```

Se o argumento for uma pasta, processar TODAS as imagens .png/.jpg da pasta em sequência.

---

## Workflow — Imagem única

1. Perguntar ao usuário (se não veio nos argumentos):
   - **Prompt de animação?** (ou usar default: "Subtle, elegant motion. The elements gently animate with smooth transitions, like a premium Apple keynote presentation. Camera slowly zooms in.")
   - **Duração?** 5s ou 10s (default: 5)
   - **Modo?** std (rápido) ou pro (qualidade) (default: std)

2. Rodar o script:

```bash
python3 <skill_path>/scripts/animate.py "<image_path>" --prompt "<prompt>" --duration <5|10> --mode <std|pro> --output "<output_path>"
```

3. O script faz:
   - Gera JWT com as credenciais
   - Converte imagem em base64
   - Envia para Kling 3.0 (model: kling-v3)
   - Faz polling a cada 5s até completar (timeout: 5min)
   - Baixa o vídeo MP4

4. Apresentar o resultado: caminho do vídeo salvo.

---

## Workflow — Batch (pasta de slides)

1. Listar todas as imagens .png e .jpg na pasta, ordenadas por nome
2. Perguntar:
   - **Prompt de animação?** (mesmo prompt para todos, ou personalizado por slide?)
   - **Duração?** 5s ou 10s
   - **Modo?** std ou pro
3. Processar cada imagem sequencialmente:

```bash
python3 <skill_path>/scripts/animate.py "<image_1>" --prompt "<prompt>" --duration <dur> --mode <mode> --output "<pasta>/video-01.mp4"
python3 <skill_path>/scripts/animate.py "<image_2>" --prompt "<prompt>" --duration <dur> --mode <mode> --output "<pasta>/video-02.mp4"
# ... etc
```

4. Ao final, listar todos os vídeos gerados com status (sucesso/falha).

---

## Prompts sugeridos por tipo de slide

| Tipo de slide | Prompt sugerido |
|---|---|
| Texto puro (frase impactante) | "Camera slowly zooms in on the text. Subtle light shift on the background. Cinematic, elegant." |
| Slide com ícones/cards | "Elements gently fade in one by one. Smooth, minimal motion. Professional keynote animation." |
| Slide com tabela/dados | "Camera slowly pans across the data. Numbers subtly highlight. Clean, editorial motion." |
| Slide com imagem/render | "Gentle parallax motion on the image. Background subtly shifts. Premium product reveal feel." |
| Slide de transição | "Text elegantly fades in from black. Slow, deliberate reveal. Apple keynote style." |

---

## Output

- Vídeos salvos na mesma pasta da imagem, com extensão .mp4
- Nome: mesmo da imagem original (ex: `slide-01-problema.png` → `slide-01-problema.mp4`)
- Em batch: também cria `video-01.mp4`, `video-02.mp4` etc. numerados

---

## Erros comuns

- **"KLING_ACCESS_KEY não definida"** → Configurar variáveis de ambiente
- **"Task falhou"** → Imagem pode ser muito grande ou conteúdo bloqueado pela moderação
- **"Timeout"** → Kling pode estar sobrecarregado, tentar novamente
- **"PyJWT não instalado"** → `pip3 install PyJWT`
