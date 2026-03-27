"""组合键工具"""

from typing import Optional, Any


class KeyBuilder:
    """组合键工具"""

    def build(self, *parts: Any, separator: str = ":") -> str:
        """构建键"""
        return separator.join(str(p) for p in parts)

    def parse(self, key: str, separator: str = ":") -> list:
        """解析键"""
        return key.split(separator)


_builder: Optional[KeyBuilder] = None


def get_key_builder() -> KeyBuilder:
    global _builder
    if _builder is None:
        _builder = KeyBuilder()
    return _builder