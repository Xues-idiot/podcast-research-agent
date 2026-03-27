"""信用卡API"""

from fastapi import APIRouter

from echo.research.credit_card import get_credit_card_tool


router = APIRouter(prefix="/api/credit_card", tags=["credit_card"])


@router.post("/mask")
async def mask(card_number: str):
    return {"result": get_credit_card_tool().mask(card_number)}


@router.post("/validate")
async def validate(card_number: str):
    return {"valid": get_credit_card_tool().validate_luhn(card_number)}