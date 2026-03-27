"""电话号码API"""

from fastapi import APIRouter

from echo.research.phone_tool import get_phone_tool


router = APIRouter(prefix="/api/phone", tags=["phone"])


@router.post("/validate")
async def validate(phone: str):
    """验证电话"""
    tool = get_phone_tool()
    return {"valid": tool.is_valid(phone)}


@router.post("/format")
async def format_phone(phone: str):
    """格式化电话"""
    tool = get_phone_tool()
    return {"formatted": tool.format(phone)}
