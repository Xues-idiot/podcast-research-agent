"""CSV转换API"""

from fastapi import APIRouter

from echo.research.csv_converter import get_csv_converter


router = APIRouter(prefix="/api/csv", tags=["csv"])


@router.post("/to")
async def to_csv(data: list[dict], headers: list[str] = None):
    return {"result": get_csv_converter().to_csv(data, headers)}


@router.post("/from")
async def from_csv(csv_str: str):
    return {"data": get_csv_converter().from_csv(csv_str)}


@router.post("/to_tsv")
async def to_tsv(data: list[dict]):
    return {"result": get_csv_converter().to_tsv(data)}