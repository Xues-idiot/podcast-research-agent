"""首字母大写工具"""

from typing import Optional


class Capitalizer:
    _instance: Optional["Capitalizer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def capitalize(self, text: str) -> str:
        return text.capitalize()

    def title_case(self, text: str) -> str:
        return text.title()

    def upper_first(self, text: str) -> str:
        if not text:
            return text
        return text[0].upper() + text[1:]


def get_capitalizer() -> Capitalizer:
    return Capitalizer()
