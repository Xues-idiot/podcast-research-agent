"""音频限制器工具"""

from typing import List, Optional


class AudioLimiterTool:
    _instance: Optional["AudioLimiterTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def limit(self, signal: List[float], threshold: float = 0.9) -> List[float]:
        if not signal:
            return []
        threshold = max(0.0, min(1.0, threshold))
        return [max(-threshold, min(threshold, s)) for s in signal]


def get_audio_limiter_tool() -> AudioLimiterTool:
    return AudioLimiterTool()