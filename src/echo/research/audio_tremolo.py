"""音频颤音效果工具"""

import math
from typing import List, Optional


class AudioTremoloTool:
    _instance: Optional["AudioTremoloTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def tremolo(self, signal: List[float], rate: float = 5.0, depth: float = 0.5) -> List[float]:
        if not signal:
            return []
        n = len(signal)
        result = []
        for i in range(n):
            mod = (1.0 + depth * math.sin(2 * math.pi * rate * i / n))
            result.append(signal[i] * mod)
        return result


def get_audio_tremolo_tool() -> AudioTremoloTool:
    return AudioTremoloTool()