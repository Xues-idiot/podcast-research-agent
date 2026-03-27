"""电话号码API"""

from fastapi import APIRouter

from echo.research.phone_formatter import get_phone_formatter


router = APIRouter(prefix="/api/phone", tags=["phone"])


@router.post("/format_cn")
async def format_cn(phone: str):
    return {"result": get_phone_formatter().format_cn(phone)}


@router.post("/validate_cn")
async def validate_cn(phone: str):
    return {"valid": get_phone_formatter().validate_cn_mobile(phone)}