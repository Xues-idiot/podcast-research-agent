"""ID生成工具"""

import uuid
import secrets
import string
from typing import Optional


class IdGenerator:
    """ID生成工具"""

    def uuid4(self) -> str:
        """生成UUID4"""
        return str(uuid.uuid4())

    def short_id(self, length: int = 12) -> str:
        """生成短ID"""
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def numeric_id(self, length: int = 8) -> str:
        """生成数字ID"""
        return ''.join(secrets.choice(string.digits) for _ in range(length))

    def hash_id(self, text: str) -> str:
        """基于文本生成哈希ID"""
        import hashlib
        return hashlib.md5(text.encode()).hexdigest()[:12]


_generator: Optional[IdGenerator] = None


def get_id_generator() -> IdGenerator:
    global _generator
    if _generator is None:
        _generator = IdGenerator()
    return _generator