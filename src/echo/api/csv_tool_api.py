"""CSV工具API"""

from fastapi import APIRouter

from echo.research.csv_tool import get_csv_tool


router = APIRouter(prefix="/api/csv", tags=["csv"])


@router.post("/parse")
async def parse(text: str, delimiter: str = ","):
    """解析CSV"""
    tool = get_csv_tool()
    return {"data": tool.parse(text, delimiter)}


@router.post("/to-csv")
async def to_csv(data: list, delimiter: str = ","):
    """转CSV"""
    tool = get_csv_tool()
    return {"result": tool.to_csv(data, delimiter)}
