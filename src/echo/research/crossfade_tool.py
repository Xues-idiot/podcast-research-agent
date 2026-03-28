"""交叉淡入淡出工具"""

from typing import List, Optional


class CrossfadeTool:
    _instance: Optional["CrossfadeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def crossfade(self, a: List[float], b: List[float], duration: int) -> List[float]:
        result = list(a)
        for i in range(min(duration, len(b), len(a))):
            ratio = i / duration
            result[-duration + i] = result[-duration + i] * (1 - ratio) + b[i] * ratio
        result.extend(b[duration:])
        return result


def get_crossfade_tool() -> CrossfadeTool:
    return CrossfadeTool()
