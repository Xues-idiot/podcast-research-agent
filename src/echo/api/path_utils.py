"""路径工具API"""

from fastapi import APIRouter

from echo.research.path_utils import get_path_utils


router = APIRouter(prefix="/api/path", tags=["path"])


@router.get("/extension")
async def get_extension(path: str):
    return {"extension": get_path_utils().get_extension(path)}


@router.get("/filename")
async def get_filename(path: str):
    return {"filename": get_path_utils().get_filename(path)}


@router.get("/basename")
async def get_basename(path: str):
    return {"basename": get_path_utils().get_basename(path)}


@router.post("/join")
async def join_paths(parts: list[str]):
    return {"path": get_path_utils().join(*parts)}