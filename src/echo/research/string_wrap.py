"""字符串包裹工具"""

import textwrap
from typing import Optional


class StringWrapTool:
    _instance: Optional["StringWrapTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def wrap(self, text: str, width: int = 80) -> str:
        return textwrap.fill(text, width=width)

    def wrap_words(self, text: str, width: int = 80) -> list:
        return textwrap.wrap(text, width=width)

    def indent(self, text: str, prefix: str = "    ") -> str:
        return textwrap.indent(text, prefix)


def get_string_wrap_tool() -> StringWrapTool:
    return StringWrapTool()