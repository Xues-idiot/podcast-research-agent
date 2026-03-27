"""正则表达式工具"""

import re
from typing import Optional


class RegexHelper:
    """正则表达式工具"""

    def find_all_matches(self, text: str, pattern: str) -> list[str]:
        """查找所有匹配"""
        try:
            return re.findall(pattern, text)
        except re.error:
            return []

    def find_with_context(self, text: str, pattern: str, context_chars: int = 50) -> list[dict]:
        """带上下文查找"""
        try:
            compiled = re.compile(pattern)
            results = []
            for match in compiled.finditer(text):
                start = max(0, match.start() - context_chars)
                end = min(len(text), match.end() + context_chars)
                results.append({
                    "match": match.group(),
                    "position": match.start(),
                    "context": text[start:end]
                })
            return results
        except re.error:
            return []

    def split_by_pattern(self, text: str, pattern: str) -> list[str]:
        """按模式分割"""
        try:
            return re.split(pattern, text)
        except re.error:
            return [text]


_helper: Optional[RegexHelper] = None


def get_regex_helper() -> RegexHelper:
    global _helper
    if _helper is None:
        _helper = RegexHelper()
    return _helper