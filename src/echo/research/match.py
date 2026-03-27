"""匹配工具"""

from typing import Optional, Any, Callable


class MatchTool:
    """匹配工具"""

    def match(self, value: Any, patterns: list) -> Any:
        """模式匹配"""
        for pattern, result in patterns:
            if pattern == value:
                return result
        return None


_tool: Optional[MatchTool] = None


def get_match_tool() -> MatchTool:
    global _tool
    if _tool is None:
        _tool = MatchTool()
    return _tool