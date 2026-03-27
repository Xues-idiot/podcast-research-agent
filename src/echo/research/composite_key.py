"""组合键工具"""

from typing import List, Any, Tuple, Optional


class CompositeKey:
    _instance: Optional["CompositeKey"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def make_key(self, *parts: Any) -> str:
        return ":".join(str(p) for p in parts)

    def parse_key(self, key: str) -> List[str]:
        return key.split(":")


def get_composite_key() -> CompositeKey:
    return CompositeKey()
