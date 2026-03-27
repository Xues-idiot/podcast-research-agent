"""LR解析器API"""

from fastapi import APIRouter

from echo.research.lr_parser import get_lr_parser


router = APIRouter(prefix="/api/lr-parser", tags=["lr-parser"])


@router.post("/parse")
async def parse(tokens: list, grammar: dict):
    """解析"""
    tool = get_lr_parser()
    return {"result": tool.parse(tokens, grammar)}
