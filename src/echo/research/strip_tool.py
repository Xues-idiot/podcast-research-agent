"""去除空白工具"""

from typing import Optional


class StripTool:
    """去除空白工具"""

    def strip(self, text: str) -> str:
        """去除空白"""
        return text.strip()


_strip_tool: Optional[StripTool] = None


def get_strip_tool() -> StripTool:
    global _strip_tool
    if _strip_tool is None:
        _strip_tool = StripTool()
    return _strip_tool