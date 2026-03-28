"""波形生成器"""

import math
from typing import List, Optional


class WaveformGenerator:
    _instance: Optional["WaveformGenerator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate(self, waveform_type: str, freq: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        if waveform_type == "sine":
            return [math.sin(2 * math.pi * freq * i / sample_rate) for i in range(n)]
        elif waveform_type == "square":
            return [1.0 if math.sin(2 * math.pi * freq * i / sample_rate) > 0 else -1.0 for i in range(n)]
        elif waveform_type == "sawtooth":
            return [2 * (freq * i / sample_rate % 1) - 1 for i in range(n)]
        return [0.0] * n


def get_waveform_generator() -> WaveformGenerator:
    return WaveformGenerator()
