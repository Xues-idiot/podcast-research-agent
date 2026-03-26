"""关键词提取工具"""

import re
from collections import Counter
from typing import Optional


class KeywordExtractor:
    """提取关键词"""

    STOP_WORDS = {
        "的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一",
        "一个", "上", "也", "很", "到", "说", "要", "去", "你", "会", "着", "没有",
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "must", "shall", "can", "need", "this",
        "that", "these", "those", "in", "on", "at", "by", "for", "with"
    }

    def extract(self, text: str, top_n: int = 10) -> list[dict]:
        """提取关键词"""
        if not text:
            return []

        # 清理文本
        text = re.sub(r'[^\w\s]', ' ', text)
        words = text.split()

        # 过滤
        filtered = [
            w for w in words
            if len(w) >= 2
            and w.lower() not in self.STOP_WORDS
            and not w.isdigit()
        ]

        # 词频统计
        counter = Counter(filtered)
        total = sum(counter.values()) if counter else 1

        # 计算TF-IDF近似值
        results = []
        for word, count in counter.most_common(top_n * 2):
            tf = count / total
            idf = 1.0  # 简化版
            score = tf * idf
            results.append({
                "keyword": word,
                "score": round(score, 4),
                "count": count
            })

        return results[:top_n]

    def extract_phrases(self, text: str, top_n: int = 5) -> list[dict]:
        """提取短语"""
        if not text:
            return []

        # 提取2-3词的短语
        words = text.split()
        phrases = []

        for n in [2, 3]:
            for i in range(len(words) - n + 1):
                phrase = "".join(words[i:i+n])
                if all(w.lower() not in self.STOP_WORDS for w in words[i:i+n]):
                    phrases.append(phrase)

        counter = Counter(phrases)
        total = sum(counter.values()) if counter else 1

        return [
            {"phrase": phrase, "score": round(count/total, 4), "count": count}
            for phrase, count in counter.most_common(top_n)
        ]


_extractor: Optional[KeywordExtractor] = None


def get_keyword_extractor() -> KeywordExtractor:
    global _extractor
    if _extractor is None:
        _extractor = KeywordExtractor()
    return _extractor