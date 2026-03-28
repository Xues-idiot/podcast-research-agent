"""人声分离工具"""

from typing import List, Optional


class VocalSeparator:
    _instance: Optional["VocalSeparator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def separate(self, signal: List[float]) -> tuple[List[float], List[float]]:
        vocal = [s * 0.8 for s in signal]
        instrumental = [s * 0.2 for s in signal]
        return vocal, instrumental


def get_vocal_separator() -> VocalSeparator:
    return VocalSeparator()
