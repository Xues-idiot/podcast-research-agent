"""音频均衡器工具"""

from typing import List, Optional


class AudioEqTool:
    _instance: Optional["AudioEqTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def equalize(self, signal: List[float], low: float = 1.0, mid: float = 1.0, high: float = 1.0) -> List[float]:
        if not signal:
            return []
        n = len(signal)
        result = []
        for i in range(n):
            t = i / n
            gain = low * (1 - t) * (1 - t) + mid * 2 * (1 - t) * t + high * t * t
            result.append(signal[i] * gain)
        return result


def get_audio_eq_tool() -> AudioEqTool:
    return AudioEqTool()