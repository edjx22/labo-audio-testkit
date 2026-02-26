"""Demo script: analyze bundled example WAV and print metrics."""

from __future__ import annotations

import json
from pathlib import Path

from labo_audio_testkit import analyze_wav

if __name__ == "__main__":
    wav = Path(__file__).parent / "assets" / "example.wav"
    metrics = analyze_wav(wav)
    print(json.dumps(metrics, indent=2))
