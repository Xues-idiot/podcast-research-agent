"""音频反转工具"""

from typing import List, Optional


class AudioReverser:
    _instance: Optional["AudioReverser"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse(self, signal: List[float]) -> List[float]:
        return list(reversed(signal))


def get_audio_reverser() -> AudioReverser:
    return AudioReverser()
