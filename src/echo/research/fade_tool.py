"""淡入淡出工具"""

from typing import List, Optional


class FadeTool:
    _instance: Optional["FadeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fade_in(self, signal: List[float], duration_ms: int = 1000, sample_rate: float = 44100) -> List[float]:
        samples = int(duration_ms * sample_rate / 1000)
        result = list(signal)
        for i in range(min(samples, len(result))):
            result[i] *= i / samples
        return result

    def fade_out(self, signal: List[float], duration_ms: int = 1000, sample_rate: float = 44100) -> List[float]:
        samples = int(duration_ms * sample_rate / 1000)
        result = list(signal)
        for i in range(min(samples, len(result))):
            result[-i - 1] *= i / samples
        return result


def get_fade_tool() -> FadeTool:
    return FadeTool()
