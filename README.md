# labo-audio-testkit

Audio measurement and DSP testing toolkit with CLI utilities and report generation.

---

# Quick Start (30 seconds)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

python scripts/generate_example_wav.py

python -m labo_audio_testkit analyze examples/assets/example.wav -o out/metrics.json

cat out/metrics.json
```

---

# CLI Usage

Show available commands:

```bash
python -m labo_audio_testkit --help
```

Basic analysis:

```bash
python -m labo_audio_testkit analyze examples/assets/example.wav -o out/metrics.json
```

Generate a report:

```bash
python -m labo_audio_testkit analyze \
  examples/assets/example.wav \
  -o out/metrics.json \
  --report md \
  --report-out out/report.md
```

---

# Python API Example

```python
from labo_audio_testkit import analyze_wav, write_markdown_report

metrics = analyze_wav("examples/assets/example.wav")
write_markdown_report("examples/assets/example.wav", metrics, "out/report.md")

print(metrics)
```

---

# Report Generation

Generate a Markdown report from analysis results:

```bash
python -m labo_audio_testkit analyze \
  examples/assets/example.wav \
  -o out/metrics.json \
  --report md \
  --report-out out/report.md
```

The generated report (`out/report.md`) includes:

* file name
* sample rate
* number of channels
* duration
* key metrics from `metrics.json`

---

# Spectrum Analyzer

Generate a frequency spectrum plot from a WAV file:

```bash
python -m labo_audio_testkit spectrum example.wav --out spectrum.png
```

Example using the repository sample audio:

```bash
python -m labo_audio_testkit spectrum \
  examples/assets/example.wav \
  --out out/spectrum.png
```

---

# Demo

Run the included demo script:

```bash
python examples/demo.py
```

---

# Example Analysis Output

Run:

```bash
python -m labo_audio_testkit analyze \
  examples/assets/example.wav \
  -o out/metrics.json \
  --report md
```

Example metrics output:

```json
{
  "sample_rate": 48000,
  "duration_sec": 0.1,
  "rms_dbfs": -20,
  "peak_dbfs": -3,
  "crest_factor_db": 17
}
```

---

# Development

Install development dependencies:

```bash
pip install -e .[dev]
```

Format and lint code:

```bash
ruff format .
ruff check .
```

Run type checks:

```bash
mypy src tests
```

Run tests:

```bash
pytest
```

---

# Roadmap

1. Full time-domain and frequency-domain metrics (THD+N, SNR, LUFS, frequency response)
2. Multi-format audio support (WAV / FLAC) and batch processing
3. Reusable measurement profiles (JSON / YAML)
4. HTML / PDF report generation with visualizations
5. Plugin regression testing workflow (offline rendering + golden references)
