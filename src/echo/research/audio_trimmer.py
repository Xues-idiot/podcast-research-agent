"""音频裁剪工具"""

from typing import List, Optional


class AudioTrimmerTool:
    _instance: Optional["AudioTrimmerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trim(self, signal: List[float], start: int = 0, end: int = -1) -> List[float]:
        if not signal:
            return []
        if end < 0 or end > len(signal):
            end = len(signal)
        if start >= len(signal):
            return []
        return signal[start:end]


def get_audio_trimmer_tool() -> AudioTrimmerTool:
    return AudioTrimmerTool()