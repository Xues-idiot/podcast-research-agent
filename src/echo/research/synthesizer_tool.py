"""合成器工具"""

import math
from typing import List, Optional


class SynthesizerTool:
    _instance: Optional["SynthesizerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sine_wave(self, freq: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        return [math.sin(2 * math.pi * freq * i / sample_rate) for i in range(n)]

    def square_wave(self, freq: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        return [1.0 if math.sin(2 * math.pi * freq * i / sample_rate) > 0 else -1.0 for i in range(n)]

    def sawtooth_wave(self, freq: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        return [2 * (freq * i / sample_rate % 1) - 1 for i in range(n)]


def get_synthesizer_tool() -> SynthesizerTool:
    return SynthesizerTool()
