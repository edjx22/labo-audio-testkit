# labo-audio-testkit

Audio measurement & DSP test toolkit with CLI + report outputs.

## 30 秒快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python scripts/generate_example_wav.py
python -m labo_audio_testkit analyze examples/assets/example.wav -o out/metrics.json
cat out/metrics.json
```

## 命令行示例

```bash
python -m labo_audio_testkit --help
python -m labo_audio_testkit analyze examples/assets/example.wav -o out/metrics.json
python -m labo_audio_testkit analyze examples/assets/example.wav -o out/metrics.json --report md --report-out out/report.md
```

## Python API 示例

```python
from labo_audio_testkit import analyze_wav, write_markdown_report

metrics = analyze_wav("examples/assets/example.wav")
write_markdown_report("examples/assets/example.wav", metrics, "out/report.md")
print(metrics)
```

## Generate report

```bash
python -m labo_audio_testkit analyze \
  examples/assets/example.wav \
  -o out/metrics.json \
  --report md \
  --report-out out/report.md
```

生成的 `out/report.md` 至少包含文件名、采样率、声道数、时长，以及 `metrics.json` 里的关键指标表格。

## Demo

```bash
python examples/demo.py
```

## Example Analysis Output

Run:

```bash
python -m labo_audio_testkit analyze examples/assets/example.wav -o out/metrics.json --report md
```

## 开发

```bash
pip install -e .[dev]
ruff format .
ruff check .
mypy src tests
pytest
```

## Roadmap

1. 完整频域与时域指标（THD+N、SNR、LUFS、频响偏差）
2. 多格式输入（WAV/FLAC）与批处理任务
3. 可复用的测量 profile（JSON/YAML）
4. HTML/PDF 报告输出与图表可视化
5. 插件回归测试工作流（离线渲染 + golden references）
