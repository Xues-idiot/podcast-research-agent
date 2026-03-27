"""角度转换API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.angle_converter import get_angle_converter


router = APIRouter(prefix="/api/angle-converter", tags=["angle-converter"])


class AngleRequest(BaseModel):
    degrees: float


@router.post("/to-radians")
async def to_radians(request: AngleRequest):
    return {"result": get_angle_converter().degrees_to_radians(request.degrees)}
