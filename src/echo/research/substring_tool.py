"""子串工具"""

from typing import Optional


class SubstringTool:
    """子串工具"""

    def substring(self, text: str, start: int, end: int = None) -> str:
        """子串"""
        return text[start:end]


_substring_tool: Optional[SubstringTool] = None


def get_substring_tool() -> SubstringTool:
    global _substring_tool
    if _substring_tool is None:
        _substring_tool = SubstringTool()
    return _substring_tool