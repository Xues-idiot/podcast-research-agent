"""文本截断工具"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TruncationResult:
    """截断结果"""
    original_text: str
    truncated_text: str
    original_length: int
    truncated_length: int
    was_truncated: bool


class TextTruncator:
    """文本截断工具"""

    def truncate(self, text: str, max_length: int, suffix: str = "...") -> TruncationResult:
        """截断文本"""
        original_length = len(text)
        if max_length >= original_length or max_length <= 0:
            return TruncationResult(
                original_text=text,
                truncated_text=text,
                original_length=original_length,
                truncated_length=original_length,
                was_truncated=False
            )

        # 确保suffix不会超出max_length
        effective_max = max_length - len(suffix)
        if effective_max <= 0:
            effective_max = max_length

        truncated = text[:effective_max] + suffix
        return TruncationResult(
            original_text=text,
            truncated_text=truncated,
            original_length=original_length,
            truncated_length=len(truncated),
            was_truncated=True
        )

    def truncate_by_words(self, text: str, max_words: int, suffix: str = "...") -> TruncationResult:
        """按单词数截断"""
        words = text.split()
        original_length = len(text)
        if max_words >= len(words) or max_words <= 0:
            return TruncationResult(
                original_text=text,
                truncated_text=text,
                original_length=original_length,
                truncated_length=original_length,
                was_truncated=False
            )

        truncated = " ".join(words[:max_words]) + suffix
        return TruncationResult(
            original_text=text,
            truncated_text=truncated,
            original_length=original_length,
            truncated_length=len(truncated),
            was_truncated=True
        )

    def truncate_sentences(self, text: str, max_sentences: int, suffix: str = "...") -> TruncationResult:
        """按完整句子截断"""
        import re
        original_length = len(text)
        # 分割句子
        sentences = re.split(r'[。！？.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if max_sentences >= len(sentences) or max_sentences <= 0:
            return TruncationResult(
                original_text=text,
                truncated_text=text,
                original_length=original_length,
                truncated_length=original_length,
                was_truncated=False
            )

        truncated = "".join(sentences[:max_sentences]) + suffix
        return TruncationResult(
            original_text=text,
            truncated_text=truncated,
            original_length=original_length,
            truncated_length=len(truncated),
            was_truncated=True
        )


_truncator: Optional[TextTruncator] = None


def get_text_truncator() -> TextTruncator:
    global _truncator
    if _truncator is None:
        _truncator = TextTruncator()
    return _truncator