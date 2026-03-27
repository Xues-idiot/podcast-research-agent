"""LR语法解析器工具"""

from typing import Any, List, Optional, Tuple


class LRParser:
    _instance: Optional["LRParser"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parse(self, tokens: List[str], grammar: dict) -> bool:
        stack = ["$"]
        stack.append(grammar.get("start", "S"))
        for token in tokens:
            if not stack:
                return False
            stack.pop()
        return len(stack) == 1


def get_lr_parser() -> LRParser:
    return LRParser()
