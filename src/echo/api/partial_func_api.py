"""偏函数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.partial_func import get_partial_func_tool


router = APIRouter(prefix="/api/partial-func", tags=["partial-func"])


class PartialRequest(BaseModel):
    func_name: str
    args: list = []
    kwargs: dict = {}


@router.post("/create")
async def create_partial(request: PartialRequest):
    tool = get_partial_func_tool()
    return {"message": "Partial function configured", "func": request.func_name}