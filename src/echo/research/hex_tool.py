"""十六进制工具"""

from typing import Optional


class HexTool:
    _instance: Optional["HexTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_hex(self, data: bytes) -> str:
        return data.hex()

    def from_hex(self, hex_str: str) -> bytes:
        return bytes.fromhex(hex_str)


def get_hex_tool() -> HexTool:
    return HexTool()
