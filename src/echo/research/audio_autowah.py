"""音频自动哇音效果工具"""

import math
from typing import List, Optional


class AudioAutowahTool:
    _instance: Optional["AudioAutowahTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def autowah(self, signal: List[float], cutoff: float = 0.5, resonance: float = 2.0, mix: float = 0.5) -> List[float]:
        if not signal:
            return []
        cutoff = max(0.0, min(1.0, cutoff))
        resonance = max(0.1, min(10.0, resonance))
        envelope = 0.0
        result = []
        for s in signal:
            envelope = 0.3 * envelope + 0.7 * abs(s)
            wah = cutoff * resonance * envelope
            wah = max(0.0, min(1.0, wah))
            filtered = s * wah
            result.append(s * (1 - mix) + filtered * mix)
        return result


def get_audio_autowah_tool() -> AudioAutowahTool:
    return AudioAutowahTool()