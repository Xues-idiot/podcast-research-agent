"""去除空白工具"""

from typing import Optional


class StripText:
    _instance: Optional["StripText"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def strip(self, text: str) -> str:
        return text.strip()

    def strip_left(self, text: str) -> str:
        return text.lstrip()

    def strip_right(self, text: str) -> str:
        return text.rstrip()

    def normalize(self, text: str) -> str:
        return " ".join(text.split())


def get_strip_text() -> StripText:
    return StripText()
