"""音频镶边效果工具"""

import math
from typing import List, Optional


class AudioFlangerTool:
    _instance: Optional["AudioFlangerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flanger(self, signal: List[float], depth: float = 0.005, rate: float = 0.5, mix: float = 0.5) -> List[float]:
        if not signal:
            return []
        n = len(signal)
        base_delay = int(0.005 * n)
        result = []
        for i in range(n):
            mod = int(depth * n * (0.5 + 0.5 * math.sin(2 * math.pi * rate * i / n)))
            delay = max(0, min(n - 1, base_delay + mod))
            delayed = signal[i - delay] if i >= delay else 0.0
            result.append(signal[i] * (1 - mix) + delayed * mix)
        return result


def get_audio_flanger_tool() -> AudioFlangerTool:
    return AudioFlangerTool()