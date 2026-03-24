"""Echo 数据类型定义"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Transcript:
    """转录结果"""
    text: str
    segments: List[dict] = field(default_factory=list)
    language: str = "zh"
    duration: Optional[str] = None


@dataclass
class Summary:
    """摘要结果"""
    title: str
    summary: str
    highlights: List[str] = field(default_factory=list)


@dataclass
class KeyPoint:
    """关键要点"""
    id: int
    content: str
    importance: str = "medium"  # high, medium, low
    applications: List[str] = field(default_factory=list)


@dataclass
class RelatedItem:
    """关联条目"""
    title: str
    url: str
    content: str = ""


@dataclass
class KnowledgeCard:
    """知识卡片"""
    keypoint: str
    related: List[RelatedItem] = field(default_factory=list)
    confidence: float = 0.0


@dataclass
class MindMapBranch:
    """思维导图分支"""
    title: str
    children: List[str] = field(default_factory=list)


@dataclass
class MindMap:
    """思维导图"""
    root: str
    branches: List[MindMapBranch] = field(default_factory=list)


@dataclass
class ResearchResult:
    """完整研究结果"""
    transcript: Transcript
    summary: Summary
    keypoints: List[KeyPoint]
    mindmap: MindMap
    knowledge_cards: List[KnowledgeCard] = field(default_factory=list)
    report: str = ""

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "transcript": {
                "text": self.transcript.text,
                "segments": self.transcript.segments,
                "language": self.transcript.language,
            },
            "summary": {
                "title": self.summary.title,
                "summary": self.summary.summary,
                "highlights": self.summary.highlights,
            },
            "keypoints": [
                {
                    "id": kp.id,
                    "content": kp.content,
                    "importance": kp.importance,
                }
                for kp in self.keypoints
            ],
            "mindmap": {
                "root": self.mindmap.root,
                "branches": [
                    {"title": b.title, "children": b.children}
                    for b in self.mindmap.branches
                ]
            },
            "knowledge_cards": [
                {
                    "keypoint": card.keypoint,
                    "related": [
                        {"title": r.title, "url": r.url}
                        for r in card.related
                    ],
                    "confidence": card.confidence,
                }
                for card in self.knowledge_cards
            ],
            "report": self.report,
        }
