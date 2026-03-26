"""文本分割器"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SplitResult:
    """分割结果"""
    parts: list[str]
    part_count: int


class TextSplitter:
    """文本分割工具"""

    def split_by_chars(self, text: str, chunk_size: int = 1000, overlap: int = 100) -> SplitResult:
        """按字符数分割"""
        if not text or chunk_size <= 0:
            return SplitResult(parts=[], part_count=0)

        parts = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = min(start + chunk_size, text_len)
            parts.append(text[start:end])
            start = end - overlap if end < text_len else text_len

        return SplitResult(parts=parts, part_count=len(parts))

    def split_by_sentences(self, text: str, sentences_per_chunk: int = 5) -> SplitResult:
        """按句子数分割"""
        import re
        if not text:
            return SplitResult(parts=[], part_count=0)

        # 简单句子分割
        sentence_endings = r'[。！？.!?]+'
        sentences = re.split(sentence_endings, text)
        sentences = [s.strip() for s in sentences if s.strip()]

        parts = []
        for i in range(0, len(sentences), sentences_per_chunk):
            chunk = ''.join(sentences[i:i + sentences_per_chunk])
            parts.append(chunk)

        return SplitResult(parts=parts, part_count=len(parts))

    def split_by_paragraphs(self, text: str, paragraphs_per_chunk: int = 3) -> SplitResult:
        """按段落数分割"""
        if not text:
            return SplitResult(parts=[], part_count=0)

        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        parts = []
        for i in range(0, len(paragraphs), paragraphs_per_chunk):
            chunk = '\n\n'.join(paragraphs[i:i + paragraphs_per_chunk])
            parts.append(chunk)

        return SplitResult(parts=parts, part_count=len(parts))


_splitter: Optional[TextSplitter] = None


def get_text_splitter() -> TextSplitter:
    global _splitter
    if _splitter is None:
        _splitter = TextSplitter()
    return _splitter