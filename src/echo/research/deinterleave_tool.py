"""解交织工具"""

from typing import List, Optional


class DeinterleaveTool:
    _instance: Optional["DeinterleaveTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def deinterleave(self, signal: List[float], num_channels: int) -> List[List[float]]:
        result = [[] for _ in range(num_channels)]
        for i, s in enumerate(signal):
            result[i % num_channels].append(s)
        return result


def get_deinterleave_tool() -> DeinterleaveTool:
    return DeinterleaveTool()
