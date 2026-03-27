"""连接工具"""

from typing import Optional, List


class JoinTool:
    """连接工具"""

    def join(self, items: List[str], delimiter: str) -> str:
        """连接"""
        return delimiter.join(items)


_join_tool: Optional[JoinTool] = None


def get_join_tool() -> JoinTool:
    global _join_tool
    if _join_tool is None:
        _join_tool = JoinTool()
    return _join_tool