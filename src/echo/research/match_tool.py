"""匹配工具"""

from typing import Optional, Any, Callable, List


class MatchTool:
    """匹配工具"""

    def match(self, value: Any, patterns: List[tuple]) -> Any:
        """模式匹配"""
        for pattern, result in patterns:
            if value == pattern:
                return result
        return None


_match_tool: Optional[MatchTool] = None


def get_match_tool() -> MatchTool:
    global _match_tool
    if _match_tool is None:
        _match_tool = MatchTool()
    return _match_tool