"""四元数乘法API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.quaternion_multiply import get_quaternion_multiply_tool


router = APIRouter(prefix="/api/quaternion-multiply", tags=["quaternion-multiply"])


class MultiplyRequest(BaseModel):
    q1: list[float]
    q2: list[float]


@router.post("/multiply")
async def multiply(request: MultiplyRequest):
    tool = get_quaternion_multiply_tool()
    return {"result": tool.multiply(request.q1, request.q2)}