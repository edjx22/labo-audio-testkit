from pathlib import Path

from labo_audio_testkit import analyze_wav


def test_analyze_wav_returns_expected_fields() -> None:
    wav_path = Path("examples/assets/example.wav")
    metrics = analyze_wav(wav_path)

    assert metrics["sample_rate"] == 48000
    assert metrics["channels"] == 1
    assert metrics["duration_sec"] > 0
    assert "rms_dbfs" in metrics
