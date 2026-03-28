"""文本反转工具"""

from typing import Optional


class TextReverseTool:
    _instance: Optional["TextReverseTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse_string(self, text: str) -> str:
        return text[::-1]

    def reverse_words(self, text: str) -> str:
        return ' '.join(text.split()[::-1])

    def reverse_lines(self, text: str) -> str:
        return '\n'.join(text.split('\n')[::-1])


def get_text_reverse_tool() -> TextReverseTool:
    return TextReverseTool()