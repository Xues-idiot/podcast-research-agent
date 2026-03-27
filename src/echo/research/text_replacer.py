"""文本替换工具"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ReplaceResult:
    """替换结果"""
    original_text: str
    result_text: str
    replacement_count: int


class TextReplacer:
    """文本替换工具"""

    def replace(self, text: str, old: str, new: str, count: int = -1) -> ReplaceResult:
        """替换文本"""
        if count == -1:
            result, replacement_count = text.replace(old, new), text.count(old)
        else:
            result, replacement_count = text.replace(old, new, count), min(count, text.count(old))

        return ReplaceResult(
            original_text=text,
            result_text=result,
            replacement_count=replacement_count
        )

    def replace_regex(self, text: str, pattern: str, replacement: str) -> ReplaceResult:
        """正则替换"""
        result = re.sub(pattern, replacement, text)
        matches = re.findall(pattern, text)
        return ReplaceResult(
            original_text=text,
            result_text=result,
            replacement_count=len(matches)
        )

    def replace_multiple(self, text: str, replacements: dict[str, str]) -> ReplaceResult:
        """多模式替换"""
        result = text
        total_count = 0
        for old, new in replacements.items():
            result, count = result.replace(old, new), result.count(old)
            total_count += count

        return ReplaceResult(
            original_text=text,
            result_text=result,
            replacement_count=total_count
        )


_replacer: Optional[TextReplacer] = None


def get_text_replacer() -> TextReplacer:
    global _replacer
    if _replacer is None:
        _replacer = TextReplacer()
    return _replacer