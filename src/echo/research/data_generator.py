"""数据生成工具"""

import random
import string
from typing import Optional


class DataGenerator:
    """数据生成工具"""

    def random_string(self, length: int = 10, chars: str = None) -> str:
        """生成随机字符串"""
        if chars is None:
            chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def random_digits(self, length: int = 6) -> str:
        """生成随机数字"""
        return ''.join(random.choice(string.digits) for _ in range(length))

    def random_letters(self, length: int = 10) -> str:
        """生成随机字母"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def random_hex(self, length: int = 8) -> str:
        """生成随机十六进制"""
        return ''.join(random.choice('0123456789abcdef') for _ in range(length))


_generator: Optional[DataGenerator] = None


def get_data_generator() -> DataGenerator:
    global _generator
    if _generator is None:
        _generator = DataGenerator()
    return _generator