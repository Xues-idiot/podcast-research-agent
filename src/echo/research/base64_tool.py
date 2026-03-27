"""Base64工具"""

import base64 as b64
from typing import Optional


class Base64Tool:
    """Base64工具"""

    def encode(self, data: str) -> str:
        """Base64编码"""
        return b64.b64encode(data.encode('utf-8')).decode('ascii')

    def decode(self, encoded: str) -> str:
        """Base64解码"""
        return b64.b64decode(encoded.encode('ascii')).decode('utf-8')

    def encode_url(self, data: str) -> str:
        """URL安全的Base64编码"""
        return b64.urlsafe_b64encode(data.encode('utf-8')).decode('ascii').rstrip('=')

    def decode_url(self, encoded: str) -> str:
        """URL安全的Base64解码"""
        padding = 4 - len(encoded) % 4
        encoded += '=' * padding
        return b64.urlsafe_b64decode(encoded.encode('ascii')).decode('utf-8')


_tool: Optional[Base64Tool] = None


def get_base64_tool() -> Base64Tool:
    global _tool
    if _tool is None:
        _tool = Base64Tool()
    return _tool