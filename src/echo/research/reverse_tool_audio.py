"""反转工具v2"""

from typing import List, Optional


class ReverseToolAudio:
    _instance: Optional["ReverseToolAudio"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse(self, signal: List[float]) -> List[float]:
        return list(reversed(signal))


def get_reverse_tool_audio() -> ReverseToolAudio:
    return ReverseToolAudio()
