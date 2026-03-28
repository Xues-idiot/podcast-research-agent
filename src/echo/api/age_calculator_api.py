"""年龄计算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.age_calculator import get_age_calculator_tool


router = APIRouter(prefix="/api/age-calculator", tags=["age-calculator"])


class BirthDateRequest(BaseModel):
    birth_date: str


@router.post("/calculate")
async def calculate(request: BirthDateRequest):
    tool = get_age_calculator_tool()
    return {"age": tool.calculate(request.birth_date)}


@router.post("/days-until")
async def days_until(request: BirthDateRequest):
    tool = get_age_calculator_tool()
    return {"days": tool.days_until_birthday(request.birth_date)}