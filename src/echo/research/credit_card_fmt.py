"""信用卡格式化工具"""

from typing import Optional


class CreditCardFmtTool:
    _instance: Optional["CreditCardFmtTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def format(self, card_number: str) -> str:
        """格式化信用卡号"""
        digits = "".join(c for c in card_number if c.isdigit())
        groups = [digits[i:i+4] for i in range(0, len(digits), 4)]
        return " ".join(groups)

    def mask(self, card_number: str) -> str:
        """脱敏信用卡号"""
        digits = "".join(c for c in card_number if c.isdigit())
        if len(digits) < 4:
            return "*" * len(digits)
        return "*" * (len(digits) - 4) + digits[-4:]

    def get_type(self, card_number: str) -> str:
        """获取卡类型"""
        digits = "".join(c for c in card_number if c.isdigit())
        if not digits:
            return "unknown"
        if digits[0] == "4":
            return "Visa"
        if digits[:2] in ("51", "52", "53", "54", "55"):
            return "Mastercard"
        if digits[:2] in ("34", "37"):
            return "Amex"
        if digits[:4] == "6011" or digits[:2] == "65":
            return "Discover"
        return "unknown"

    def validate_luhn(self, card_number: str) -> bool:
        """Luhn算法验证"""
        digits = "".join(c for c in card_number if c.isdigit())
        if not digits:
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


_cc_instance: Optional[CreditCardFmtTool] = None


def get_credit_card_fmt_tool() -> CreditCardFmtTool:
    global _cc_instance
    if _cc_instance is None:
        _cc_instance = CreditCardFmtTool()
    return _cc_instance