"""音频反转工具"""

from typing import List, Optional


class AudioReverseTool:
    _instance: Optional["AudioReverseTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse(self, signal: List[float]) -> List[float]:
        if not signal:
            return []
        return signal[::-1]


def get_audio_reverse_tool() -> AudioReverseTool:
    return AudioReverseTool()