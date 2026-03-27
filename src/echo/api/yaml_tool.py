"""YAML工具API"""

from fastapi import APIRouter

from echo.research.yaml_tool import get_yaml_tool


router = APIRouter(prefix="/api/yaml", tags=["yaml"])


@router.post("/to_json")
async def to_json(yaml_str: str):
    return {"result": get_yaml_tool().to_json(yaml_str)}


@router.post("/from_json")
async def from_json(json_str: str):
    return {"result": get_yaml_tool().from_json(json_str)}