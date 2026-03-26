"""研究模板API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.templates import (
    TemplateType,
    get_template,
    list_templates,
    create_custom_template,
)


router = APIRouter(prefix="/api/templates", tags=["templates"])


class CustomTemplateRequest(BaseModel):
    """自定义模板请求"""
    name: str
    description: str
    num_keypoints: int = 5
    num_qa_pairs: int = 5
    include_transcript: bool = True
    include_audio_overview: bool = True
    include_knowledge_cards: bool = True
    include_mindmap: bool = True
    include_report: bool = True


@router.get("/")
async def get_templates():
    """获取所有可用模板

    Returns:
        模板列表
    """
    return {"templates": list_templates()}


@router.get("/{template_type}")
async def get_template_by_type(template_type: str):
    """获取指定模板

    Args:
        template_type: 模板类型

    Returns:
        模板配置
    """
    try:
        t_type = TemplateType(template_type)
        template = get_template(t_type)
        return {
            "type": template.template_type.value,
            "name": template.name,
            "description": template.description,
            "num_keypoints": template.num_keypoints,
            "num_qa_pairs": template.num_qa_pairs,
            "include_transcript": template.include_transcript,
            "include_audio_overview": template.include_audio_overview,
            "include_knowledge_cards": template.include_knowledge_cards,
            "include_mindmap": template.include_mindmap,
            "include_report": template.include_report,
            "custom_prompts": template.custom_prompts,
        }
    except ValueError:
        return {"error": f"Unknown template type: {template_type}"}


@router.post("/")
async def create_template(request: CustomTemplateRequest):
    """创建自定义模板

    Args:
        request: 自定义模板配置

    Returns:
        创建的模板
    """
    template = create_custom_template(
        name=request.name,
        description=request.description,
        num_keypoints=request.num_keypoints,
        num_qa_pairs=request.num_qa_pairs,
        include_transcript=request.include_transcript,
        include_audio_overview=request.include_audio_overview,
        include_knowledge_cards=request.include_knowledge_cards,
        include_mindmap=request.include_mindmap,
        include_report=request.include_report,
    )
    return {
        "type": template.template_type.value,
        "name": template.name,
        "description": template.description,
        "num_keypoints": template.num_keypoints,
        "num_qa_pairs": template.num_qa_pairs,
    }
