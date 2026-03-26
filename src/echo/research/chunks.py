"""智能分块策略"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Chunk:
    """分块结果"""
    content: str
    start_index: int
    end_index: int
    chunk_type: str


class ChunkingStrategy:
    """内容分块策略"""

    def chunk_by_size(self, content: str, max_size: int = 1000, overlap: int = 100) -> list[Chunk]:
        """按大小分块"""
        chunks = []
        start = 0
        content_len = len(content)

        while start < content_len:
            end = min(start + max_size, content_len)
            # 尝试在句子边界处切割
            if end < content_len:
                boundary = self._find_sentence_boundary(content, end)
                if boundary > start:
                    end = boundary

            chunks.append(Chunk(
                content=content[start:end],
                start_index=start,
                end_index=end,
                chunk_type="size_based"
            ))
            start = end - overlap if end - overlap > start else start + max_size

        return chunks

    def chunk_by_paragraph(self, content: str, max_paragraphs: int = 5) -> list[Chunk]:
        """按段落分块"""
        paragraphs = content.split("\n\n")
        chunks = []
        start_index = 0

        for i in range(0, len(paragraphs), max_paragraphs):
            group = paragraphs[i:i + max_paragraphs]
            chunk_content = "\n\n".join(group)
            chunk_len = len(chunk_content)

            chunks.append(Chunk(
                content=chunk_content,
                start_index=start_index,
                end_index=start_index + chunk_len,
                chunk_type="paragraph_based"
            ))
            start_index += chunk_len

        return chunks

    def chunk_by_topic(self, content: str, min_topic_size: int = 200) -> list[Chunk]:
        """按主题分块"""
        import re
        # 识别主题标记
        topic_markers = [
            r'^#{1,3}\s+',  # Markdown标题
            r'^\d+\.\s+[A-Z]',  # 编号标题
            r'^【[^】]+】',  # 中文方括号标题
        ]

        sections = []
        lines = content.split("\n")
        current_section = []
        current_start = 0

        for i, line in enumerate(lines):
            is_marker = False
            for pattern in topic_markers:
                if re.match(pattern, line.strip()):
                    is_marker = True
                    break

            if is_marker and current_section:
                sections.append(("\n".join(current_section), current_start))
                current_section = [line]
                current_start = content.find(line)
            else:
                current_section.append(line)

        if current_section:
            sections.append(("\n".join(current_section), current_start))

        chunks = []
        for section_content, start_idx in sections:
            if len(section_content) >= min_topic_size:
                chunks.append(Chunk(
                    content=section_content,
                    start_index=start_idx,
                    end_index=start_idx + len(section_content),
                    chunk_type="topic_based"
                ))

        return chunks if chunks else self.chunk_by_size(content)

    def _find_sentence_boundary(self, content: str, pos: int) -> int:
        """查找最近的句子边界"""
        markers = ['。', '！', '？', '.', '!', '?', '\n']
        for i in range(pos - 1, max(0, pos - 200), -1):
            if content[i] in markers:
                return i + 1
        return pos


_strategies = {}


def get_chunking_strategy(name: str = "size") -> ChunkingStrategy:
    if name not in _strategies:
        _strategies[name] = ChunkingStrategy()
    return _strategies[name]