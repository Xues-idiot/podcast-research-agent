"""音频修剪工具"""

from typing import List


class TrimmerTool:
    _instance: TrimmerTool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trim(self, signal: List[float], start: int, end: int) -> List[float]:
        return signal[start:end]


def get_trimmer_tool() -> TrimmerTool:
    return TrimmerTool()
