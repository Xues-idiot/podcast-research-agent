"""裁剪工具"""

from typing import List, Optional


class ClipTool:
    _instance: Optional["ClipTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def clip(self, signal: List[float], start: int, end: int) -> List[float]:
        return signal[start:end]


def get_clip_tool() -> ClipTool:
    return ClipTool()
