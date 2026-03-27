"""URL工具API"""

from fastapi import APIRouter

from echo.research.url_tool import get_url_tool


router = APIRouter(prefix="/api/url", tags=["url"])


@router.get("/parse")
async def parse_url(url: str):
    return get_url_tool().parse(url)


@router.get("/query_params")
async def get_query_params(url: str):
    return get_url_tool().get_query_params(url)


@router.post("/join")
async def join_urls(base: str, relative: str):
    return {"result": get_url_tool().join(base, relative)}