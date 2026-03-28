"""Base64 URL安全编码工具"""

from typing import Optional
import base64


class Base64UrlTool:
    _instance: Optional["Base64UrlTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def encode(self, text: str) -> str:
        """URL安全Base64编码"""
        return base64.urlsafe_b64encode(text.encode()).decode()

    def decode(self, encoded: str) -> str:
        """Base64解码"""
        padding = 4 - len(encoded) % 4
        if padding != 4:
            encoded += "=" * padding
        return base64.urlsafe_b64decode(encoded.encode()).decode()

    def encode_json(self, data: dict) -> str:
        """JSON对象编码"""
        import json
        json_str = json.dumps(data)
        return self.encode(json_str)

    def decode_json(self, encoded: str) -> dict:
        """JSON对象解码"""
        import json
        json_str = self.decode(encoded)
        return json.loads(json_str)


_b64_instance: Optional[Base64UrlTool] = None


def get_base64_url_tool() -> Base64UrlTool:
    global _b64_instance
    if _b64_instance is None:
        _b64_instance = Base64UrlTool()
    return _b64_instance