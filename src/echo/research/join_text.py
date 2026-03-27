"""连接文本工具"""

from typing import List, Optional


class JoinText:
    _instance: Optional["JoinText"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def join(self, items: List[str], delimiter: str = " ") -> str:
        return delimiter.join(items)

    def join_lines(self, lines: List[str]) -> str:
        return "\n".join(lines)


def get_join_text() -> JoinText:
    return JoinText()
