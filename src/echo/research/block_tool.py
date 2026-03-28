"""分块工具v2"""

from typing import List, Optional


class BlockTool2:
    _instance: Optional["BlockTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def block(self, signal: List[float], size: int) -> List[List[float]]:
        return [signal[i:i + size] for i in range(0, len(signal), size)]


def get_block_tool2() -> BlockTool2:
    return BlockTool2()
