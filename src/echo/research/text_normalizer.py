"""文本标准化工具"""

import re
from typing import Optional


class TextNormalizer:
    """文本标准化工具"""

    def normalize_whitespace(self, text: str) -> str:
        """标准化空白字符"""
        text = re.sub(r'[\t\v\f]', ' ', text)
        text = re.sub(r' +', ' ', text)
        return text

    def normalize_newlines(self, text: str, max_consecutive: int = 2) -> str:
        """标准化换行符"""
        text = re.sub(r'\r\n', '\n', text)
        text = re.sub(r'\r', '\n', text)
        text = re.sub(r'\n{' + str(max_consecutive + 1) + r',}', '\n' * max_consecutive, text)
        return text.strip()

    def normalize_quotes(self, text: str) -> str:
        """标准化引号"""
        replacements = {
            '"': '"', '"': '"',
            ''': "'", ''': "'",
            '«': '"', '»': '"',
            '`': "'", '´': "'",
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    def normalize_dashes(self, text: str) -> str:
        """标准化破折号"""
        text = re.sub(r'[\u2014\u2013\u2012\u2010\u2011\u2012]', '-', text)
        text = re.sub(r'-{3,}', '---', text)
        return text

    def normalize_unicode(self, text: str) -> str:
        """标准化Unicode"""
        import unicodedata
        return unicodedata.normalize('NFKC', text)

    def full_normalize(self, text: str) -> str:
        """完整标准化"""
        text = self.normalize_unicode(text)
        text = self.normalize_whitespace(text)
        text = self.normalize_newlines(text)
        text = self.normalize_quotes(text)
        text = self.normalize_dashes(text)
        return text


_normalizer: Optional[TextNormalizer] = None


def get_text_normalizer() -> TextNormalizer:
    global _normalizer
    if _normalizer is None:
        _normalizer = TextNormalizer()
    return _normalizer