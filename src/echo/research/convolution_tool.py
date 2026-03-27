"""卷积工具"""

from typing import List


class ConvolutionTool:
    _instance: Optional["ConvolutionTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convolve(self, a: List[float], b: List[float]) -> List[float]:
        result = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                result[i + j] += x * y
        return result


def get_convolution_tool() -> ConvolutionTool:
    return ConvolutionTool()
