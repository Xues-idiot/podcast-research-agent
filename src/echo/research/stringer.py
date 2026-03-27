"""字符串构建工具"""

from typing import Optional


class Stringer:
    """字符串构建工具"""

    def build(self, *parts) -> str:
        """构建字符串"""
        return "".join(str(p) for p in parts)


_stringer: Optional[Stringer] = None


def get_stringer() -> Stringer:
    global _stringer
    if _stringer is None:
        _stringer = Stringer()
    return _stringer