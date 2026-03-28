"""缓冲区工具"""

from typing import List, Optional


class BufferTool:
    _instance: Optional["BufferTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, size: int, fill: float = 0.0) -> List[float]:
        return [fill] * size


def get_buffer_tool() -> BufferTool:
    return BufferTool()
