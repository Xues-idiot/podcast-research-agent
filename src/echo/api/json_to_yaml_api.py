"""JSON转YAML API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.json_to_yaml import get_json_to_yaml_tool


router = APIRouter(prefix="/api/json-to-yaml", tags=["json-to-yaml"])


class ConvertRequest(BaseModel):
    json_str: str


@router.post("/convert")
async def convert(request: ConvertRequest):
    tool = get_json_to_yaml_tool()
    return {"yaml": tool.convert(request.json_str)}