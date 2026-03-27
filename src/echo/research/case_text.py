"""大小写转换工具"""

from typing import Optional


class CaseText:
    _instance: Optional["CaseText"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def upper(self, text: str) -> str:
        return text.upper()

    def lower(self, text: str) -> str:
        return text.lower()

    def swap(self, text: str) -> str:
        return text.swapcase()

    def camel(self, text: str) -> str:
        words = text.split()
        if not words:
            return text
        return words[0].lower() + "".join(w.capitalize() for w in words[1:])

    def snake(self, text: str) -> str:
        import re
        text = re.sub(r"([A-Z])", r"_\1", text)
        return text.lower().strip("_")


def get_case_text() -> CaseText:
    return CaseText()
