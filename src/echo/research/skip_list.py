"""跳表工具"""

from typing import Any, Optional
import random


class SkipNode:
    def __init__(self, value: Any, level: int = 0):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipListTool:
    _instance: Optional["SkipListTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_node(self, value: Any, level: int) -> SkipNode:
        return SkipNode(value, level)

    def random_level(self, max_level: int = 16) -> int:
        level = 0
        while random.random() < 0.5 and level < max_level:
            level += 1
        return level


def get_skip_list_tool() -> SkipListTool:
    return SkipListTool()
