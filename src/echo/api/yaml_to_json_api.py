"""YAML转JSON API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.yaml_to_json import get_yaml_to_json_tool


router = APIRouter(prefix="/api/yaml-to-json", tags=["yaml-to-json"])


class ConvertRequest(BaseModel):
    yaml_str: str


@router.post("/convert")
async def convert(request: ConvertRequest):
    tool = get_yaml_to_json_tool()
    return {"json": tool.convert(request.yaml_str)}