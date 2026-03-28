"""复制工具v2"""

from typing import List, Optional


class DuplicateTool:
    _instance: Optional["DuplicateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def duplicate(self, signal: List[float]) -> List[float]:
        return list(signal)


def get_duplicate_tool() -> DuplicateTool:
    return DuplicateTool()
