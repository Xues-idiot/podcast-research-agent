"""Slug生成工具"""

from typing import Optional
import re


class SlugMakerTool:
    _instance: Optional["SlugMakerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def make(self, text: str, max_length: int = 50) -> str:
        """生成slug"""
        slug = text.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        slug = slug.strip('-')
        if max_length > 0 and len(slug) > max_length:
            slug = slug[:max_length].rstrip('-')
        return slug

    def make_from_words(self, words: list, separator: str = "-") -> str:
        """从单词列表生成slug"""
        return separator.join(w.lower().strip() for w in words if w.strip())


_slug_instance: Optional[SlugMakerTool] = None


def get_slug_maker_tool() -> SlugMakerTool:
    global _slug_instance
    if _slug_instance is None:
        _slug_instance = SlugMakerTool()
    return _slug_instance