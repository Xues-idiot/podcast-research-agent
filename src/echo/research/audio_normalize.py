"""音频归一化工具"""

from typing import List, Optional


class AudioNormalizeTool:
    _instance: Optional["AudioNormalizeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def normalize(self, signal: List[float], target: float = 1.0) -> List[float]:
        if not signal:
            return []
        peak = max(abs(s) for s in signal)
        if peak == 0:
            return signal
        gain = target / peak
        return [s * gain for s in signal]


def get_audio_normalize_tool() -> AudioNormalizeTool:
    return AudioNormalizeTool()