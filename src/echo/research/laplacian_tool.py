"""拉普拉斯工具"""

from typing import List, Optional


class LaplacianTool:
    _instance: Optional["LaplacianTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def laplacian(self, signal: List[float]) -> List[float]:
        return [0.0] + [signal[i + 1] - 2 * signal[i] + signal[i - 1] for i in range(1, len(signal) - 1)] + [0.0]


def get_laplacian_tool() -> LaplacianTool:
    return LaplacianTool()
