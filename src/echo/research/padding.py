"""文本填充工具"""

from typing import Optional


class TextPadder:
    """文本填充工具"""

    def pad_left(self, text: str, width: int, char: str = " ") -> str:
        """左填充"""
        return text.rjust(width, char)

    def pad_right(self, text: str, width: int, char: str = " ") -> str:
        """右填充"""
        return text.ljust(width, char)

    def pad_center(self, text: str, width: int, char: str = " ") -> str:
        """居中填充"""
        return text.center(width, char)

    def pad_both(self, text: str, width: int, char: str = " ") -> str:
        """两端填充"""
        left_space = (width - len(text)) // 2
        right_space = width - len(text) - left_space
        return char * left_space + text + char * right_space


_padder: Optional[TextPadder] = None


def get_text_padder() -> TextPadder:
    global _padder
    if _padder is None:
        _padder = TextPadder()
    return _padder