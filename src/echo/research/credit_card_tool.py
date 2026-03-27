"""信用卡工具"""

from typing import Optional
import re


class CreditCardTool:
    _instance: Optional["CreditCardTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_valid(self, card: str) -> bool:
        digits = "".join(c for c in card if c.isdigit())
        if len(digits) < 13 or len(digits) > 19:
            return False
        total = 0
        reverse_digits = digits[::-1]
        for i, d in enumerate(reverse_digits):
            n = int(d)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0


def get_credit_card_tool() -> CreditCardTool:
    return CreditCardTool()
