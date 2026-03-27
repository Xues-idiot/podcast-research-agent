"""句子分割工具"""

import re
from typing import Optional


class SentenceSplitter:
    """句子分割工具"""

    def split_chinese(self, text: str) -> list[str]:
        """中文分句"""
        sentences = re.split(r'[。！？]+', text)
        return [s.strip() for s in sentences if s.strip()]

    def split_english(self, text: str) -> list[str]:
        """英文分句"""
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]

    def split_mixed(self, text: str) -> list[str]:
        """混合分句"""
        sentences = re.split(r'[。！？.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]

    def split_by_length(self, text: str, max_length: int = 200) -> list[str]:
        """按长度分句"""
        sentences = self.split_mixed(text)
        result = []
        for sent in sentences:
            if len(sent) <= max_length:
                result.append(sent)
            else:
                words = sent.split()
                current = []
                current_len = 0
                for word in words:
                    if current_len + len(word) > max_length and current:
                        result.append(' '.join(current))
                        current = [word]
                        current_len = len(word)
                    else:
                        current.append(word)
                        current_len += len(word) + 1
                if current:
                    result.append(' '.join(current))
        return result


_splitter: Optional[SentenceSplitter] = None


def get_sentence_splitter() -> SentenceSplitter:
    global _splitter
    if _splitter is None:
        _splitter = SentenceSplitter()
    return _splitter