"""音频位深压缩工具"""

import math
from typing import List, Optional


class AudioBitcrushTool:
    _instance: Optional["AudioBitcrushTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def bitcrush(self, signal: List[float], bits: int = 8, mix: float = 0.5) -> List[float]:
        if not signal:
            return []
        bits = max(1, min(16, bits))
        levels = 2 ** bits
        result = [math.floor(s * levels) / levels for s in signal]
        return [signal[i] * (1 - mix) + result[i] * mix for i in range(len(signal))]


def get_audio_bitcrush_tool() -> AudioBitcrushTool:
    return AudioBitcrushTool()