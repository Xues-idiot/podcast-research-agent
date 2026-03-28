"""音频 vibrato 效果工具"""

import math
from typing import List, Optional


class AudioVibratoTool:
    _instance: Optional["AudioVibratoTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def vibrato(self, signal: List[float], rate: float = 6.0, depth: float = 0.01, mix: float = 0.5) -> List[float]:
        if not signal:
            return []
        n = len(signal)
        base_delay = int(0.02 * n)
        max_dev = int(depth * n)
        result = []
        for i in range(n):
            mod = int(max_dev * math.sin(2 * math.pi * rate * i / n))
            delay = max(0, min(n - 1, base_delay + mod))
            delayed = signal[i - delay] if i >= delay else 0.0
            result.append(signal[i] * (1 - mix) + delayed * mix)
        return result


def get_audio_vibrato_tool() -> AudioVibratoTool:
    return AudioVibratoTool()