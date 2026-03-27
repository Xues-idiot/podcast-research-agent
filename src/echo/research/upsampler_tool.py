"""升采样工具"""

from typing import List


class UpsamplerTool:
    _instance: Optional["UpsamplerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def upsample(self, signal: List[float], factor: int) -> List[float]:
        if factor <= 1:
            return signal
        result = []
        for val in signal:
            result.append(val)
            for _ in range(factor - 1):
                result.append(0)
        return result


def get_upsampler_tool() -> UpsamplerTool:
    return UpsamplerTool()
