"""降采样工具"""

from typing import List, Optional


class DownsamplerTool:
    _instance: Optional["DownsamplerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def downsample(self, signal: List[float], factor: int) -> List[float]:
        if factor <= 1:
            return signal
        return [signal[i] for i in range(0, len(signal), factor)]


def get_downsampler_tool() -> DownsamplerTool:
    return DownsamplerTool()
