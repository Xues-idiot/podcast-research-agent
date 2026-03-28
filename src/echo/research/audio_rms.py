"""音频RMS工具"""

import math
from typing import List, Optional


class AudioRmsTool:
    _instance: Optional["AudioRmsTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rms(self, signal: List[float]) -> float:
        if not signal:
            return 0.0
        return math.sqrt(sum(s * s for s in signal) / len(signal))

    def rms_windowed(self, signal: List[float], window_size: int = 1024) -> List[float]:
        if not signal or window_size <= 0:
            return []
        result = []
        for i in range(0, len(signal), window_size):
            chunk = signal[i:i + window_size]
            result.append(self.rms(chunk))
        return result


def get_audio_rms_tool() -> AudioRmsTool:
    return AudioRmsTool()