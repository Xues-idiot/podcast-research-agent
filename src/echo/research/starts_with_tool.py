"""开头检查工具"""

from typing import Optional


class StartsWithTool:
    """开头检查工具"""

    def starts_with(self, text: str, prefix: str) -> bool:
        """开头检查"""
        return text.startswith(prefix)


_starts_with_tool: Optional[StartsWithTool] = None


def get_starts_with_tool() -> StartsWithTool:
    global _starts_with_tool
    if _starts_with_tool is None:
        _starts_with_tool = StartsWithTool()
    return _starts_with_tool