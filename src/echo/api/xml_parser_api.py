"""XML解析API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.xml_parser import get_xml_parser_tool


router = APIRouter(prefix="/api/xml-parser", tags=["xml-parser"])


class ParseRequest(BaseModel):
    xml_str: str


@router.post("/parse")
async def parse(request: ParseRequest):
    tool = get_xml_parser_tool()
    result = tool.parse(request.xml_str)
    if result:
        return {"result": result}
    return {"error": "Invalid XML"}