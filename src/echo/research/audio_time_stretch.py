"""音频时间拉伸工具"""

from typing import List, Optional


class AudioTimeStretchTool:
    _instance: Optional["AudioTimeStretchTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def time_stretch(self, signal: List[float], factor: float = 1.0) -> List[float]:
        if not signal or factor == 1.0:
            return signal
        factor = max(0.1, min(10.0, factor))
        n = len(signal)
        result = []
        for i in range(int(n / factor)):
            src_idx = int(i * factor)
            if src_idx < n:
                result.append(signal[src_idx])
        while len(result) < n:
            result.append(0.0)
        return result[:n]


def get_audio_time_stretch_tool() -> AudioTimeStretchTool:
    return AudioTimeStretchTool()