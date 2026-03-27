"""角度API"""

from fastapi import APIRouter

from echo.research.angle_tool import get_angle_tool


router = APIRouter(prefix="/api/angle", tags=["angle"])


@router.post("/degrees-to-radians")
async def degrees_to_radians(degrees: float):
    return {"result": get_angle_tool().degrees_to_radians(degrees)}


@router.post("/radians-to-degrees")
async def radians_to_degrees(radians: float):
    return {"result": get_angle_tool().radians_to_degrees(radians)}


@router.post("/sin")
async def sin(degrees: float):
    return {"result": get_angle_tool().sin(degrees)}


@router.post("/cos")
async def cos(degrees: float):
    return {"result": get_angle_tool().cos(degrees)}