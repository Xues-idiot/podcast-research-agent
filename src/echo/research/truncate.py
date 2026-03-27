"""截断工具"""

from typing import Optional


class TruncateTool:
    _instance: Optional["TruncateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def truncate(self, text: str, length: int, suffix: str = "...") -> str:
        if len(text) <= length:
            return text
        return text[:length - len(suffix)] + suffix

    def truncate_words(self, text: str, word_count: int, suffix: str = "...") -> str:
        words = text.split()
        if len(words) <= word_count:
            return text
        return " ".join(words[:word_count]) + suffix


def get_truncate_tool() -> TruncateTool:
    return TruncateTool()
