import json
import subprocess
import sys
from pathlib import Path


def test_cli_analyze_writes_json(tmp_path: Path) -> None:
    output_path = tmp_path / "metrics.json"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "labo_audio_testkit",
            "analyze",
            "examples/assets/example.wav",
            "-o",
            str(output_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert output_path.exists()

    data = json.loads(output_path.read_text(encoding="utf-8"))
    assert data["sample_rate"] == 48000


def test_cli_analyze_writes_markdown_report(tmp_path: Path) -> None:
    output_path = tmp_path / "metrics.json"
    report_path = tmp_path / "report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "labo_audio_testkit",
            "analyze",
            "examples/assets/example.wav",
            "-o",
            str(output_path),
            "--report",
            "md",
            "--report-out",
            str(report_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert report_path.exists()
    assert "Wrote report to" in result.stdout
    assert "Sample rate" in report_path.read_text(encoding="utf-8")


def test_cli_spectrum_runs_successfully(tmp_path: Path) -> None:
    output_path = tmp_path / "spectrum.png"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "labo_audio_testkit",
            "spectrum",
            "examples/assets/example.wav",
            "--out",
            str(output_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert "Wrote spectrum to" in result.stdout


def test_cli_spectrum_writes_output_file(tmp_path: Path) -> None:
    output_path = tmp_path / "spectrum.png"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "labo_audio_testkit",
            "spectrum",
            "examples/assets/example.wav",
            "--out",
            str(output_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_module_help() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "labo_audio_testkit", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "analyze" in result.stdout
    assert "spectrum" in result.stdout
