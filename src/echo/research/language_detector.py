"""语言检测工具"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class LanguageResult:
    """语言检测结果"""
    language: str
    confidence: float
    script: str


class LanguageDetector:
    """语言检测工具"""

    def detect(self, text: str) -> LanguageResult:
        """检测语言"""
        if not text:
            return LanguageResult(language="unknown", confidence=0.0, script="unknown")

        chinese_count = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        japanese_count = sum(1 for c in text if '\u3040' <= c <= '\u309f' or '\u30a0' <= c <= '\u30ff')
        korean_count = sum(1 for c in text if '\uac00' <= c <= '\ud7af')
        total = len(text)

        if total == 0:
            return LanguageResult(language="unknown", confidence=0.0, script="unknown")

        chinese_ratio = chinese_count / total
        japanese_ratio = japanese_count / total
        korean_ratio = korean_count / total

        if chinese_ratio > 0.3:
            return LanguageResult(language="chinese", confidence=min(1.0, chinese_ratio + 0.3), script="cjk")
        elif japanese_ratio > 0.2:
            return LanguageResult(language="japanese", confidence=min(1.0, japanese_ratio + 0.3), script="cjk")
        elif korean_ratio > 0.2:
            return LanguageResult(language="korean", confidence=min(1.0, korean_ratio + 0.3), script="cjk")

        # 检测英文
        ascii_count = sum(1 for c in text if c.isascii() and c.isalpha())
        ascii_ratio = ascii_count / total

        if ascii_ratio > 0.5:
            return LanguageResult(language="english", confidence=min(1.0, ascii_ratio), script="latin")

        return LanguageResult(language="mixed", confidence=0.5, script="mixed")


_detector: Optional[LanguageDetector] = None


def get_language_detector() -> LanguageDetector:
    global _detector
    if _detector is None:
        _detector = LanguageDetector()
    return _detector