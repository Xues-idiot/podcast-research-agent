"""研究模板系统 - 支持不同的研究配置模板"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TemplateType(Enum):
    """模板类型"""
    STANDARD = "standard"  # 标准研究
    QUICK = "quick"  # 快速摘要
    DEEP = "deep"  # 深度研究
    INTERVIEW = "interview"  # 访谈分析
    EDUCATIONAL = "educational"  # 教育内容


@dataclass
class TemplateConfig:
    """模板配置"""
    name: str
    description: str
    template_type: TemplateType
    num_keypoints: int = 5
    num_qa_pairs: int = 5
    include_transcript: bool = True
    include_audio_overview: bool = True
    include_knowledge_cards: bool = True
    include_mindmap: bool = True
    include_report: bool = True
    custom_prompts: dict = field(default_factory=dict)


# 预设模板
TEMPLATES = {
    TemplateType.STANDARD: TemplateConfig(
        name="标准研究",
        description="完整的研究流程，包含摘要、要点、思维导图等",
        template_type=TemplateType.STANDARD,
        num_keypoints=5,
        num_qa_pairs=5,
        include_transcript=True,
        include_audio_overview=True,
        include_knowledge_cards=True,
        include_mindmap=True,
        include_report=True,
    ),
    TemplateType.QUICK: TemplateConfig(
        name="快速摘要",
        description="快速获取播客核心内容，节省时间",
        template_type=TemplateType.QUICK,
        num_keypoints=3,
        num_qa_pairs=3,
        include_transcript=False,
        include_audio_overview=False,
        include_knowledge_cards=False,
        include_mindmap=False,
        include_report=False,
    ),
    TemplateType.DEEP: TemplateConfig(
        name="深度研究",
        description="全面深入的分析，适合学习复杂主题",
        template_type=TemplateType.DEEP,
        num_keypoints=10,
        num_qa_pairs=10,
        include_transcript=True,
        include_audio_overview=True,
        include_knowledge_cards=True,
        include_mindmap=True,
        include_report=True,
        custom_prompts={
            "summary": "请提供深入详细的摘要，包含背景、核心观点、论证过程和结论",
            "keypoint": "请提取深层次的核心要点，包括独到见解和原创观点",
        },
    ),
    TemplateType.INTERVIEW: TemplateConfig(
        name="访谈分析",
        description="分析访谈类播客的人物观点和对话",
        template_type=TemplateType.INTERVIEW,
        num_keypoints=8,
        num_qa_pairs=8,
        include_transcript=True,
        include_audio_overview=True,
        include_knowledge_cards=True,
        include_mindmap=True,
        include_report=True,
        custom_prompts={
            "summary": "请分析访谈中的主要观点、争议点和结论",
            "keypoint": "请提取访谈中的关键论点、论据和嘉宾观点",
        },
    ),
    TemplateType.EDUCATIONAL: TemplateConfig(
        name="教育内容",
        description="提取教学知识点，方便复习和记忆",
        template_type=TemplateType.EDUCATIONAL,
        num_keypoints=10,
        num_qa_pairs=10,
        include_transcript=True,
        include_audio_overview=True,
        include_knowledge_cards=True,
        include_mindmap=True,
        include_report=True,
        custom_prompts={
            "summary": "请总结教育内容的主要知识点和学习目标",
            "keypoint": "请提取可用于教学的知识点，包含定义、例子和练习",
        },
    ),
}


def get_template(template_type: TemplateType) -> TemplateConfig:
    """获取模板配置"""
    return TEMPLATES.get(template_type, TEMPLATES[TemplateType.STANDARD])


def list_templates() -> list[dict]:
    """列出所有可用模板"""
    return [
        {
            "type": t.template_type.value,
            "name": t.name,
            "description": t.description,
            "num_keypoints": t.num_keypoints,
            "features": {
                "transcript": t.include_transcript,
                "audio_overview": t.include_audio_overview,
                "knowledge_cards": t.include_knowledge_cards,
                "mindmap": t.include_mindmap,
                "report": t.include_report,
            },
        }
        for t in TEMPLATES.values()
    ]


def create_custom_template(
    name: str,
    description: str,
    num_keypoints: int = 5,
    num_qa_pairs: int = 5,
    include_transcript: bool = True,
    include_audio_overview: bool = True,
    include_knowledge_cards: bool = True,
    include_mindmap: bool = True,
    include_report: bool = True,
) -> TemplateConfig:
    """创建自定义模板"""
    return TemplateConfig(
        name=name,
        description=description,
        template_type=TemplateType.STANDARD,  # 自定义模板使用标准类型
        num_keypoints=num_keypoints,
        num_qa_pairs=num_qa_pairs,
        include_transcript=include_transcript,
        include_audio_overview=include_audio_overview,
        include_knowledge_cards=include_knowledge_cards,
        include_mindmap=include_mindmap,
        include_report=include_report,
    )
