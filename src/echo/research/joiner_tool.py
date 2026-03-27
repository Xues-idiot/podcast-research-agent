"""连接工具"""

from typing import Optional, Any


class JoinerTool:
    """连接工具"""

    def join(self, items: list, delimiter: str = "") -> str:
        """连接"""
        return delimiter.join(str(i) for i in items)

    def join_with(self, items: list, delimiter: str) -> str:
        """带分隔符连接"""
        return delimiter.join(items)


_joiner: Optional[JoinerTool] = None


def get_joiner_tool() -> JoinerTool:
    global _joiner
    if _joiner is None:
        _joiner = JoinerTool()
    return _joiner