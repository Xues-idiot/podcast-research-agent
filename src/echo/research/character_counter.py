"""字符统计工具"""

from collections import Counter
from typing import Optional


class CharacterCounter:
    """字符统计工具"""

    def count_chars(self, text: str) -> dict:
        """统计字符"""
        return dict(Counter(text))

    def count_unique_chars(self, text: str) -> int:
        """统计唯一字符数"""
        return len(set(text))

    def most_common_chars(self, text: str, top_n: int = 10) -> list[tuple[str, int]]:
        """最常见字符"""
        return Counter(text).most_common(top_n)


_counter: Optional[CharacterCounter] = None


def get_character_counter() -> CharacterCounter:
    global _counter
    if _counter is None:
        _counter = CharacterCounter()
    return _counter