"""数据脱敏API"""

from fastapi import APIRouter

from echo.research.data_sanitizer import get_data_sanitizer


router = APIRouter(prefix="/api/sanitize", tags=["sanitize"])


@router.post("/email")
async def mask_email(email: str):
    return {"result": get_data_sanitizer().mask_email(email)}


@router.post("/phone")
async def mask_phone(phone: str):
    return {"result": get_data_sanitizer().mask_phone(phone)}


@router.post("/id_card")
async def mask_id_card(id_card: str):
    return {"result": get_data_sanitizer().mask_id_card(id_card)}