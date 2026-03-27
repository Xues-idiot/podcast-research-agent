"""数据脱敏工具"""

import re
from typing import Optional


class DataSanitizer:
    """数据脱敏工具"""

    def mask_email(self, email: str) -> str:
        """邮箱脱敏"""
        parts = email.split('@')
        if len(parts[0]) > 2:
            return parts[0][0] + '*' * (len(parts[0]) - 2) + parts[0][-1] + '@' + parts[1]
        return email

    def mask_phone(self, phone: str) -> str:
        """手机号脱敏"""
        digits = re.sub(r'\D', '', phone)
        if len(digits) >= 7:
            return digits[:3] + '****' + digits[-4:]
        return phone

    def mask_id_card(self, id_card: str) -> str:
        """身份证号脱敏"""
        if len(id_card) >= 10:
            return id_card[:4] + '*' * (len(id_card) - 8) + id_card[-4:]
        return id_card


_sanitizer: Optional[DataSanitizer] = None


def get_data_sanitizer() -> DataSanitizer:
    global _sanitizer
    if _sanitizer is None:
        _sanitizer = DataSanitizer()
    return _sanitizer