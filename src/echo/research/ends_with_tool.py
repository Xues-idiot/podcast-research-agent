"""结尾检查工具"""

from typing import Optional


class EndsWithTool:
    """结尾检查工具"""

    def ends_with(self, text: str, suffix: str) -> bool:
        """结尾检查"""
        return text.endswith(suffix)


_ends_with_tool: Optional[EndsWithTool] = None


def get_ends_with_tool() -> EndsWithTool:
    global _ends_with_tool
    if _ends_with_tool is None:
        _ends_with_tool = EndsWithTool()
    return _ends_with_tool