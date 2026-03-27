"""邮箱工具"""

import re
from typing import Optional


class EmailTool:
    _instance: Optional["EmailTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_valid(self, email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))


def get_email_tool() -> EmailTool:
    return EmailTool()
