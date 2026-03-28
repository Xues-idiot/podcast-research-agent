"""空白字符处理工具"""

import re
from typing import Optional


class WhitespaceTool:
    _instance: Optional["WhitespaceTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def remove_extra_spaces(self, text: str) -> str:
        return re.sub(r'\s+', ' ', text).strip()

    def normalize_spaces(self, text: str) -> str:
        return re.sub(r'[ \t]+', ' ', text)

    def remove_all_spaces(self, text: str) -> str:
        return re.sub(r'\s+', '', text)

    def split_lines(self, text: str) -> list:
        return [line.strip() for line in text.split('\n') if line.strip()]


def get_whitespace_tool() -> WhitespaceTool:
    return WhitespaceTool()