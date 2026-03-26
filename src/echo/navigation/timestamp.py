"""时间戳导航器 - 基于关键内容的时间戳跳转

参考 khoj 的 trainOfThoughtVideoPlayer 实现，
支持按时间戳跳转到播客的关键内容位置。
"""

from dataclasses import dataclass, field
from typing import Optional
import bisect


# 重要性字符串到浮点数的映射
IMPORTANCE_TO_RELEVANCE = {
    "high": 1.0,
    "medium": 0.5,
    "low": 0.2,
    "高": 1.0,
    "中": 0.5,
    "低": 0.2,
}


def _importance_to_relevance(importance: str, default: float = 0.5) -> float:
    """将重要性字符串转换为相关度浮点数

    Args:
        importance: 重要性字符串 (high/medium/low 或 高/中/低)
        default: 默认值

    Returns:
        float: 相关度分数 (0-1)
    """
    return IMPORTANCE_TO_RELEVANCE.get(importance.lower() if isinstance(importance, str) else "", default)


@dataclass
class TimestampEntry:
    """时间戳条目

    Attributes:
        timestamp: 时间戳（秒）
        content: 内容摘要
        entry_id: 关联的Entry ID
        type: 条目类型 (keypoint, qa, topic)
        relevance: 相关度评分 (0-1)
    """
    timestamp: float
    content: str
    entry_id: str = ""
    type: str = "content"  # keypoint, qa, topic, content
    relevance: float = 1.0


@dataclass
class JumpResult:
    """跳转结果

    Attributes:
        target_timestamp: 目标时间戳
        nearby_entries: 附近的条目列表
        context_before: 跳转前的上下文内容
        context_after: 跳转后的上下文内容
        jump_type: 跳转类型
    """
    target_timestamp: float
    nearby_entries: list[TimestampEntry] = field(default_factory=list)
    context_before: str = ""
    context_after: str = ""
    jump_type: str = "exact"  # exact, nearest, keyframe


class TimestampNavigator:
    """时间戳导航器

    支持：
    - 按时间戳获取附近内容
    - 获取关键时刻列表
    - 跳转到最相关的时刻
    """

    def __init__(self, entries: list):
        """初始化导航器

        Args:
            entries: Entry列表，每个Entry需要有以下属性：
                    - start_time: float
                    - end_time: float
                    - id: str
                    - compiled: str
                    - raw: str
        """
        self.entries = sorted(entries, key=lambda e: e.start_time)
        self._timestamps = [e.start_time for e in self.entries]

    def jump_to(
        self,
        target_timestamp: float,
        window_seconds: float = 30.0,
    ) -> JumpResult:
        """跳转到指定时间戳

        Args:
            target_timestamp: 目标时间戳（秒）
            window_seconds: 窗口大小（秒）

        Returns:
            JumpResult: 跳转结果
        """
        if not self.entries:
            return JumpResult(target_timestamp=target_timestamp, jump_type="empty")

        # 找到最近的Entry
        idx = self._find_nearest_entry(target_timestamp)
        if idx < 0:
            idx = 0
        if idx >= len(self.entries):
            idx = len(self.entries) - 1

        target_entry = self.entries[idx]
        actual_timestamp = target_entry.start_time

        # 确定跳转类型
        if abs(actual_timestamp - target_timestamp) < 1.0:
            jump_type = "exact"
        elif actual_timestamp > target_timestamp:
            jump_type = "forward"
        else:
            jump_type = "backward"

        # 获取窗口内的条目
        nearby = self._get_entries_in_window(
            actual_timestamp,
            window_seconds / 2
        )

        # 构建上下文
        context_before = target_entry.raw[:200] if target_entry.raw else ""
        context_after = ""
        if idx + 1 < len(self.entries):
            context_after = self.entries[idx + 1].raw[:200] if self.entries[idx + 1].raw else ""

        return JumpResult(
            target_timestamp=actual_timestamp,
            nearby_entries=nearby,
            context_before=context_before,
            context_after=context_after,
            jump_type=jump_type,
        )

    def get_key_moments(
        self,
        num_moments: int = 10,
    ) -> list[TimestampEntry]:
        """获取关键时刻列表

        使用智能分析而不是均匀采样：
        1. 基于内容特征评分（长度、问题模式、数字模式）
        2. 检测话题变化点（语义突变）
        3. 选择高权重时刻（开头、重要讨论节点）

        Args:
            num_moments: 返回的时刻数量

        Returns:
            list[TimestampEntry]: 关键时刻列表
        """
        if not self.entries:
            return []

        # 第一步：对每个entry计算重要性得分
        scored_entries = []
        for i, entry in enumerate(self.entries):
            score = self._calculate_importance_score(entry, i)
            scored_entries.append((entry, score))

        # 第二步：检测话题变化点
        topic_change_scores = self._detect_topic_changes()

        # 第三步：综合评分并选择关键时刻
        final_scores = []
        for i, (entry, base_score) in enumerate(scored_entries):
            combined_score = base_score + topic_change_scores[i] * 0.5
            final_scores.append((entry, combined_score))

        # 优先选择开头和结尾
        if final_scores:
            # 开头很重要
            final_scores[0] = (final_scores[0][0], final_scores[0][1] + 2.0)
            # 结尾也很重要
            final_scores[-1] = (final_scores[-1][0], final_scores[-1][1] + 1.5)

        # 按得分排序，选择最高的
        final_scores.sort(key=lambda x: x[1], reverse=True)

        # 选择前N个，然后按时间排序
        selected = final_scores[:num_moments]

        # 去重：如果两个时刻太近（30秒内），只保留得分更高的
        filtered = self._filter_close_moments(selected, threshold=30.0)

        # 按时间排序
        filtered.sort(key=lambda x: x[0].start_time)

        # 转换为TimestampEntry
        moments = []
        for entry, score in filtered:
            moments.append(TimestampEntry(
                timestamp=entry.start_time,
                content=entry.compiled[:100] + "..." if len(entry.compiled) > 100 else entry.compiled,
                entry_id=entry.id,
                type="intelligent",
                relevance=min(score / 10.0, 1.0),  # 归一化到0-1
            ))

        return moments[:num_moments]

    def _calculate_importance_score(self, entry, index: int) -> float:
        """计算单个entry的重要性得分

        考虑因素：
        - 内容长度（太短可能不重要，太长可能包含重要细节）
        - 是否包含问号（问题通常意味着重要讨论）
        - 是否包含数字（数据、统计数据通常是重点）
        - 是否包含关键词（主题词、强调词）
        - 位置因素（开头、结尾略高）
        """
        score = 0.0
        text = entry.compiled.lower()
        raw_text = entry.raw.lower() if hasattr(entry, 'raw') else text

        # 长度评分：适中的长度更有信息量
        length = len(text)
        if 100 < length < 500:
            score += 1.5
        elif length >= 500:
            score += 2.0
        elif length < 50:
            score -= 0.5

        # 问号评分：问题通常表示重要讨论
        if '?' in raw_text:
            score += 1.5

        # 数字评分：包含数据的句子通常是重点
        import re
        numbers = re.findall(r'\d+', text)
        if len(numbers) >= 2:
            score += 2.0
        elif len(numbers) == 1:
            score += 1.0

        # 关键词评分：出现主题相关关键词
        important_keywords = ['但是', '然而', '所以', '因此', '关键', '重要', '特别',
                           '其实', '事实上', '最重要的是', '需要', '应该', '必须',
                           'first', 'important', 'key', 'main', 'most', 'should', 'must']
        keyword_count = sum(1 for kw in important_keywords if kw in text)
        score += keyword_count * 0.5

        # 位置评分：开头和结尾略高
        total = len(self.entries)
        if index < 3:  # 开头
            score += 0.5
        elif index > total - 3:  # 结尾
            score += 0.3

        return score

    def _detect_topic_changes(self) -> list[float]:
        """检测话题变化点

        通过比较相邻entry的内容相似度来检测话题边界。
        相似度突然下降意味着话题发生了变化。

        Returns:
            list[float]: 每个位置的话题变化得分（越高越可能是话题变化点）
        """
        if len(self.entries) < 2:
            return [0.0] * len(self.entries)

        scores = [0.0] * len(self.entries)

        for i in range(1, len(self.entries)):
            prev_text = self.entries[i-1].compiled.lower()
            curr_text = self.entries[i].compiled.lower()

            # 计算简单的词重叠
            prev_words = set(prev_text.split())
            curr_words = set(curr_text.split())

            # 去除停用词
            stopwords = {'的', '了', '是', '在', '和', '与', '或', '这', '那', '有', '没有',
                        'the', 'a', 'an', 'is', 'are', 'was', 'were', 'and', 'or', 'to', 'of'}
            prev_words -= stopwords
            curr_words -= stopwords

            if not prev_words or not curr_words:
                continue

            overlap = len(prev_words & curr_words)
            union = len(prev_words | curr_words)
            similarity = overlap / union if union > 0 else 0

            # 相似度突然下降意味着话题变化
            if similarity < 0.2:  # 话题变化点
                scores[i] += 2.0

        return scores

    def _filter_close_moments(
        self,
        scored_entries: list[tuple],
        threshold: float = 30.0,
    ) -> list[tuple]:
        """过滤时间太近的时刻，保留最重要的"""
        if not scored_entries:
            return []

        filtered = []
        for entry, score in scored_entries:
            # 检查是否与已选时刻太近
            too_close = False
            for selected_entry, _ in filtered:
                if abs(entry.start_time - selected_entry.start_time) < threshold:
                    too_close = True
                    break

            if not too_close:
                filtered.append((entry, score))

        return filtered

    def get_moments_by_keypoints(
        self,
        keypoints: list[dict],
    ) -> list[TimestampEntry]:
        """根据关键点获取对应的时间戳

        Args:
            keypoints: 关键点列表，每个包含 content 和可选的 timestamp

        Returns:
            list[TimestampEntry]: 时间戳时刻列表
        """
        moments = []
        for kp in keypoints:
            content = kp.get("content", "")
            # 如果关键点有时间戳，直接使用
            if "timestamp" in kp:
                timestamp = kp["timestamp"]
            elif "time" in kp:
                timestamp = kp["time"]
            else:
                # 否则进行语义匹配
                timestamp = self._find_best_matching_timestamp(content)

            moments.append(TimestampEntry(
                timestamp=timestamp,
                content=content[:100] + "..." if len(content) > 100 else content,
                entry_id=kp.get("entry_id", ""),
                type="keypoint",
                relevance=_importance_to_relevance(kp.get("importance", ""), 0.5),
            ))

        return moments

    def get_moments_by_qa(
        self,
        qa_pairs: list[dict],
    ) -> list[TimestampEntry]:
        """根据问答对获取对应的时间戳

        Args:
            qa_pairs: 问答对列表

        Returns:
            list[TimestampEntry]: 时间戳时刻列表
        """
        moments = []
        for qa in qa_pairs:
            question = qa.get("question", "")
            answer = qa.get("answer", "")
            # 查找答案内容对应的时间戳
            timestamp = self._find_best_matching_timestamp(answer)
            moments.append(TimestampEntry(
                timestamp=timestamp,
                content=f"Q: {question}\nA: {answer[:100]}..." if len(answer) > 100 else f"Q: {question}\nA: {answer}",
                type="qa",
                relevance=0.7,
            ))

        return moments

    def format_timestamp(self, seconds: float) -> str:
        """格式化时间戳

        Args:
            seconds: 秒数

        Returns:
            str: 格式化的时间戳字符串 (MM:SS 或 HH:MM:SS)
        """
        if seconds < 0:
            return "00:00"

        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)

        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        return f"{minutes:02d}:{secs:02d}"

    def parse_timestamp(self, timestamp_str: str) -> float:
        """解析时间戳字符串

        Args:
            timestamp_str: 时间戳字符串 (MM:SS 或 HH:MM:SS)

        Returns:
            float: 秒数
        """
        parts = timestamp_str.split(":")
        try:
            if len(parts) == 2:
                # MM:SS
                return int(parts[0]) * 60 + int(parts[1])
            elif len(parts) == 3:
                # HH:MM:SS
                return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        except ValueError:
            pass
        return 0.0

    def _find_nearest_entry(self, target_time: float) -> int:
        """找到最接近目标时间的Entry索引"""
        if not self._timestamps:
            return -1
        # bisect_left 返回插入点
        idx = bisect.bisect_left(self._timestamps, target_time)
        if idx == 0:
            return 0
        if idx >= len(self._timestamps):
            return len(self._timestamps) - 1
        # 比较前后两个时间戳
        if abs(self._timestamps[idx] - target_time) < abs(self._timestamps[idx - 1] - target_time):
            return idx
        return idx - 1

    def _get_entries_in_window(
        self,
        center_time: float,
        window_radius: float,
    ) -> list[TimestampEntry]:
        """获取时间窗口内的条目"""
        result = []
        for entry in self.entries:
            if abs(entry.start_time - center_time) <= window_radius:
                result.append(TimestampEntry(
                    timestamp=entry.start_time,
                    content=entry.compiled[:100] + "..." if len(entry.compiled) > 100 else entry.compiled,
                    entry_id=entry.id,
                    type="content",
                    relevance=1.0 - abs(entry.start_time - center_time) / (window_radius + 1),
                ))
        return result

    def _find_best_matching_timestamp(self, content: str) -> float:
        """根据内容找到最匹配的时间戳"""
        if not self.entries:
            return 0.0

        content_lower = content.lower()
        best_idx = 0
        best_score = 0

        for i, entry in enumerate(self.entries):
            score = 0
            entry_text = entry.compiled.lower()
            # 简单的词重叠计数
            content_words = set(content_lower.split())
            entry_words = set(entry_text.split())
            overlap = len(content_words & entry_words)
            if overlap > 0:
                score = overlap / len(content_words)
            if score > best_score:
                best_score = score
                best_idx = i

        return self.entries[best_idx].start_time if self.entries else 0.0
