"""正则表达式引擎工具"""

from typing import Any, Optional, Pattern
import re


class RegexEngine:
    _instance: Optional["RegexEngine"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def match(self, pattern: str, text: str) -> bool:
        return bool(re.match(pattern, text))

    def search(self, pattern: str, text: str) -> Optional[str]:
        match = re.search(pattern, text)
        return match.group() if match else None

    def find_all(self, pattern: str, text: str) -> List[str]:
        return re.findall(pattern, text)

    def replace(self, pattern: str, text: str, replacement: str) -> str:
        return re.sub(pattern, replacement, text)


def get_regex_engine() -> RegexEngine:
    return RegexEngine()
