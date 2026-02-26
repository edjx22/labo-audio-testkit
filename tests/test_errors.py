import pytest

from labo_audio_testkit import analyze_wav


def test_analyze_wav_raises_for_missing_file() -> None:
    with pytest.raises(FileNotFoundError):
        analyze_wav("this_file_does_not_exist.wav")
