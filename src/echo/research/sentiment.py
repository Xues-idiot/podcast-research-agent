"""情感分析工具"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SentimentResult:
    """情感分析结果"""
    label: str
    score: float
    positive_score: float
    negative_score: float
    neutral_score: float


class SentimentAnalyzer:
    """简单情感分析"""

    POSITIVE_WORDS = {
        "好", "棒", "赞", "优秀", "精彩", "完美", "喜欢", "爱", "happy", "great",
        "awesome", "excellent", "amazing", "wonderful", "fantastic", "good",
        "best", "beautiful", "brilliant", "outstanding", "positive", "nice"
    }

    NEGATIVE_WORDS = {
        "差", "烂", "糟糕", "讨厌", "恨", "负面", "坏", "bad", "terrible",
        "awful", "horrible", "worst", "hate", "sad", "angry", "negative",
        "poor", "disappointing", "boring", "annoying", "wrong"
    }

    INTENSIFIERS = {"非常", "特别", "极其", "very", "really", "extremely", "absolutely"}

    def analyze(self, text: str) -> SentimentResult:
        """分析情感"""
        if not text:
            return SentimentResult(
                label="neutral",
                score=0.0,
                positive_score=0.0,
                negative_score=0.0,
                neutral_score=1.0
            )

        words = text.lower().split()
        pos_count = sum(1 for w in words if w in self.POSITIVE_WORDS)
        neg_count = sum(1 for w in words if w in self.NEGATIVE_WORDS)
        total = len(words) if words else 1

        # 计算强度修饰
        has_intensifier = any(w in self.INTENSIFIERS for w in words)
        multiplier = 1.5 if has_intensifier else 1.0

        pos_score = (pos_count * multiplier) / total
        neg_score = (neg_count * multiplier) / total
        neutral_score = 1.0 - pos_score - neg_score

        # 确定标签
        if pos_score > neg_score and pos_score > neutral_score:
            label = "positive"
        elif neg_score > pos_score and neg_score > neutral_score:
            label = "negative"
        else:
            label = "neutral"

        return SentimentResult(
            label=label,
            score=pos_score - neg_score,
            positive_score=round(pos_score, 3),
            negative_score=round(neg_score, 3),
            neutral_score=round(max(0, neutral_score), 3)
        )


_analyzer: Optional[SentimentAnalyzer] = None


def get_sentiment_analyzer() -> SentimentAnalyzer:
    global _analyzer
    if _analyzer is None:
        _analyzer = SentimentAnalyzer()
    return _analyzer