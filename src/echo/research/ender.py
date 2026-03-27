"""结束符工具"""

from typing import Optional


class EnderTool:
    """结束符工具"""

    def add_period(self, text: str) -> str:
        """添加句号"""
        if not text:
            return text
        if text.endswith(".") or text.endswith("!") or text.endswith("?"):
            return text
        return text + "."

    def add_question(self, text: str) -> str:
        """添加问号"""
        if not text:
            return text
        if text.endswith("?") or text.endswith("!") or text.endswith("."):
            return text
        return text + "?"

    def add_exclamation(self, text: str) -> str:
        """添加感叹号"""
        if not text:
            return text
        if text.endswith("!") or text.endswith("?") or text.endswith("."):
            return text
        return text + "!"


_ender_tool: Optional[EnderTool] = None


def get_ender_tool() -> EnderTool:
    global _ender_tool
    if _ender_tool is None:
        _ender_tool = EnderTool()
    return _ender_tool