"""表格格式API"""

from fastapi import APIRouter

from echo.research.textrunner import get_table_formatter


router = APIRouter(prefix="/api/table", tags=["table"])


@router.post("/csv")
async def to_csv(headers: list[str], rows: list[list[str]]):
    return {"result": get_table_formatter().to_csv_table(headers, rows)}


@router.post("/markdown")
async def to_markdown(headers: list[str], rows: list[list[str]]):
    return {"result": get_table_formatter().to_markdown_table(headers, rows)}


@router.post("/tsv")
async def to_tsv(headers: list[str], rows: list[list[str]]):
    return {"result": get_table_formatter().to_tsv_table(headers, rows)}