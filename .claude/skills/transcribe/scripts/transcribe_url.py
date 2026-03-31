#!/usr/bin/env python3
"""Transcribe audio from any video URL using yt-dlp + faster-whisper.

Downloads audio-only, transcribes with faster-whisper, prints transcript to stdout.
Supports YouTube, Instagram, X/Twitter, TikTok, Facebook, Vimeo, and 1000+ sites.

Usage:
    python3 transcribe_url.py <url> [--model medium] [--timestamps]
"""

import json
import os
import sys
import tempfile
from pathlib import Path


def check_dependencies():
    """Check all required dependencies and print install instructions if missing."""
    missing = []

    try:
        import yt_dlp  # noqa: F401
    except ImportError:
        missing.append("yt-dlp")

    try:
        from faster_whisper import WhisperModel  # noqa: F401
    except ImportError:
        missing.append("faster-whisper")

    # Check ffmpeg
    import shutil
    if not shutil.which("ffmpeg"):
        missing.append("ffmpeg")

    if missing:
        print("ERROR: Missing dependencies:", ", ".join(missing), file=sys.stderr)
        print("", file=sys.stderr)
        if "yt-dlp" in missing or "faster-whisper" in missing:
            pip_pkgs = [p for p in missing if p != "ffmpeg"]
            if pip_pkgs:
                print(f"  pip3 install {' '.join(pip_pkgs)}", file=sys.stderr)
        if "ffmpeg" in missing:
            print("  brew install ffmpeg  # macOS", file=sys.stderr)
            print("  sudo apt install ffmpeg  # Ubuntu/Debian", file=sys.stderr)
        sys.exit(1)


def format_timestamp(seconds: float) -> str:
    """Convert seconds to M:SS or H:MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def download_audio(url: str, output_dir: str) -> tuple[str, dict]:
    """Download audio-only from URL using yt-dlp. Returns (audio_path, info_dict)."""
    import yt_dlp

    output_template = os.path.join(output_dir, "%(id)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "0",
        }],
        "outtmpl": output_template,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # yt-dlp converts to wav, so the output file has .wav extension
        audio_path = os.path.join(output_dir, f"{info['id']}.wav")
        return audio_path, info


def transcribe_audio(audio_path: str, model_size: str) -> tuple[list, dict]:
    """Transcribe audio file with faster-whisper. Returns (segments, info)."""
    from faster_whisper import WhisperModel

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments_iter, info = model.transcribe(audio_path, beam_size=5)

    segments = []
    for segment in segments_iter:
        segments.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": segment.text.strip(),
            "start_formatted": format_timestamp(segment.start),
        })

    return segments, info


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 transcribe_url.py <url> [--model medium] [--timestamps]")
        sys.exit(1)

    url = sys.argv[1]
    model_size = "medium"
    show_timestamps = False

    # Parse flags
    args = sys.argv[2:]
    if "--model" in args:
        idx = args.index("--model")
        if idx + 1 < len(args):
            model_size = args[idx + 1]
    if "--timestamps" in args:
        show_timestamps = True

    check_dependencies()

    tmp_dir = tempfile.mkdtemp()

    try:
        # Download audio
        print("Downloading audio...", file=sys.stderr)
        audio_path, video_info = download_audio(url, tmp_dir)

        title = video_info.get("title", "Unknown")
        duration = video_info.get("duration", 0)
        platform = video_info.get("extractor", "Unknown")
        uploader = video_info.get("uploader", "Unknown")

        # Transcribe
        print(f"Transcribing with {model_size} model...", file=sys.stderr)
        segments, trans_info = transcribe_audio(audio_path, model_size)

        # Print metadata header
        print(f"--- {platform} | {title} | {uploader} | {format_timestamp(duration or trans_info.duration)} ---")
        print()

        # Print transcript
        if show_timestamps:
            for seg in segments:
                print(f"[{seg['start_formatted']}] {seg['text']}")
        else:
            # Group into paragraphs (~30s chunks)
            paragraphs = []
            current = []
            para_start = 0

            for seg in segments:
                current.append(seg["text"])
                if seg["start"] - para_start >= 30:
                    paragraphs.append(" ".join(current))
                    current = []
                    para_start = seg["start"]

            if current:
                paragraphs.append(" ".join(current))

            print("\n\n".join(paragraphs))

        print(f"\n--- Transcription complete | {len(segments)} segments | Language: {trans_info.language} ---", file=sys.stderr)

    finally:
        # Clean up downloaded audio
        import shutil
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
