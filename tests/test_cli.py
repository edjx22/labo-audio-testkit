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


def test_module_help() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "labo_audio_testkit", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "analyze" in result.stdout
