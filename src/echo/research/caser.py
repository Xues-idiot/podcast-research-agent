"""大小写转换工具"""

from typing import Optional


class Caser:
    """大小写转换工具"""

    def to_snake_case(self, text: str) -> str:
        """转蛇形"""
        import re
        s = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
        return s

    def to_camel_case(self, text: str) -> str:
        """转驼峰"""
        parts = text.split('_')
        return parts[0] + ''.join(p.capitalize() for p in parts[1:])

    def to_pascal_case(self, text: str) -> str:
        """转帕斯卡"""
        parts = text.split('_')
        return ''.join(p.capitalize() for p in parts)

    def to_const_case(self, text: str) -> str:
        """转常量格式"""
        return text.upper().replace('-', '_')


_caser: Optional[Caser] = None


def get_caser() -> Caser:
    global _caser
    if _caser is None:
        _caser = Caser()
    return _caser