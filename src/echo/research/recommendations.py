"""播客推荐系统 - 基于研究历史推荐相关内容"""

from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Recommendation:
    """推荐内容"""
    source: str
    title: str
    reason: str
    score: float
    platform: str = ""


class PodcastRecommender:
    """播客推荐器"""

    def __init__(self):
        """初始化推荐器"""
        self._user_preferences = {}
        self._platform_stats = Counter()
        self._topic_stats = Counter()

    def learn_from_research(self, research_data: dict):
        """从研究数据学习用户偏好

        Args:
            research_data: 研究数据
        """
        platform = research_data.get("platform", "")
        tags = research_data.get("tags", [])

        if platform:
            self._platform_stats[platform] += 1
        if tags:
            self._topic_stats.update(tags)

    def get_recommendations(
        self,
        available_sources: list,
        limit: int = 5,
    ) -> list[Recommendation]:
        """获取推荐

        Args:
            available_sources: 可用的播客源列表
            limit: 返回数量

        Returns:
            推荐列表
        """
        recommendations = []

        # 基于平台偏好推荐
        if self._platform_stats:
            top_platforms = [p for p, _ in self._platform_stats.most_common(3)]
            for source in available_sources:
                for platform in top_platforms:
                    if platform.lower() in source.lower():
                        recommendations.append(Recommendation(
                            source=source,
                            title=source,
                            reason=f"匹配你喜欢的平台: {platform}",
                            score=0.8,
                            platform=platform,
                        ))

        # 基于话题偏好推荐
        if self._topic_stats:
            top_topics = [t for t, _ in self._topic_stats.most_common(5)]
            for source in available_sources:
                for topic in top_topics:
                    if topic.lower() in source.lower():
                        recommendations.append(Recommendation(
                            source=source,
                            title=source,
                            reason=f"包含你关注的话题: {topic}",
                            score=0.6,
                            platform="",
                        ))

        # 去重并排序
        seen = set()
        unique_recs = []
        for rec in recommendations:
            if rec.source not in seen:
                seen.add(rec.source)
                unique_recs.append(rec)

        unique_recs.sort(key=lambda x: x.score, reverse=True)
        return unique_recs[:limit]

    def get_similar_podcasts(self, source: str, all_sources: list, limit: int = 5) -> list[Recommendation]:
        """获取相似播客

        Args:
            source: 源播客
            all_sources: 所有播客列表
            limit: 返回数量

        Returns:
            相似播客列表
        """
        similar = []

        # 提取关键词
        keywords = set(source.lower().split())

        for other in all_sources:
            if other == source:
                continue

            # 计算相似度
            other_words = set(other.lower().split())
            overlap = len(keywords & other_words)
            if overlap > 0:
                similar.append(Recommendation(
                    source=other,
                    title=other,
                    reason=f"与当前播客有 {overlap} 个共同关键词",
                    score=overlap / max(len(keywords), 1),
                    platform="",
                ))

        similar.sort(key=lambda x: x.score, reverse=True)
        return similar[:limit]


# 全局实例
_recommender: Optional[PodcastRecommender] = None


def get_recommender() -> PodcastRecommender:
    """获取全局推荐器"""
    global _recommender
    if _recommender is None:
        _recommender = PodcastRecommender()
    return _recommender
