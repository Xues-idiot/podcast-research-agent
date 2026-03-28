"""NanoID生成工具"""

from typing import Optional
import random
import string


class NanoidGenTool:
    _instance: Optional["NanoidGenTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate(self, size: int = 21, alphabet: str = None) -> str:
        """生成NanoID"""
        if alphabet is None:
            alphabet = string.ascii_letters + string.digits + "-_"
        return "".join(random.choice(alphabet) for _ in range(size))

    def generate_multiple(self, count: int, size: int = 21) -> list:
        """批量生成"""
        return [self.generate(size) for _ in range(count)]


_nanoid_instance: Optional[NanoidGenTool] = None


def get_nanoid_gen_tool() -> NanoidGenTool:
    global _nanoid_instance
    if _nanoid_instance is None:
        _nanoid_instance = NanoidGenTool()
    return _nanoid_instance