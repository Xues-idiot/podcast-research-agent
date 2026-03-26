"""研究结果对比器 - 对比两个播客的研究结果"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ComparisonResult:
    """对比结果"""
    topic_overlap: float  # 主题重叠度 0-1
    keypoint_similarity: float  # 要点相似度 0-1
    content_length_ratio: float  # 内容长度比
    shared_concepts: list[str]  # 共享概念
    unique_insights_a: list[str]  # A独有的洞见
    unique_insights_b: list[str]  # B独有的洞见
    summary: str  # 对比总结


class ResearchComparator:
    """研究结果对比器

    对比两个播客的研究结果，找出：
    - 主题重叠度
    - 要点相似度
    - 共享概念
    - 各自独有的洞见
    """

    def compare(self, result_a: dict, result_b: dict) -> ComparisonResult:
        """对比两个研究结果

        Args:
            result_a: 第一个播客的研究结果
            result_b: 第二个播客的研究结果

        Returns:
            对比结果
        """
        # 提取关键信息
        summary_a = result_a.get("summary", {})
        summary_b = result_b.get("summary", {})
        title_a = summary_a.get("title", "")
        title_b = summary_b.get("title", "")

        keypoints_a = result_a.get("keypoints", [])
        keypoints_b = result_b.get("keypoints", [])
        transcript_a = result_a.get("transcript", {}).get("text", "")
        transcript_b = result_b.get("transcript", {}).get("text", "")

        # 计算主题重叠度（基于标题）
        topic_overlap = self._calculate_text_overlap(title_a, title_b)

        # 计算要点相似度
        keypoint_similarity = self._calculate_keypoint_similarity(keypoints_a, keypoints_b)

        # 计算内容长度比
        len_a = len(transcript_a)
        len_b = len(transcript_b)
        content_length_ratio = min(len_a, len_b) / max(len_a, len_b) if max(len_a, len_b) > 0 else 0

        # 提取关键词
        words_a = set(transcript_a.lower().split())
        words_b = set(transcript_b.lower().split())

        # 停用词
        stopwords = {"的", "了", "是", "在", "和", "与", "或", "这", "那", "有", "没有",
                     "the", "a", "an", "is", "are", "was", "were", "and", "or", "to", "of",
                     "我", "你", "他", "她", "它", "们", "的", "了", "着", "过"}

        words_a = words_a - stopwords
        words_b = words_b - stopwords

        # 共享概念
        shared = words_a & words_b
        shared_concepts = self._extract_key_concepts(shared, min_count=3)

        # 各自独有概念
        unique_a = words_a - words_b
        unique_b = words_b - words_a
        unique_insights_a = self._extract_key_concepts(unique_a, min_count=2)
        unique_insights_b = self._extract_key_concepts(unique_b, min_count=2)

        # 生成总结
        summary = self._generate_summary(
            title_a, title_b, topic_overlap, keypoint_similarity,
            shared_concepts, unique_insights_a, unique_insights_b
        )

        return ComparisonResult(
            topic_overlap=topic_overlap,
            keypoint_similarity=keypoint_similarity,
            content_length_ratio=content_length_ratio,
            shared_concepts=shared_concepts[:10],  # 最多10个
            unique_insights_a=unique_insights_a[:5],
            unique_insights_b=unique_insights_b[:5],
            summary=summary,
        )

    def _calculate_text_overlap(self, text_a: str, text_b: str) -> float:
        """计算文本重叠度"""
        if not text_a or not text_b:
            return 0.0

        words_a = set(text_a.lower().split())
        words_b = set(text_b.lower().split())

        if not words_a or not words_b:
            return 0.0

        intersection = len(words_a & words_b)
        union = len(words_a | words_b)

        return intersection / union if union > 0 else 0.0

    def _calculate_keypoint_similarity(self, kps_a: list, kps_b: list) -> float:
        """计算要点相似度"""
        if not kps_a or not kps_b:
            return 0.0

        # 提取要点内容
        texts_a = [kp.get("content", "") for kp in kps_a]
        texts_b = [kp.get("content", "") for kp in kps_b]

        # 计算两两相似度
        similarities = []
        for ta in texts_a:
            for tb in texts_b:
                sim = self._calculate_text_overlap(ta, tb)
                similarities.append(sim)

        # 返回最大相似度的平均值
        if similarities:
            return sum(sorted(similarities, reverse=True)[:3]) / min(3, len(similarities))
        return 0.0

    def _extract_key_concepts(self, words: set, min_count: int = 2) -> list[str]:
        """提取关键概念"""
        # 过滤掉太短的词
        significant = [w for w in words if len(w) >= 2]
        # 按字母序排序返回
        return sorted(significant)[:20]

    def _generate_summary(
        self,
        title_a: str,
        title_b: str,
        topic_overlap: float,
        keypoint_similarity: float,
        shared: list[str],
        unique_a: list[str],
        unique_b: list[str],
    ) -> str:
        """生成对比总结"""
        lines = [f"## 「{title_a}」 vs 「{title_b}」对比分析\n"]

        # 整体相似度
        avg_similarity = (topic_overlap + keypoint_similarity) / 2
        if avg_similarity > 0.5:
            lines.append("### 整体结论：两期内容相似度较高\n")
        elif avg_similarity > 0.3:
            lines.append("### 整体结论：两期内容有一定关联\n")
        else:
            lines.append("### 整体结论：两期内容差异较大\n")

        # 主题重叠
        lines.append(f"**主题重叠度**: {topic_overlap:.0%}\n")
        if topic_overlap > 0.5:
            lines.append("两期播客讨论的主题高度相关。\n")
        elif topic_overlap > 0.2:
            lines.append("两期播客有一些共同的主题。\n")
        else:
            lines.append("两期播客讨论的主题差异较大。\n")

        # 要点相似度
        lines.append(f"**要点相似度**: {keypoint_similarity:.0%}\n")

        # 共享概念
        if shared:
            lines.append(f"**共同关键词**: {', '.join(shared[:8])}\n")

        # 各自独特内容
        if unique_a:
            lines.append(f"**「{title_a}」独特内容**: {', '.join(unique_a[:5])}\n")
        if unique_b:
            lines.append(f"**「{title_b}」独特内容**: {', '.join(unique_b[:5])}\n")

        return "".join(lines)


# 全局实例
_comparator: Optional[ResearchComparator] = None


def get_comparator() -> ResearchComparator:
    """获取对比器实例"""
    global _comparator
    if _comparator is None:
        _comparator = ResearchComparator()
    return _comparator
