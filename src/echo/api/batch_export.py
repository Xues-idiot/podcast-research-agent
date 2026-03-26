"""批量导出API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.exporters.all_formats import get_batch_exporter


router = APIRouter(prefix="/api/export", tags=["export"])


class BatchExportRequest(BaseModel):
    """批量导出请求"""
    data: dict
    base_name: str
    formats: list = ["json", "markdown", "csv", "txt"]


@router.post("/batch")
async def batch_export(request: BatchExportRequest):
    """批量导出多种格式

    Args:
        request: 导出请求

    Returns:
        导出的文件路径
    """
    exporter = get_batch_exporter()
    paths = exporter.export_all_formats(
        data=request.data,
        base_name=request.base_name,
        include_formats=request.formats,
    )
    return {"files": paths, "count": len(paths)}


@router.post("/json")
async def export_json(data: dict, filename: str):
    """导出JSON

    Args:
        data: 数据
        filename: 文件名

    Returns:
        文件路径
    """
    exporter = get_batch_exporter()
    path = exporter._export_json(data, filename)
    return {"path": path}


@router.post("/markdown")
async def export_markdown(data: dict, filename: str):
    """导出Markdown

    Args:
        data: 数据
        filename: 文件名

    Returns:
        文件路径
    """
    exporter = get_batch_exporter()
    path = exporter._export_markdown(data, filename)
    return {"path": path}
