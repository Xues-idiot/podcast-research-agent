"""内容去重工具"""

from typing import Optional


class ContentDeduplicator:
    """去除重复内容"""

    def deduplicate_lines(self, lines: list[str], threshold: float = 0.85) -> list[str]:
        """去除重复行"""
        if not lines:
            return []

        unique_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            is_duplicate = False
            for unique in unique_lines:
                if self._similarity(line, unique) > threshold:
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_lines.append(line)

        return unique_lines

    def deduplicate_chunks(self, chunks: list[str], threshold: float = 0.8) -> list[str]:
        """去除重复块"""
        if not chunks:
            return []

        unique_chunks = []
        for chunk in chunks:
            is_duplicate = False
            for unique in unique_chunks:
                if self._similarity(chunk, unique) > threshold:
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_chunks.append(chunk)

        return unique_chunks

    def _similarity(self, s1: str, s2: str) -> float:
        """计算字符串相似度"""
        if not s1 or not s2:
            return 0.0

        # 简单的字符级Jaccard相似度
        set1 = set(s1.lower())
        set2 = set(s2.lower())
        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return intersection / union if union > 0 else 0.0


_deduplicator: Optional[ContentDeduplicator] = None


def get_deduplicator() -> ContentDeduplicator:
    global _deduplicator
    if _deduplicator is None:
        _deduplicator = ContentDeduplicator()
    return _deduplicator