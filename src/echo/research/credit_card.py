"""信用卡工具"""

import re
from typing import Optional


class CreditCardTool:
    """信用卡工具"""

    def mask(self, card_number: str) -> str:
        """脱敏信用卡号"""
        digits = re.sub(r'\D', '', card_number)
        if len(digits) >= 16:
            return f"{digits[:4]} **** **** {digits[-4:]}"
        return card_number

    def validate_luhn(self, card_number: str) -> bool:
        """Luhn算法验证"""
        digits = re.sub(r'\D', '', card_number)
        if not digits:
            return False

        total = 0
        reverse_digits = digits[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0


_tool: Optional[CreditCardTool] = None


def get_credit_card_tool() -> CreditCardTool:
    global _tool
    if _tool is None:
        _tool = CreditCardTool()
    return _tool