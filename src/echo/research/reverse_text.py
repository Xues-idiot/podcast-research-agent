"""反转文本工具"""

from typing import Optional


class ReverseText:
    _instance: Optional["ReverseText"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse(self, text: str) -> str:
        return text[::-1]

    def reverse_words(self, text: str) -> str:
        return " ".join(text.split()[::-1])

    def reverse_chars(self, text: str) -> str:
        return "".join(reversed(text))


def get_reverse_text() -> ReverseText:
    return ReverseText()
