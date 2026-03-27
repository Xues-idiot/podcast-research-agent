"""单词提取工具"""

import re
from collections import Counter
from typing import Optional


class WordExtractor:
    """单词提取工具"""

    def extract_words(self, text: str, min_length: int = 2) -> list[str]:
        """提取单词"""
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        return [w for w in words if len(w) >= min_length]

    def extract_chinese_words(self, text: str, min_length: int = 2) -> list[str]:
        """提取中文词"""
        words = re.findall(r'[\u4e00-\u9fff]+', text)
        return [w for w in words if len(w) >= min_length]

    def extract_ngrams(self, text: str, n: int = 2) -> list[str]:
        """提取N元语法"""
        words = self.extract_words(text)
        if len(words) < n:
            return []
        return [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]

    def word_frequency(self, text: str, top_n: int = 20) -> list[dict]:
        """词频统计"""
        words = self.extract_words(text)
        counter = Counter(words)
        total = len(words) if words else 1
        return [
            {"word": w, "count": c, "frequency": round(c/total, 4)}
            for w, c in counter.most_common(top_n)
        ]


_extractor: Optional[WordExtractor] = None


def get_word_extractor() -> WordExtractor:
    global _extractor
    if _extractor is None:
        _extractor = WordExtractor()
    return _extractor