"""前缀后缀工具"""

from typing import Optional


class PrefixSuffixTool:
    _instance: Optional["PrefixSuffixTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_prefix(self, text: str, prefix: str) -> str:
        return prefix + text

    def add_suffix(self, text: str, suffix: str) -> str:
        return text + suffix

    def remove_prefix(self, text: str, prefix: str) -> str:
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def remove_suffix(self, text: str, suffix: str) -> str:
        if text.endswith(suffix):
            return text[:-len(suffix)]
        return text


def get_prefix_suffix_tool() -> PrefixSuffixTool:
    return PrefixSuffixTool()