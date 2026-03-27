"""文本编码转换工具"""

from typing import Optional


class TextEncoder:
    """文本编码转换工具"""

    def to_base64(self, text: str) -> str:
        """转为Base64"""
        import base64
        return base64.b64encode(text.encode('utf-8')).decode('ascii')

    def from_base64(self, encoded: str) -> str:
        """从Base64解码"""
        import base64
        return base64.b64decode(encoded.encode('ascii')).decode('utf-8')

    def to_hex(self, text: str) -> str:
        """转为十六进制"""
        return text.encode('utf-8').hex()

    def from_hex(self, hex_str: str) -> str:
        """从十六进制解码"""
        return bytes.fromhex(hex_str).decode('utf-8')

    def to_url_encode(self, text: str) -> str:
        """URL编码"""
        import urllib.parse
        return urllib.parse.quote(text)

    def from_url_encode(self, encoded: str) -> str:
        """URL解码"""
        import urllib.parse
        return urllib.parse.unquote(encoded)


_encoder: Optional[TextEncoder] = None


def get_text_encoder() -> TextEncoder:
    global _encoder
    if _encoder is None:
        _encoder = TextEncoder()
    return _encoder