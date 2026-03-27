"""编码转换工具"""

from typing import Optional


class EncodingTool:
    _instance: Optional["EncodingTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def encode(self, text: str, encoding: str = "utf-8") -> bytes:
        return text.encode(encoding)

    def decode(self, data: bytes, encoding: str = "utf-8") -> str:
        return data.decode(encoding)


def get_encoding_tool() -> EncodingTool:
    return EncodingTool()
