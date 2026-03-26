"""导入API - 从外部平台导入播客"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.importer import get_podcast_importer


router = APIRouter(prefix="/api/import", tags=["import"])


class ImportRequest(BaseModel):
    """导入请求"""
    url: str


@router.post("/")
async def import_podcast(request: ImportRequest):
    """导入播客

    Args:
        request: 导入请求

    Returns:
        导入的播客信息
    """
    importer = get_podcast_importer()
    podcast = await importer.import_from_url(request.url)
    return podcast.__dict__


@router.get("/")
async def list_imports():
    """列出所有导入记录

    Returns:
        导入列表
    """
    importer = get_podcast_importer()
    imports = importer.get_imports()
    return {
        "imports": [imp.__dict__ for imp in imports],
        "count": len(imports),
    }


@router.get("/{import_id}")
async def get_import(import_id: str):
    """获取导入详情

    Args:
        import_id: 导入ID

    Returns:
        导入详情
    """
    importer = get_podcast_importer()
    podcast = importer.get_import(import_id)
    if not podcast:
        raise HTTPException(status_code=404, detail="Import not found")
    return podcast.__dict__


@router.delete("/{import_id}")
def delete_import(import_id: str):
    """删除导入记录

    Args:
        import_id: 导入ID

    Returns:
        操作结果
    """
    importer = get_podcast_importer()
    if not importer.delete_import(import_id):
        raise HTTPException(status_code=404, detail="Import not found")
    return {"status": "deleted", "import_id": import_id}


@router.get("/platforms/detect")
async def detect_platform(url: str):
    """检测URL平台

    Args:
        url: 播客URL

    Returns:
        平台信息
    """
    importer = get_podcast_importer()
    platform = importer.detect_platform(url)
    return {
        "url": url,
        "platform": platform,
        "supported": platform is not None,
    }
