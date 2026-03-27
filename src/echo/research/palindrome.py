"""回文工具"""

from typing import Optional


class Palindrome:
    _instance: Optional["Palindrome"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_palindrome(self, s: str) -> bool:
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    def longest_palindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self._expand_around_center(s, i, i)
            len2 = self._expand_around_center(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


def get_palindrome() -> Palindrome:
    return Palindrome()
