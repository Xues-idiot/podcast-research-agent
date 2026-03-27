"""字符串长度工具"""

from typing import Optional


class LengthStrTool:
    """字符串长度工具"""

    def length(self, text: str) -> int:
        """长度"""
        return len(text)


_length_str_tool: Optional[LengthStrTool] = None


def get_length_str_tool() -> LengthStrTool:
    global _length_str_tool
    if _length_str_tool is None:
        _length_str_tool = LengthStrTool()
    return _length_str_tool