"""验证工具"""

import re
from typing import Optional


class ValidatorUtils:
    """常用验证工具"""

    def is_email(self, value: str) -> bool:
        """验证邮箱"""
        return bool(re.match(r'[\w.-]+@[\w.-]+\.\w+', value))

    def is_url(self, value: str) -> bool:
        """验证URL"""
        return bool(re.match(r'https?://\S+', value))

    def is_phone(self, value: str) -> bool:
        """验证手机号"""
        return bool(re.match(r'1[3-9]\d{9}', value))

    def is_id_card(self, value: str) -> bool:
        """验证身份证号"""
        return bool(re.match(r'\d{17}[\dXx]', value))

    def is_postal_code(self, value: str) -> bool:
        """验证邮政编码"""
        return bool(re.match(r'\d{6}', value))


_validator: Optional[ValidatorUtils] = None


def get_validator_utils() -> ValidatorUtils:
    global _validator
    if _validator is None:
        _validator = ValidatorUtils()
    return _validator