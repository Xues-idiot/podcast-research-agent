"""大小写转换API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.case_transform import get_case_transform_tool


router = APIRouter(prefix="/api/case-transform", tags=["case-transform"])


class TransformRequest(BaseModel):
    text: str


@router.post("/camel")
async def to_camel(request: TransformRequest):
    tool = get_case_transform_tool()
    return {"result": tool.to_camel_case(request.text)}


@router.post("/snake")
async def to_snake(request: TransformRequest):
    tool = get_case_transform_tool()
    return {"result": tool.to_snake_case(request.text)}


@router.post("/pascal")
async def to_pascal(request: TransformRequest):
    tool = get_case_transform_tool()
    return {"result": tool.to_pascal_case(request.text)}