"""文本包裹工具"""

import textwrap
from typing import Optional


class Wrapper:
    """文本包裹工具"""

    def wrap(self, text: str, width: int = 80) -> str:
        """包裹文本"""
        return textwrap.fill(text, width=width)

    def wrap_lines(self, text: str, width: int = 80) -> list[str]:
        """逐行包裹"""
        return textwrap.wrap(text, width=width)

    def indent(self, text: str, prefix: str = "    ") -> str:
        """缩进文本"""
        return textwrap.indent(text, prefix)


_wrapper: Optional[Wrapper] = None


def get_wrapper() -> Wrapper:
    global _wrapper
    if _wrapper is None:
        _wrapper = Wrapper()
    return _wrapper