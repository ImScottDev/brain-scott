#!/usr/bin/env python3
"""
Kling 3.0 Image-to-Video — Anima uma imagem de referência.

Uso:
    python3 animate.py <image_path> [--prompt "..."] [--duration 5|10] [--mode std|pro] [--output output.mp4]

Requer:
    pip3 install PyJWT requests
    Variáveis de ambiente: KLING_ACCESS_KEY, KLING_SECRET_KEY
"""

import argparse
import base64
import json
import os
import sys
import time

try:
    import jwt
except ImportError:
    print("ERRO: PyJWT não instalado. Rode: pip3 install PyJWT")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("ERRO: requests não instalado. Rode: pip3 install requests")
    sys.exit(1)

API_BASE = "https://api.klingai.com"


def generate_jwt(access_key: str, secret_key: str) -> str:
    now = int(time.time())
    headers = {"alg": "HS256", "typ": "JWT"}
    payload = {
        "iss": access_key,
        "exp": now + 1800,
        "nbf": now - 5,
    }
    return jwt.encode(payload, secret_key, headers=headers)


def image_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def create_task(token: str, image_b64: str, prompt: str, duration: str, mode: str) -> str:
    url = f"{API_BASE}/v1/videos/image2video"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = {
        "model_name": "kling-v3",
        "image": image_b64,
        "prompt": prompt,
        "duration": duration,
        "mode": mode,
    }
    resp = requests.post(url, headers=headers, json=body, timeout=30)
    data = resp.json()

    if data.get("code") != 0:
        print(f"ERRO ao criar task: {json.dumps(data, indent=2)}")
        sys.exit(1)

    task_id = data["data"]["task_id"]
    print(f"Task criada: {task_id}")
    return task_id


def poll_task(token: str, task_id: str, timeout: int = 300) -> str:
    url = f"{API_BASE}/v1/videos/image2video/{task_id}"
    headers = {"Authorization": f"Bearer {token}"}
    start = time.time()

    while time.time() - start < timeout:
        resp = requests.get(url, headers=headers, timeout=30)
        data = resp.json()

        if data.get("code") != 0:
            print(f"ERRO ao consultar task: {json.dumps(data, indent=2)}")
            sys.exit(1)

        status = data["data"]["task_status"]
        elapsed = int(time.time() - start)
        print(f"  [{elapsed}s] Status: {status}")

        if status == "succeed":
            video_url = data["data"]["task_result"]["videos"][0]["url"]
            duration = data["data"]["task_result"]["videos"][0].get("duration", "?")
            print(f"Video gerado! Duração: {duration}s")
            return video_url
        elif status == "failed":
            msg = data["data"].get("task_status_msg", "sem detalhes")
            print(f"ERRO: Task falhou — {msg}")
            sys.exit(1)

        time.sleep(5)

    print("ERRO: Timeout — video não ficou pronto a tempo")
    sys.exit(1)


def download_video(video_url: str, output_path: str):
    print(f"Baixando video para {output_path}...")
    resp = requests.get(video_url, stream=True, timeout=60)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Salvo: {output_path} ({size_mb:.1f} MB)")


def main():
    parser = argparse.ArgumentParser(description="Kling 3.0 — Anima imagem em vídeo")
    parser.add_argument("image", help="Caminho da imagem de referência")
    parser.add_argument("--prompt", default="Subtle, elegant motion. The elements gently animate with smooth transitions, like a premium Apple keynote presentation. Camera slowly zooms in.",
                        help="Prompt descrevendo a animação desejada")
    parser.add_argument("--duration", default="5", choices=["5", "10"],
                        help="Duração do vídeo em segundos (default: 5)")
    parser.add_argument("--mode", default="std", choices=["std", "pro"],
                        help="Modo de geração: std (rápido) ou pro (qualidade)")
    parser.add_argument("--output", default=None,
                        help="Caminho do vídeo de saída (default: mesmo nome da imagem .mp4)")
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"ERRO: Imagem não encontrada: {args.image}")
        sys.exit(1)

    access_key = os.environ.get("KLING_ACCESS_KEY")
    secret_key = os.environ.get("KLING_SECRET_KEY")
    if not access_key or not secret_key:
        print("ERRO: Defina KLING_ACCESS_KEY e KLING_SECRET_KEY nas variáveis de ambiente")
        sys.exit(1)

    output = args.output
    if not output:
        base = os.path.splitext(args.image)[0]
        output = f"{base}.mp4"

    print(f"Imagem: {args.image}")
    print(f"Prompt: {args.prompt}")
    print(f"Duração: {args.duration}s | Modo: {args.mode}")
    print(f"Output: {output}")
    print()

    print("Gerando JWT...")
    token = generate_jwt(access_key, secret_key)

    print("Codificando imagem em base64...")
    image_b64 = image_to_base64(args.image)

    print("Enviando para Kling 3.0...")
    task_id = create_task(token, image_b64, args.prompt, args.duration, args.mode)

    print("Aguardando geração do vídeo...")
    video_url = poll_task(token, task_id)

    download_video(video_url, output)
    print(f"\nPronto! Video salvo em: {output}")


if __name__ == "__main__":
    main()
