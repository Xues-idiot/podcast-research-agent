"""音频混响工具"""

from typing import List, Optional
import math


class AudioReverbTool:
    _instance: Optional["AudioReverbTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverb(self, signal: List[float], room_size: float = 0.5, damping: float = 0.5, mix: float = 0.3) -> List[float]:
        if not signal:
            return []
        n = len(signal)
        decays = int(room_size * n * 0.1)
        delays = [int(decays * 0.1 * i) for i in range(1, 8)]
        result = signal[:]
        for d in delays:
            for i in range(d, n):
                idx = i - d
                decay = damping ** (d / n)
                result[i] += signal[idx] * decay * 0.15
        return [signal[i] * (1 - mix) + result[i] * mix for i in range(n)]


def get_audio_reverb_tool() -> AudioReverbTool:
    return AudioReverbTool()