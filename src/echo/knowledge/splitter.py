"""文本分割器 - 将播客转录分割成Entry

支持多种分割策略：
- 按段落分割
- 按句子分割
- 按时间窗口分割
- 递归字符分割（参考LangChain）
"""

import re
from dataclasses import dataclass
from typing import Callable, Optional

from echo.knowledge.entry import Entry


@dataclass
class TextSplitter:
    """文本分割器

    将长文本（转录）分割成较小的Entry，每个Entry包含：
    - raw: 原始文本
    - compiled: 编译后的文本（用于检索）
    - start_time: 开始时间
    - end_time: 结束时间
    """

    chunk_size: int = 500  # 按字符数分割
    chunk_overlap: int = 50  # 重叠字符数
    separators: list[str] = None  # 分割符列表

    def __post_init__(self):
        if self.separators is None:
            self.separators = ["\n\n", "\n", "。", "！", "？", ". ", "! ", "? ", " ", "\t"]

    def split_transcript(
        self,
        podcast_id: str,
        transcript_segments: list[dict],
        min_duration: float = 5.0,
        max_duration: float = 120.0,
    ) -> list[Entry]:
        """将转录分割成Entry

        Args:
            podcast_id: 播客ID
            transcript_segments: 转录片段列表，每项包含 start, end, text
            min_duration: 最小Entry时长（秒）
            max_duration: 最大Entry时长（秒）

        Returns:
            Entry列表
        """
        entries = []
        current_text = ""
        current_start = 0.0
        current_end = 0.0

        for segment in transcript_segments:
            start = segment.get("start", 0)
            end = segment.get("end", start)
            text = segment.get("text", "")

            # 如果当前Entry加上这个片段会超过最大时长，先保存当前Entry
            if current_text and (end - current_start) >= max_duration:
                # 保存当前Entry
                if current_text.strip():
                    entry = self._create_entry(
                        podcast_id=podcast_id,
                        raw=current_text.strip(),
                        start_time=current_start,
                        end_time=current_end,
                    )
                    entries.append(entry)

                # 开始新的Entry
                current_text = text
                current_start = start
                current_end = end
            else:
                # 添加到当前Entry
                if current_text:
                    current_text += " " + text
                else:
                    current_text = text
                    current_start = start
                current_end = end

        # 保存最后一个Entry (不检查min_duration，确保不丢失内容)
        if current_text.strip():
            entry = self._create_entry(
                podcast_id=podcast_id,
                raw=current_text.strip(),
                start_time=current_start,
                end_time=current_end,
            )
            entries.append(entry)

        return entries

    def split_text(self, text: str) -> list[str]:
        """将纯文本分割成块

        使用递归分割策略，依次尝试不同的分割符

        Args:
            text: 待分割文本

        Returns:
            文本块列表
        """
        if not text:
            return []

        chunks = [text]

        for separator in self.separators:
            if len(chunks) == 1 and separator not in chunks[0]:
                continue

            new_chunks = []
            for chunk in chunks:
                if len(chunk) <= self.chunk_size:
                    new_chunks.append(chunk)
                else:
                    parts = chunk.split(separator)
                    current = ""

                    for part in parts:
                        test = current + (separator if current else "") + part
                        if len(test) <= self.chunk_size:
                            current = test
                        else:
                            if current:
                                new_chunks.append(current.strip())
                            # 如果单个part超过chunk_size，继续分割
                            while len(part) > self.chunk_size:
                                new_chunks.append(part[:self.chunk_size])
                                part = part[self.chunk_size:]
                            current = part

                    if current.strip():
                        new_chunks.append(current.strip())

            chunks = new_chunks

        return [c.strip() for c in chunks if c.strip()]

    def _create_entry(
        self,
        podcast_id: str,
        raw: str,
        start_time: float,
        end_time: float,
    ) -> Entry:
        """创建Entry"""
        # 编译文本：取前500字符或整个文本（取较短者）
        compiled = raw[:500] if len(raw) > 500 else raw

        return Entry(
            podcast_id=podcast_id,
            raw=raw,
            compiled=compiled,
            start_time=start_time,
            end_time=end_time,
            metadata={
                "duration": end_time - start_time,
                "word_count": len(raw),
            }
        )


class RecursiveTextSplitter(TextSplitter):
    """递归文本分割器

    参考 LangChain 的 RecursiveCharacterTextSplitter，
    优先按段落分割，然后按句子，最后按单词
    """

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
    ):
        super().__init__(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", "。", "！", "？", ". ", "! ", "? ", " ", ""],
        )

    def split_text_with_overlap(self, text: str) -> list[str]:
        """带重叠的分割

        每个文本块与下一个块有重叠部分，用于保持上下文连贯性

        Args:
            text: 待分割文本

        Returns:
            文本块列表
        """
        if not text:
            return []

        chunks = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = min(start + self.chunk_size, text_len)
            chunk = text[start:end]
            chunks.append(chunk)

            # 下一个块的起始位置（考虑重叠）
            start = end - self.chunk_overlap
            if start >= text_len - self.chunk_overlap:
                break

        return chunks
