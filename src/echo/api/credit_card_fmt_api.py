"""信用卡格式化API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.credit_card_fmt import get_credit_card_fmt_tool


router = APIRouter(prefix="/api/credit-card-fmt", tags=["credit-card-fmt"])


class CardRequest(BaseModel):
    card_number: str


@router.post("/format")
async def format_card(request: CardRequest):
    tool = get_credit_card_fmt_tool()
    return {"result": tool.format(request.card_number)}


@router.post("/mask")
async def mask_card(request: CardRequest):
    tool = get_credit_card_fmt_tool()
    return {"result": tool.mask(request.card_number)}


@router.post("/type")
async def get_type(request: CardRequest):
    tool = get_credit_card_fmt_tool()
    return {"result": tool.get_type(request.card_number)}


@router.post("/validate")
async def validate(request: CardRequest):
    tool = get_credit_card_fmt_tool()
    return {"result": tool.validate_luhn(request.card_number)}