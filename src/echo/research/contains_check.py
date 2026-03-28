"""包含检查工具"""

from typing import Optional


class ContainsCheckTool:
    _instance: Optional["ContainsCheckTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def contains(self, text: str, substring: str) -> bool:
        return substring in text

    def starts_with(self, text: str, prefix: str) -> bool:
        return text.startswith(prefix)

    def ends_with(self, text: str, suffix: str) -> bool:
        return text.endswith(suffix)


def get_contains_check_tool() -> ContainsCheckTool:
    return ContainsCheckTool()