"""单位换算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.unit_converter import get_unit_converter_tool


router = APIRouter(prefix="/api/unit-converter", tags=["unit-converter"])


class ConvertRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str


@router.post("/convert")
async def convert(request: ConvertRequest):
    tool = get_unit_converter_tool()
    result = tool.convert(request.value, request.from_unit, request.to_unit)
    return {"result": result}