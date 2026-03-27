"""字符串空检查工具"""

from typing import Optional


class IsEmptyStrTool:
    """字符串空检查工具"""

    def is_empty(self, text: str) -> bool:
        """是否为空"""
        return len(text.strip()) == 0


_is_empty_str_tool: Optional[IsEmptyStrTool] = None


def get_is_empty_str_tool() -> IsEmptyStrTool:
    global _is_empty_str_tool
    if _is_empty_str_tool is None:
        _is_empty_str_tool = IsEmptyStrTool()
    return _is_empty_str_tool