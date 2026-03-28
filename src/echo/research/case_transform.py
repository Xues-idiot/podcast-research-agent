"""大小写转换工具"""

import re
from typing import Optional


class CaseTransformTool:
    _instance: Optional["CaseTransformTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_camel_case(self, text: str) -> str:
        words = re.sub(r'[^\w]', ' ', text).split()
        return words[0].lower() + ''.join(w.capitalize() for w in words[1:]) if words else text

    def to_snake_case(self, text: str) -> str:
        text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', text)
        text = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', text)
        return text.lower()

    def to_pascal_case(self, text: str) -> str:
        words = re.sub(r'[^\w]', ' ', text).split()
        return ''.join(w.capitalize() for w in words) if words else text


def get_case_transform_tool() -> CaseTransformTool:
    return CaseTransformTool()