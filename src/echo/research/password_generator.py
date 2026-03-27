"""密码生成工具"""

import secrets
import string
from typing import Optional


class PasswordGenerator:
    """密码生成工具"""

    def generate(self, length: int = 16, include_special: bool = True) -> str:
        """生成密码"""
        chars = string.ascii_letters + string.digits
        if include_special:
            chars += string.punctuation
        return ''.join(secrets.choice(chars) for _ in range(length))

    def generate_strong(self, length: int = 16) -> str:
        """生成强密码"""
        while True:
            pwd = self.generate(length, True)
            if (any(c.islower() for c in pwd) and
                any(c.isupper() for c in pwd) and
                any(c.isdigit() for c in pwd) and
                any(c in string.punctuation for c in pwd)):
                return pwd


_generator: Optional[PasswordGenerator] = None


def get_password_generator() -> PasswordGenerator:
    global _generator
    if _generator is None:
        _generator = PasswordGenerator()
    return _generator