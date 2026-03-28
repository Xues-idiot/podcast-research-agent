"""CSV转JSON API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.csv_to_json import get_csv_to_json_tool


router = APIRouter(prefix="/api/csv-to-json", tags=["csv-to-json"])


class ConvertRequest(BaseModel):
    csv_str: str


@router.post("/convert")
async def convert(request: ConvertRequest):
    tool = get_csv_to_json_tool()
    return {"json": tool.convert(request.csv_str)}