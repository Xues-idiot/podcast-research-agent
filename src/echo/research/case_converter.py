"""大小写转换工具"""

from typing import Optional


class CaseConverter:
    """大小写转换工具"""

    def to_uppercase(self, text: str) -> str:
        """转为大写"""
        return text.upper()

    def to_lowercase(self, text: str) -> str:
        """转为小写"""
        return text.lower()

    def to_title_case(self, text: str) -> str:
        """转为标题格式"""
        return text.title()

    def to_sentence_case(self, text: str) -> str:
        """转为句子格式"""
        return text.capitalize()

    def to_camel_case(self, text: str) -> str:
        """转为驼峰格式"""
        words = self._split_words(text)
        if not words:
            return ""
        return words[0].lower() + "".join(w.capitalize() for w in words[1:])

    def to_pascal_case(self, text: str) -> str:
        """转为帕斯卡格式"""
        words = self._split_words(text)
        return "".join(w.capitalize() for w in words)

    def to_snake_case(self, text: str) -> str:
        """转为蛇形格式"""
        import re
        words = self._split_words(text)
        return "_".join(w.lower() for w in words)

    def to_kebab_case(self, text: str) -> str:
        """转为短横线格式"""
        words = self._split_words(text)
        return "-".join(w.lower() for w in words)

    def _split_words(self, text: str) -> list[str]:
        """分割单词"""
        import re
        words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', text)
        return [w for w in words if w]


_converter: Optional[CaseConverter] = None


def get_case_converter() -> CaseConverter:
    global _converter
    if _converter is None:
        _converter = CaseConverter()
    return _converter