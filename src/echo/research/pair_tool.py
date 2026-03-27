"""配对工具"""

from typing import Optional, Any


class PairTool:
    """配对工具"""

    def make_pair(self, a: Any, b: Any) -> tuple:
        """创建配对"""
        return (a, b)

    def unpair(self, pair: tuple) -> tuple:
        """解配对"""
        return pair


_pair: Optional[PairTool] = None


def get_pair_tool() -> PairTool:
    global _pair
    if _pair is None:
        _pair = PairTool()
    return _pair