"""键值对工具"""

from typing import Optional, Any


class KeyValueMaker:
    """键值对工具"""

    def make(self, key: str, value: Any) -> tuple:
        """创建键值对"""
        return (key, value)

    def to_dict(self, pairs: list) -> dict:
        """键值对列表转字典"""
        return dict(pairs)

    def from_dict(self, data: dict) -> list:
        """字典转键值对列表"""
        return list(data.items())


_maker: Optional[KeyValueMaker] = None


def get_key_value_maker() -> KeyValueMaker:
    global _maker
    if _maker is None:
        _maker = KeyValueMaker()
    return _maker