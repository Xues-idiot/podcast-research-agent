"""单位转换API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.units_convert import get_units_convert_tool


router = APIRouter(prefix="/api/units-convert", tags=["units-convert"])


@router.post("/length/mm-to-cm")
async def mm_to_cm(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.length_mm_to_cm(request.get("mm", 0))}


@router.post("/length/cm-to-m")
async def cm_to_m(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.length_cm_to_m(request.get("cm", 0))}


@router.post("/length/m-to-km")
async def m_to_km(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.length_m_to_km(request.get("m", 0))}


@router.post("/length/inch-to-cm")
async def inch_to_cm(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.length_inch_to_cm(request.get("inch", 0))}


@router.post("/length/foot-to-m")
async def foot_to_m(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.length_foot_to_m(request.get("foot", 0))}


@router.post("/length/mile-to-km")
async def mile_to_km(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.length_mile_to_km(request.get("mile", 0))}


@router.post("/weight/g-to-kg")
async def g_to_kg(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.weight_g_to_kg(request.get("g", 0))}


@router.post("/weight/kg-to-t")
async def kg_to_t(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.weight_kg_to_t(request.get("kg", 0))}


@router.post("/weight/lb-to-kg")
async def lb_to_kg(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.weight_lb_to_kg(request.get("lb", 0))}


@router.post("/weight/oz-to-g")
async def oz_to_g(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.weight_oz_to_g(request.get("oz", 0))}


@router.post("/temperature/c-to-f")
async def c_to_f(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.temperature_c_to_f(request.get("c", 0))}


@router.post("/temperature/f-to-c")
async def f_to_c(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.temperature_f_to_c(request.get("f", 0))}


@router.post("/temperature/c-to-k")
async def c_to_k(request: BaseModel):
    tool = get_units_convert_tool()
    return {"result": tool.temperature_c_to_k(request.get("c", 0))}