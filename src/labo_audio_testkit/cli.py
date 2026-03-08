"""Command-line interface for labo_audio_testkit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .analyzer import analyze_wav, write_markdown_report, write_spectrum_plot


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="labo_audio_testkit",
        description="Audio measurement & DSP test toolkit with CLI + report outputs",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser("analyze", help="Analyze a WAV file")
    analyze_parser.add_argument("input_wav", type=Path, help="Path to input WAV file")
    analyze_parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Output metrics JSON path",
    )
    analyze_parser.add_argument(
        "--report",
        choices=["md"],
        help="Optional report format to generate",
    )
    analyze_parser.add_argument(
        "--report-out",
        type=Path,
        default=Path("out/report.md"),
        help="Output report path (default: out/report.md)",
    )

    spectrum_parser = subparsers.add_parser("spectrum", help="Generate a WAV spectrum plot")
    spectrum_parser.add_argument("input_wav", type=Path, help="Path to input WAV file")
    spectrum_parser.add_argument(
        "--out",
        type=Path,
        required=True,
        help="Output PNG path",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "analyze":
        metrics = analyze_wav(args.input_wav)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        print(f"Wrote metrics to {args.output}")
        if args.report == "md":
            report_path = write_markdown_report(args.input_wav, metrics, args.report_out)
            print(f"Wrote report to {report_path}")
        return 0

    if args.command == "spectrum":
        spectrum_path = write_spectrum_plot(args.input_wav, args.out)
        print(f"Wrote spectrum to {spectrum_path}")
        return 0

    parser.error("Unknown command")
    return 2
