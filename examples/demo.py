"""Demo script: analyze bundled example WAV and generate outputs under out/."""

from __future__ import annotations

import json
from pathlib import Path

from labo_audio_testkit import analyze_wav, write_markdown_report

if __name__ == "__main__":
    wav = Path(__file__).parent / "assets" / "example.wav"
    out_dir = Path("out")
    out_dir.mkdir(parents=True, exist_ok=True)

    metrics = analyze_wav(wav)
    metrics_path = out_dir / "metrics.json"
    report_path = out_dir / "report.md"

    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    write_markdown_report(wav, metrics, report_path)

    print(f"Wrote metrics to {metrics_path}")
    print(f"Wrote report to {report_path}")
