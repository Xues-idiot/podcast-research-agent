"""分割文本工具"""

from typing import List, Optional


class SplitText:
    _instance: Optional["SplitText"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def split(self, text: str, delimiter: str = " ") -> List[str]:
        return text.split(delimiter)

    def split_lines(self, text: str) -> List[str]:
        return text.split("\n")

    def split_words(self, text: str) -> List[str]:
        return text.split()


def get_split_text() -> SplitText:
    return SplitText()
