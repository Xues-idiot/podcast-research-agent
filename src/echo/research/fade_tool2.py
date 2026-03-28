"""淡出工具"""

from typing import List, Optional


class FadeOutTool:
    _instance: Optional["FadeOutTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fade_out(self, signal: List[float], duration_ms: int, sample_rate: float = 44100) -> List[float]:
        samples = int(duration_ms * sample_rate / 1000)
        result = list(signal)
        for i in range(min(samples, len(result))):
            result[-i - 1] *= i / samples if samples > 0 else 0
        return result


def get_fade_out_tool() -> FadeOutTool:
    return FadeOutTool()
