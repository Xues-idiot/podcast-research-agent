"""JSON格式化API"""

from fastapi import APIRouter

from echo.research.json_formatter import get_json_formatter


router = APIRouter(prefix="/api/json", tags=["json"])


@router.post("/format")
async def format_json(data: str, indent: int = 2):
    return {"result": get_json_formatter().format(data, indent)}


@router.post("/minify")
async def minify_json(data: str):
    return {"result": get_json_formatter().minify(data)}


@router.post("/validate")
async def validate_json(data: str):
    return get_json_formatter().validate(data)