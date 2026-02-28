from pathlib import Path

from labo_audio_testkit import analyze_wav, write_markdown_report


def test_analyze_wav_returns_expected_fields() -> None:
    wav_path = Path("examples/assets/example.wav")
    metrics = analyze_wav(wav_path)

    assert metrics["sample_rate"] == 48000
    assert metrics["channels"] == 1
    assert metrics["duration_sec"] > 0
    assert "rms_dbfs" in metrics


def test_write_markdown_report_contains_summary_and_metrics(tmp_path: Path) -> None:
    wav_path = Path("examples/assets/example.wav")
    metrics = analyze_wav(wav_path)
    report_path = tmp_path / "report.md"

    written_path = write_markdown_report(wav_path, metrics, report_path)

    content = written_path.read_text(encoding="utf-8")
    assert written_path == report_path
    assert "# Audio Analysis Report" in content
    assert "Sample rate" in content
    assert "| sample_rate | 48000 |" in content
