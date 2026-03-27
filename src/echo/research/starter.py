"""前缀后缀工具"""

from typing import Optional


class PrefixSuffix:
    """前缀后缀工具"""

    def has_prefix(self, text: str, prefix: str) -> bool:
        """是否有前缀"""
        return text.startswith(prefix)

    def has_suffix(self, text: str, suffix: str) -> bool:
        """是否有后缀"""
        return text.endswith(suffix)

    def add_prefix(self, text: str, prefix: str) -> str:
        """添加前缀"""
        return prefix + text

    def add_suffix(self, text: str, suffix: str) -> str:
        """添加后缀"""
        return text + suffix

    def remove_prefix(self, text: str, prefix: str) -> str:
        """移除前缀"""
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def remove_suffix(self, text: str, suffix: str) -> str:
        """移除后缀"""
        if text.endswith(suffix):
            return text[:-len(suffix)]
        return text


_ps: Optional[PrefixSuffix] = None


def get_prefix_suffix() -> PrefixSuffix:
    global _ps
    if _ps is None:
        _ps = PrefixSuffix()
    return _ps