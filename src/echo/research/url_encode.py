"""URL编码工具"""

from typing import Optional
from urllib.parse import quote, unquote


class UrlEncode:
    _instance: Optional["UrlEncode"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def encode(self, text: str, safe: str = "") -> str:
        return quote(text, safe=safe)

    def decode(self, text: str) -> str:
        return unquote(text)


def get_url_encode() -> UrlEncode:
    return UrlEncode()
