"""Generate a tiny example WAV asset (1kHz sine)."""

from __future__ import annotations

import math
import wave
from pathlib import Path


def generate_sine_wav(
    output_path: Path,
    frequency_hz: float = 1000.0,
    duration_sec: float = 0.1,
    sample_rate: int = 48_000,
    amplitude: float = 0.3,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    n_samples = int(duration_sec * sample_rate)
    with wave.open(str(output_path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        frames = bytearray()
        for n in range(n_samples):
            sample = amplitude * math.sin(2.0 * math.pi * frequency_hz * (n / sample_rate))
            pcm = int(max(-1.0, min(1.0, sample)) * 32767)
            frames.extend(pcm.to_bytes(2, byteorder="little", signed=True))

        wav.writeframes(bytes(frames))


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "examples" / "assets" / "example.wav"
    generate_sine_wav(output)
    print(f"Generated: {output}")
