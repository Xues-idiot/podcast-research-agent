"""文本合并工具"""

from typing import Optional


class TextMerger:
    """文本合并工具"""

    def merge_consecutive(self, texts: list[str], separator: str = " ") -> str:
        """合并连续文本"""
        if not texts:
            return ""
        return separator.join(t for t in texts if t)

    def merge_with_overlap(self, texts: list[str], overlap_chars: int = 100) -> str:
        """带重叠的合并"""
        if not texts:
            return ""
        if len(texts) == 1:
            return texts[0]

        result = texts[0]
        for text in texts[1:]:
            if overlap_chars > 0 and len(result) > overlap_chars:
                # 从result末尾取overlap_chars与text开头合并
                result = result[:-overlap_chars] + text
            else:
                result += text

        return result

    def merge_by_theme(self, texts: list[str], similarity_threshold: float = 0.5) -> list[str]:
        """按主题合并"""
        if not texts:
            return []
        if len(texts) == 1:
            return texts

        merged = [texts[0]]
        for text in texts[1:]:
            if self._similarity(merged[-1], text) > similarity_threshold:
                merged[-1] = merged[-1] + "\n\n" + text
            else:
                merged.append(text)

        return merged

    def _similarity(self, s1: str, s2: str) -> float:
        """简单相似度计算"""
        if not s1 or not s2:
            return 0.0
        set1 = set(s1.lower())
        set2 = set(s2.lower())
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return intersection / union if union > 0 else 0.0


_merger: Optional[TextMerger] = None


def get_text_merger() -> TextMerger:
    global _merger
    if _merger is None:
        _merger = TextMerger()
    return _merger