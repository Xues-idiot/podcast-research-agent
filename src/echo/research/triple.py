"""三元组工具"""

from typing import Optional, Any


class TripleTool:
    """三元组工具"""

    def make_triple(self, a: Any, b: Any, c: Any) -> tuple:
        """创建三元组"""
        return (a, b, c)

    def unpair_triple(self, triple: tuple) -> tuple:
        """解三元组"""
        return triple


_triple: Optional[TripleTool] = None


def get_triple_tool() -> TripleTool:
    global _triple
    if _triple is None:
        _triple = TripleTool()
    return _triple