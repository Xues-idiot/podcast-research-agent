"""研究结果质量评分系统"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class QualityScore:
    """质量评分"""
    research_id: str = ""
    overall_score: float = 0.0  # 0-100
    completeness: float = 0.0  # 完整性
    accuracy: float = 0.0  # 准确性
    depth: float = 0.0  # 深度
    citations: float = 0.0  # 引用质量
    graded_at: str = ""


class QualityGrader:
    """质量评分器"""

    def grade(self, research_result: dict) -> QualityScore:
        """评估研究结果质量

        Args:
            research_result: 研究结果字典

        Returns:
            质量评分
        """
        score = QualityScore(
            research_id=research_result.get("id", ""),
            graded_at=datetime.now().isoformat(),
        )

        # 评估完整性
        score.completeness = self._grade_completeness(research_result)

        # 评估准确性
        score.accuracy = self._grade_accuracy(research_result)

        # 评估深度
        score.depth = self._grade_depth(research_result)

        # 评估引用
        score.citations = self._grade_citations(research_result)

        # 计算总分（加权平均）
        score.overall_score = (
            score.completeness * 0.25 +
            score.accuracy * 0.30 +
            score.depth * 0.25 +
            score.citations * 0.20
        )

        return score

    def _grade_completeness(self, result: dict) -> float:
        """评估完整性"""
        score = 0.0
        total = 0

        # 检查必要字段
        required_fields = ["summary", "keypoints"]
        for field in required_fields:
            if result.get(field):
                score += 50.0
            total += 50.0

        # 检查额外字段
        extra_fields = ["mindmap", "knowledge_cards", "qa_pairs", "report"]
        for field in extra_fields:
            if result.get(field):
                score += 10.0
            total += 10.0

        return score / total * 100.0 if total > 0 else 0.0

    def _grade_accuracy(self, result: dict) -> float:
        """评估准确性"""
        # 基础分
        score = 70.0

        # 检查summary是否有实质性内容
        summary = result.get("summary", {})
        if isinstance(summary, dict):
            content = summary.get("content", "")
            if len(content) > 100:
                score += 10.0
            if any(marker in content for marker in ["主要", "关键", "核心", "重点"]):
                score += 5.0

        # 检查keypoints是否有具体内容
        keypoints = result.get("keypoints", [])
        if keypoints:
            avg_length = sum(len(str(kp.get("content", ""))) for kp in keypoints) / len(keypoints)
            if avg_length > 50:
                score += 10.0

        return min(100.0, score)

    def _grade_depth(self, result: dict) -> float:
        """评估深度"""
        score = 50.0

        # keypoints数量
        keypoints = result.get("keypoints", [])
        if len(keypoints) >= 5:
            score += 15.0
        elif len(keypoints) >= 3:
            score += 10.0

        # 知识卡片数量
        kcards = result.get("knowledge_cards", [])
        if len(kcards) >= 3:
            score += 15.0
        elif len(kcards) >= 1:
            score += 10.0

        # QA对数量
        qa_pairs = result.get("qa_pairs", [])
        if len(qa_pairs) >= 5:
            score += 10.0
        elif len(qa_pairs) >= 3:
            score += 5.0

        return min(100.0, score)

    def _grade_citations(self, result: dict) -> float:
        """评估引用质量"""
        score = 50.0

        # 检查keypoints是否有引用
        keypoints = result.get("keypoints", [])
        cited_count = sum(1 for kp in keypoints if kp.get("citations") or kp.get("timestamp"))
        if keypoints:
            citation_ratio = cited_count / len(keypoints)
            score += citation_ratio * 30.0

        # 检查知识卡片是否有引用
        kcards = result.get("knowledge_cards", [])
        if kcards:
            score += 10.0

        return min(100.0, score)

    def get_quality_tier(self, score: float) -> str:
        """获取质量等级

        Args:
            score: 分数

        Returns:
            等级描述
        """
        if score >= 90:
            return "优秀"
        elif score >= 75:
            return "良好"
        elif score >= 60:
            return "一般"
        elif score >= 40:
            return "较差"
        else:
            return "很差"


# 全局实例
_quality_grader: Optional[QualityGrader] = None


def get_quality_grader() -> QualityGrader:
    """获取全局评分器"""
    global _quality_grader
    if _quality_grader is None:
        _quality_grader = QualityGrader()
    return _quality_grader
