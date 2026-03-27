"""转小写工具"""

from typing import Optional


class LowerTool:
    """转小写工具"""

    def lower(self, text: str) -> str:
        """转小写"""
        return text.lower()


_lower_tool: Optional[LowerTool] = None


def get_lower_tool() -> LowerTool:
    global _lower_tool
    if _lower_tool is None:
        _lower_tool = LowerTool()
    return _lower_tool