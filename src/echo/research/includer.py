"""包含检查工具"""

from typing import Optional


class Includer:
    """包含检查工具"""

    def contains(self, text: str, substring: str, case_sensitive: bool = True) -> bool:
        """是否包含子串"""
        if not case_sensitive:
            text = text.lower()
            substring = substring.lower()
        return substring in text

    def contains_any(self, text: str, substrings: list) -> bool:
        """是否包含任一子串"""
        return any(s in text for s in substrings)

    def contains_all(self, text: str, substrings: list) -> bool:
        """是否包含所有子串"""
        return all(s in text for s in substrings)


_includer: Optional[Includer] = None


def get_includer() -> Includer:
    global _includer
    if _includer is None:
        _includer = Includer()
    return _includer