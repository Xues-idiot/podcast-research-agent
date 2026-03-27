"""电话号码工具"""

import re
from typing import Optional


class PhoneFormatter:
    """电话号码工具"""

    def format_cn(self, phone: str) -> str:
        """格式化中国手机号"""
        digits = re.sub(r'\D', '', phone)
        if len(digits) == 11:
            return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
        return phone

    def validate_cn_mobile(self, phone: str) -> bool:
        """验证中国手机号"""
        digits = re.sub(r'\D', '', phone)
        return bool(re.match(r'^1[3-9]\d{9}$', digits))


_formatter: Optional[PhoneFormatter] = None


def get_phone_formatter() -> PhoneFormatter:
    global _formatter
    if _formatter is None:
        _formatter = PhoneFormatter()
    return _formatter