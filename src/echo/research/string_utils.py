"""字符串工具"""

from typing import Optional


class StringUtils:
    """字符串工具"""

    def reverse(self, text: str) -> str:
        """反转字符串"""
        return text[::-1]

    def is_palindrome(self, text: str) -> bool:
        """是否回文"""
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

    def count_vowels(self, text: str) -> int:
        """统计元音字母"""
        vowels = set('aeiouAEIOU')
        return sum(1 for c in text if c in vowels)

    def count_consonants(self, text: str) -> int:
        """统计辅音字母"""
        consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
        return sum(1 for c in text if c in consonants)

    def capitalize_words(self, text: str) -> str:
        """首字母大写"""
        return ' '.join(w.capitalize() for w in text.split())


_utils: Optional[StringUtils] = None


def get_string_utils() -> StringUtils:
    global _utils
    if _utils is None:
        _utils = StringUtils()
    return _utils