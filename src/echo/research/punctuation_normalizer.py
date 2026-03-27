"""标点符号工具"""

import re
from typing import Optional


class PunctuationNormalizer:
    """标点符号工具"""

    def normalize(self, text: str) -> str:
        """规范化标点"""
        text = re.sub(r'[,,]', ',', text)
        text = re.sub(r'[;;]', ';', text)
        text = re.sub(r'[:]', ':', text)
        text = re.sub(r'['']', "'", text)
        text = re.sub(r'[""]', '"', text)
        text = re.sub(r'[\s]+([.,;:!?])', r'\1', text)
        text = re.sub(r'([.,;:!?])([^\s])', r'\1 \2', text)
        return text

    def add_spaces(self, text: str) -> str:
        """在标点后添加空格"""
        return re.sub(r'([.,;:!?])([^\s])', r'\1 \2', text)

    def remove_spaces(self, text: str) -> str:
        """移除标点前的空格"""
        return re.sub(r'\s+([.,;:!?])', r'\1', text)


_normalizer: Optional[PunctuationNormalizer] = None


def get_punctuation_normalizer() -> PunctuationNormalizer:
    global _normalizer
    if _normalizer is None:
        _normalizer = PunctuationNormalizer()
    return _normalizer