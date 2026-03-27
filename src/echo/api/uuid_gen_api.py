"""UUID API"""

from fastapi import APIRouter

from echo.research.uuid_gen import get_uuid_gen


router = APIRouter(prefix="/api/uuid", tags=["uuid"])


@router.post("/generate")
async def generate():
    """生成UUID"""
    tool = get_uuid_gen()
    return {"uuid": tool.generate()}


@router.post("/validate")
async def validate(text: str):
    """验证UUID"""
    tool = get_uuid_gen()
    return {"valid": tool.validate(text)}
