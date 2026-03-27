"""文本连接工具"""

from typing import Optional


class TextJoiner:
    """文本连接工具"""

    def join_lines(self, lines: list[str], separator: str = "\n") -> str:
        """连接行"""
        return separator.join(lines)

    def join_with_space(self, parts: list[str]) -> str:
        """用空格连接"""
        return " ".join(p for p in parts if p)

    def join_paragraphs(self, paragraphs: list[str]) -> str:
        """连接段落"""
        return "\n\n".join(p for p in paragraphs if p)


_joiner: Optional[TextJoiner] = None


def get_text_joiner() -> TextJoiner:
    global _joiner
    if _joiner is None:
        _joiner = TextJoiner()
    return _joiner