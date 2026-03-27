"""连接工具"""

from typing import Optional


class Joiner:
    """连接工具"""

    def join_with(self, items: list, delimiter: str = ", ") -> str:
        """带分隔符连接"""
        return delimiter.join(str(i) for i in items)

    def join_lines(self, lines: list) -> str:
        """连接行"""
        return '\n'.join(lines)

    def join_paths(self, *parts: str) -> str:
        """连接路径"""
        import os
        return os.path.join(*parts)


_joiner: Optional[Joiner] = None


def get_joiner() -> Joiner:
    global _joiner
    if _joiner is None:
        _joiner = Joiner()
    return _joiner