"""行操作工具"""

from typing import Optional


class LineOperator:
    """行操作工具"""

    def count_lines(self, text: str) -> int:
        """计算行数"""
        return len(text.split("\n"))

    def get_lines(self, text: str) -> list:
        """获取所有行"""
        return text.split("\n")

    def join_lines(self, lines: list, separator: str = "\n") -> str:
        """连接行"""
        return separator.join(lines)


_operator: Optional[LineOperator] = None


def get_line_operator() -> LineOperator:
    global _operator
    if _operator is None:
        _operator = LineOperator()
    return _operator