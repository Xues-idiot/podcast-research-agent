"""内容格式检测器"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FormatResult:
    """格式检测结果"""
    format_type: str
    confidence: float
    language: str
    is_timestamped: bool
    has_speaker_labels: bool


class FormatDetector:
    """检测音视频内容格式"""

    def detect(self, content: str) -> FormatResult:
        """检测内容格式"""
        if not content:
            return FormatResult(
                format_type="unknown",
                confidence=0.0,
                language="unknown",
                is_timestamped=False,
                has_speaker_labels=False
            )

        lines = content.split("\n")
        timestamp_count = 0
        speaker_count = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            # 时间戳格式: [00:01:23] 或 00:01:23
            if self._is_timestamp_line(line):
                timestamp_count += 1
            # 说话人标签: Speaker 1: 或 【Speaker 1】
            if self._has_speaker_label(line):
                speaker_count += 1

        total_lines = len([l for l in lines if l.strip()])
        timestamp_ratio = timestamp_count / total_lines if total_lines > 0 else 0
        speaker_ratio = speaker_count / total_lines if total_lines > 0 else 0

        return FormatResult(
            format_type=self._infer_format_type(timestamp_ratio, speaker_ratio),
            confidence=min(1.0, (timestamp_ratio + speaker_ratio) / 2 + 0.3),
            language=self._detect_language(content),
            is_timestamped=timestamp_ratio > 0.3,
            has_speaker_labels=speaker_ratio > 0.2
        )

    def _is_timestamp_line(self, line: str) -> bool:
        import re
        patterns = [
            r'\[\d{1,2}:\d{2}(:\d{2})?\]',
            r'^\d{1,2}:\d{2}(:\d{2})?\s',
        ]
        for p in patterns:
            if re.match(p, line):
                return True
        return False

    def _has_speaker_label(self, line: str) -> bool:
        import re
        patterns = [
            r'^【[^】]+】',
            r'^[A-Za-z]+\s*\d+:',
            r'^Speaker\s+\d+:',
        ]
        for p in patterns:
            if re.match(p, line):
                return True
        return False

    def _infer_format_type(self, timestamp_ratio: float, speaker_ratio: float) -> str:
        if timestamp_ratio > 0.5 and speaker_ratio > 0.3:
            return "transcript_with_speakers"
        elif timestamp_ratio > 0.5:
            return "transcript"
        elif speaker_ratio > 0.3:
            return "dialogue"
        elif timestamp_ratio > 0.1:
            return "hybrid"
        return "plain_text"

    def _detect_language(self, content: str) -> str:
        chinese_count = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
        total = len(content)
        ratio = chinese_count / total if total > 0 else 0
        return "chinese" if ratio > 0.3 else "english"


_detector: Optional[FormatDetector] = None

def get_format_detector() -> FormatDetector:
    global _detector
    if _detector is None:
        _detector = FormatDetector()
    return _detector