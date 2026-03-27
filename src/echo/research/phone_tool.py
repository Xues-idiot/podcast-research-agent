"""电话号码工具"""

from typing import Optional
import re


class PhoneTool:
    _instance: Optional["PhoneTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_valid(self, phone: str) -> bool:
        pattern = r"^\+?1?\d{9,15}$"
        return bool(re.match(pattern, phone.replace("-", "").replace(" ", "")))

    def format(self, phone: str) -> str:
        digits = "".join(c for c in phone if c.isdigit())
        if len(digits) == 11 and digits[0] == "1":
            return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        return phone


def get_phone_tool() -> PhoneTool:
    return PhoneTool()
