"""标签API - 自动标签生成"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.tags import get_auto_tagger


router = APIRouter(prefix="/api/tags", tags=["tags"])


class GenerateTagsRequest(BaseModel):
    """生成标签请求"""
    text: str = ""
    title: str = ""
    max_tags: int = 10


@router.post("/generate")
async def generate_tags(request: GenerateTagsRequest):
    """自动生成标签

    Args:
        request: 请求内容

    Returns:
        标签列表
    """
    tagger = get_auto_tagger()
    tags = tagger.generate_tags(
        text=request.text,
        title=request.title,
        max_tags=request.max_tags,
    )

    return {
        "tags": [
            {
                "name": tag.name,
                "count": tag.count,
                "source": tag.source,
            }
            for tag in tags
        ],
        "count": len(tags),
    }


@router.post("/entities")
async def extract_entities(text: str):
    """提取文本实体

    Args:
        text: 文本内容

    Returns:
        实体字典
    """
    tagger = get_auto_tagger()
    entities = tagger.extract_entities(text)
    return entities


@router.get("/keywords")
async def get_keyword_tags():
    """获取关键词标签分类

    Returns:
        关键词分类
    """
    from echo.research.tags import AutoTagger
    return {
        "categories": list(AutoTagger.KEYWORD_TAGS.keys()),
        "tags": AutoTagger.KEYWORD_TAGS,
    }
