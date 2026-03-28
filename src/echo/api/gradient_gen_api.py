"""渐变生成API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.gradient_gen import get_gradient_gen_tool


router = APIRouter(prefix="/api/gradient-gen", tags=["gradient-gen"])


class GradientRequest(BaseModel):
    color1: str
    color2: str
    steps: int = 5


@router.post("/linear")
async def linear_gradient(request: GradientRequest):
    tool = get_gradient_gen_tool()
    return {"result": tool.linear_gradient(request.color1, request.color2, request.steps)}