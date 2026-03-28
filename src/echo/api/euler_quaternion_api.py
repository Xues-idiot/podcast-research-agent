"""欧拉角四元数转换API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.euler_quaternion import get_euler_quaternion_tool


router = APIRouter(prefix="/api/euler-quaternion", tags=["euler-quaternion"])


class EulerToQuaternionRequest(BaseModel):
    euler: list[float]


class QuaternionToEulerRequest(BaseModel):
    q: list[float]


@router.post("/euler-to-quaternion")
async def euler_to_quaternion(request: EulerToQuaternionRequest):
    tool = get_euler_quaternion_tool()
    return {"result": tool.euler_to_quaternion(request.euler)}


@router.post("/quaternion-to-euler")
async def quaternion_to_euler(request: QuaternionToEulerRequest):
    tool = get_euler_quaternion_tool()
    return {"result": tool.quaternion_to_euler(request.q)}