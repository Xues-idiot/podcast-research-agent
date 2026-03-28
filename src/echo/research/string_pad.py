"""字符串填充工具"""

from typing import Optional


class StringPadTool:
    _instance: Optional["StringPadTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pad_left(self, text: str, width: int, char: str = " ") -> str:
        return text.rjust(width, char)

    def pad_right(self, text: str, width: int, char: str = " ") -> str:
        return text.ljust(width, char)

    def center(self, text: str, width: int, char: str = " ") -> str:
        return text.center(width, char)


def get_string_pad_tool() -> StringPadTool:
    return StringPadTool()