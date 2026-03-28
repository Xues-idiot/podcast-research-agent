"""音频淡入淡出工具"""

from typing import List, Optional


class AudioFadeTool:
    _instance: Optional["AudioFadeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fade_in(self, signal: List[float], samples: int = 1000) -> List[float]:
        if not signal:
            return []
        samples = max(1, min(len(signal), samples))
        result = [0.0] * samples
        for i in range(samples):
            result.append(signal[i])
        return [signal[i] * (i / samples) if i < samples else signal[i] for i in range(len(signal))]

    def fade_out(self, signal: List[float], samples: int = 1000) -> List[float]:
        if not signal:
            return []
        samples = max(1, min(len(signal), samples))
        return [signal[i] * ((len(signal) - i) / samples) if i >= len(signal) - samples else signal[i] for i in range(len(signal))]


def get_audio_fade_tool() -> AudioFadeTool:
    return AudioFadeTool()