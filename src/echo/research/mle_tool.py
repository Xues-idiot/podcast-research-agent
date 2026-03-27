"""最大似然估计工具"""

import math
from typing import List, Optional


class MleTool:
    _instance: Optional["MleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def normal_mle(self, data: List[float]) -> Optional[List[float]]:
        if len(data) < 1:
            return None
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return [mean, math.sqrt(variance) if variance > 0 else 0]


def get_mle_tool() -> MleTool:
    return MleTool()
