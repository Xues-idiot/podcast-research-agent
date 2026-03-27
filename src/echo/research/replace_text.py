"""替换文本工具"""

from typing import Optional


class ReplaceText:
    _instance: Optional["ReplaceText"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def replace(self, text: str, old: str, new: str) -> str:
        return text.replace(old, new)

    def replace_all(self, text: str, old: str, new: str) -> str:
        return text.replace(old, new)

    def replace_between(self, text: str, start: str, end: str, new: str) -> str:
        idx_start = text.find(start)
        if idx_start == -1:
            return text
        idx_end = text.find(end, idx_start + len(start))
        if idx_end == -1:
            return text
        return text[:idx_start] + start + new + end + text[idx_end + len(end):]


def get_replace_text() -> ReplaceText:
    return ReplaceText()
