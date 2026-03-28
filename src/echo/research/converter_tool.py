"""音频转换工具"""

from typing import List


class ConverterTool:
    _instance: ConverterTool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_mono(self, stereo: List[List[float]]) -> List[float]:
        if not stereo:
            return []
        return [(stereo[i][0] + stereo[i][1]) / 2 for i in range(len(stereo))]


def get_converter_tool() -> ConverterTool:
    return ConverterTool()
