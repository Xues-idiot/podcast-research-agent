"""JSON路径API"""

from fastapi import APIRouter

from echo.research.json_path import get_json_path


router = APIRouter(prefix="/api/json-path", tags=["json-path"])


@router.post("/get")
async def get(data: dict, path: str):
    """获取路径值"""
    tool = get_json_path()
    return {"value": tool.get(data, path)}
