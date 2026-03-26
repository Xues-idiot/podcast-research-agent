"""研究趋势分析 - 分析研究历史发现趋势"""

import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


@dataclass
class TrendReport:
    """趋势报告"""
    period: str = ""
    total_researches: int = 0
    platform_breakdown: dict = None
    topic_trends: dict = None
    activity_timeline: list = None
    insights: list = None

    def __post_init__(self):
        if self.platform_breakdown is None:
            self.platform_breakdown = {}
        if self.topic_trends is None:
            self.topic_trends = {}
        if self.activity_timeline is None:
            self.activity_timeline = []
        if self.insights is None:
            self.insights = []


class TrendAnalyzer:
    """趋势分析器"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化分析器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "trends"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._history_file = self.storage_path / "history.json"
        self._history: list = []
        self._load()

    def _load(self):
        """加载历史数据"""
        if self._history_file.exists():
            try:
                with open(self._history_file, "r", encoding="utf-8") as f:
                    self._history = json.load(f)
            except json.JSONDecodeError:
                self._history = []

    def _save(self):
        """保存历史数据"""
        temp_file = self._history_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(self._history, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._history_file)

    def record_research(self, research_data: dict):
        """记录研究

        Args:
            research_data: 研究数据
        """
        record = {
            "id": research_data.get("id", ""),
            "title": research_data.get("title", ""),
            "platform": research_data.get("platform", ""),
            "source": research_data.get("source", ""),
            "timestamp": research_data.get("timestamp", datetime.now().isoformat()),
            "keypoints_count": len(research_data.get("keypoints", [])),
            "tags": research_data.get("tags", []),
            "duration": research_data.get("duration", 0),
        }
        self._history.append(record)
        self._save()

    def analyze(
        self,
        days: int = 30,
        group_by: str = "day",
    ) -> TrendReport:
        """分析趋势

        Args:
            days: 分析天数
            group_by: 分组方式 - day, week, month

        Returns:
            趋势报告
        """
        report = TrendReport()
        cutoff = datetime.now() - timedelta(days=days)

        # 筛选数据
        recent = []
        for item in self._history:
            try:
                item_time = datetime.fromisoformat(item.get("timestamp", ""))
                if item_time >= cutoff:
                    recent.append(item)
            except:
                pass

        report.total_researches = len(recent)
        report.period = f"最近{days}天"

        # 平台分布
        report.platform_breakdown = self._analyze_platforms(recent)

        # 话题趋势
        report.topic_trends = self._analyze_topics(recent)

        # 活动时间线
        report.activity_timeline = self._analyze_timeline(recent, group_by)

        # 生成洞察
        report.insights = self._generate_insights(report, recent)

        return report

    def _analyze_platforms(self, data: list) -> dict:
        """分析平台分布"""
        platforms = Counter(item.get("platform", "unknown") for item in data)
        return dict(platforms.most_common(10))

    def _analyze_topics(self, data: list) -> dict:
        """分析话题趋势"""
        all_tags = []
        for item in data:
            all_tags.extend(item.get("tags", []))

        tag_counts = Counter(all_tags)
        return dict(tag_counts.most_common(20))

    def _analyze_timeline(
        self,
        data: list,
        group_by: str,
    ) -> list:
        """分析活动时间线"""
        timeline = defaultdict(lambda: {"count": 0, "keypoints": 0, "duration": 0})

        for item in data:
            try:
                timestamp = datetime.fromisoformat(item.get("timestamp", ""))
                if group_by == "day":
                    key = timestamp.strftime("%Y-%m-%d")
                elif group_by == "week":
                    key = timestamp.strftime("%Y-W%U")
                else:
                    key = timestamp.strftime("%Y-%m")

                timeline[key]["count"] += 1
                timeline[key]["keypoints"] += item.get("keypoints_count", 0)
                timeline[key]["duration"] += item.get("duration", 0)
            except:
                pass

        result = [
            {
                "period": period,
                "researches": stats["count"],
                "keypoints": stats["keypoints"],
                "duration_minutes": round(stats["duration"] / 60, 1),
            }
            for period, stats in sorted(timeline.items())
        ]

        return result

    def _generate_insights(self, report: TrendReport, data: list) -> list:
        """生成洞察"""
        insights = []

        # 最活跃的平台
        if report.platform_breakdown:
            top_platform = max(report.platform_breakdown.items(), key=lambda x: x[1])
            insights.append(f"你最活跃的平台是 {top_platform[0]}，共研究了 {top_platform[1]} 个内容")

        # 热门话题
        if report.topic_trends:
            top_topics = list(report.topic_trends.items())[:3]
            topics_str = "、".join([f"{t[0]}({t[1]}次)" for t in top_topics])
            insights.append(f"热门话题包括：{topics_str}")

        # 研究频率
        if report.total_researches > 0:
            avg_per_week = report.total_researches / 4
            if avg_per_week > 3:
                insights.append(f"你的研究频率很高，平均每周 {avg_per_week:.1f} 个内容")
            elif avg_per_week > 1:
                insights.append(f"你的研究频率适中，平均每周 {avg_per_week:.1f} 个内容")
            else:
                insights.append("建议增加研究频率以获取更多知识")

        # 要点产出
        total_keypoints = sum(item.get("keypoints_count", 0) for item in data)
        if total_keypoints > 0:
            insights.append(f"共产出了 {total_keypoints} 个关键要点")

        return insights

    def get_topic_network(self, days: int = 30) -> dict:
        """构建话题网络（哪些话题经常一起出现）

        Args:
            days: 分析天数

        Returns:
            话题网络
        """
        cutoff = datetime.now() - timedelta(days=days)
        tag_pairs = Counter()

        for item in self._history:
            try:
                item_time = datetime.fromisoformat(item.get("timestamp", ""))
                if item_time >= cutoff:
                    tags = item.get("tags", [])
                    # 统计标签对共现
                    for i, tag1 in enumerate(tags):
                        for tag2 in tags[i+1:]:
                            pair = tuple(sorted([tag1, tag2]))
                            tag_pairs[pair] += 1
            except:
                pass

        # 转换为网络格式
        nodes = set()
        links = []

        for (tag1, tag2), weight in tag_pairs.most_common(30):
            nodes.add(tag1)
            nodes.add(tag2)
            links.append({
                "source": tag1,
                "target": tag2,
                "weight": weight,
            })

        return {
            "nodes": [{"id": n} for n in nodes],
            "links": links,
        }


# 全局实例
_trend_analyzer: Optional[TrendAnalyzer] = None


def get_trend_analyzer() -> TrendAnalyzer:
    """获取全局趋势分析器"""
    global _trend_analyzer
    if _trend_analyzer is None:
        _trend_analyzer = TrendAnalyzer()
    return _trend_analyzer
