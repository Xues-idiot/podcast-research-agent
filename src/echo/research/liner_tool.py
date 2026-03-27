"""行处理工具"""

from typing import Optional, List


class LinerTool:
    """行处理工具"""

    def lines(self, text: str) -> List[str]:
        """获取行"""
        return text.split("\n")

    def join_lines(self, lines: List[str]) -> str:
        """连接行"""
        return "\n".join(lines)


_liner_tool: Optional[LinerTool] = None


def get_liner_tool() -> LinerTool:
    global _liner_tool
    if _liner_tool is None:
        _liner_tool = LinerTool()
    return _liner_tool