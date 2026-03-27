"""单位转换API"""

from fastapi import APIRouter

from echo.research.units_converter import get_units_converter


router = APIRouter(prefix="/api/units", tags=["units"])


@router.post("/length")
async def convert_length(value: float, from_unit: str, to_unit: str):
    return {"result": get_units_converter().length(value, from_unit, to_unit)}


@router.post("/weight")
async def convert_weight(value: float, from_unit: str, to_unit: str):
    return {"result": get_units_converter().weight(value, from_unit, to_unit)}


@router.post("/temperature")
async def convert_temperature(value: float, from_unit: str, to_unit: str):
    return {"result": get_units_converter().temperature(value, from_unit, to_unit)}