"""抽取工具"""

from typing import List, Optional


class DecimateTool:
    _instance: Optional["DecimateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def decimate(self, signal: List[float], factor: int) -> List[float]:
        return [signal[i] for i in range(0, len(signal), factor)]


def get_decimate_tool() -> DecimateTool:
    return DecimateTool()
