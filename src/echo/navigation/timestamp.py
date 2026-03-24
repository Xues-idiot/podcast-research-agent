"""时间戳导航器 - 基于关键内容的时间戳跳转

参考 khoj 的 trainOfThoughtVideoPlayer 实现，
支持按时间戳跳转到播客的关键内容位置。
"""

from dataclasses import dataclass, field
from typing import Optional
import bisect


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

        基于内容长度和位置，计算最可能是关键时刻的时间点。

        Args:
            num_moments: 返回的时刻数量

        Returns:
            list[TimestampEntry]: 关键时刻列表
        """
        if not self.entries:
            return []

        moments = []
        total_duration = self.entries[-1].end_time if self.entries else 0

        # 方法1：均匀采样
        if total_duration > 0:
            interval = total_duration / (num_moments + 1)
            for i in range(1, num_moments + 1):
                target_time = interval * i
                idx = self._find_nearest_entry(target_time)
                if 0 <= idx < len(self.entries):
                    entry = self.entries[idx]
                    moments.append(TimestampEntry(
                        timestamp=entry.start_time,
                        content=entry.compiled[:100] + "..." if len(entry.compiled) > 100 else entry.compiled,
                        entry_id=entry.id,
                        type="sampled",
                        relevance=1.0 - abs(entry.start_time - target_time) / total_duration,
                    ))

        # 按时间排序
        moments.sort(key=lambda m: m.timestamp)
        return moments[:num_moments]

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
                relevance=kp.get("importance", 0.5),
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
