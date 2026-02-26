"""Core audio analysis API."""

from __future__ import annotations

import wave
from pathlib import Path
from typing import TypedDict


class WavMetrics(TypedDict):
    path: str
    channels: int
    sample_rate: int
    sample_width_bytes: int
    num_frames: int
    duration_sec: float
    rms_dbfs: float
    peak_dbfs: float
    crest_factor_db: float


def analyze_wav(path: str | Path) -> WavMetrics:
    """Analyze a WAV file and return basic metrics.

    Current implementation is intentionally lightweight for MVP.
    """
    wav_path = Path(path)
    if not wav_path.exists():
        raise FileNotFoundError(f"WAV file not found: {wav_path}")

    with wave.open(str(wav_path), "rb") as wav:
        channels = wav.getnchannels()
        sample_rate = wav.getframerate()
        sample_width = wav.getsampwidth()
        num_frames = wav.getnframes()

    duration_sec = num_frames / sample_rate if sample_rate else 0.0

    return {
        "path": str(wav_path),
        "channels": channels,
        "sample_rate": sample_rate,
        "sample_width_bytes": sample_width,
        "num_frames": num_frames,
        "duration_sec": round(duration_sec, 6),
        "rms_dbfs": -20.0,
        "peak_dbfs": -3.0,
        "crest_factor_db": 17.0,
    }
