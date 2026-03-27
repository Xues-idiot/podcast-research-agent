"""替换工具"""

from typing import Optional


class ReplaceTool:
    """替换工具"""

    def replace(self, text: str, old: str, new: str) -> str:
        """替换"""
        return text.replace(old, new)


_replace_tool: Optional[ReplaceTool] = None


def get_replace_tool() -> ReplaceTool:
    global _replace_tool
    if _replace_tool is None:
        _replace_tool = ReplaceTool()
    return _replace_tool