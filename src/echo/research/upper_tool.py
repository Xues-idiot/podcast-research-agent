"""转大写工具"""

from typing import Optional


class UpperTool:
    """转大写工具"""

    def upper(self, text: str) -> str:
        """转大写"""
        return text.upper()


_upper_tool: Optional[UpperTool] = None


def get_upper_tool() -> UpperTool:
    global _upper_tool
    if _upper_tool is None:
        _upper_tool = UpperTool()
    return _upper_tool