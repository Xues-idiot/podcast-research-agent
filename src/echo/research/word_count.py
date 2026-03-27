"""单词计数工具"""

from typing import Optional


class WordCount:
    _instance: Optional["WordCount"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def count(self, text: str) -> int:
        return len(text.split())

    def count_chars(self, text: str, include_spaces: bool = False) -> int:
        if include_spaces:
            return len(text)
        return len(text.replace(" ", ""))


def get_word_count() -> WordCount:
    return WordCount()
