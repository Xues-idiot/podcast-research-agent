"""HTML编码工具"""

from typing import Optional
from html import escape, unescape


class HtmlEncode:
    _instance: Optional["HtmlEncode"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def encode(self, text: str) -> str:
        return escape(text)

    def decode(self, text: str) -> str:
        return unescape(text)


def get_html_encode() -> HtmlEncode:
    return HtmlEncode()
