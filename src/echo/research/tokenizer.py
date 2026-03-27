"""分词工具"""

import jieba
from typing import Optional


class Tokenizer:
    """中文分词工具"""

    def tokenize(self, text: str) -> list[str]:
        """分词"""
        return list(jieba.cut(text))

    def tokenize_for_search(self, text: str) -> list[str]:
        """搜索引擎分词"""
        return list(jieba.cut_for_search(text))

    def extract_keywords(self, text: str, top_n: int = 20) -> list[str]:
        """提取关键词"""
        import jieba.analyse
        return jieba.analyse.extract_tags(text, topK=top_n)


_tokenizer: Optional[Tokenizer] = None


def get_tokenizer() -> Tokenizer:
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = Tokenizer()
    return _tokenizer