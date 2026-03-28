"""路径工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.path_utils import path_join, path_split, path_basename, path_dirname, path_ext, path_stem, path_exists, path_is_file, path_is_dir, path_abs, path_norm


class PathRequest(BaseModel):
    path: str


class JoinRequest(BaseModel):
    parts: List[str]


router = APIRouter(prefix="/api/path", tags=["path"])


@router.post("/join")
async def join(request: JoinRequest) -> dict:
    return {"result": path_join(*request.parts)}


@router.post("/split")
async def split(request: PathRequest) -> dict:
    return {"result": path_split(request.path)}


@router.post("/basename")
async def basename(request: PathRequest) -> dict:
    return {"result": path_basename(request.path)}


@router.post("/dirname")
async def dirname(request: PathRequest) -> dict:
    return {"result": path_dirname(request.path)}


@router.post("/ext")
async def ext(request: PathRequest) -> dict:
    return {"result": path_ext(request.path)}


@router.post("/stem")
async def stem(request: PathRequest) -> dict:
    return {"result": path_stem(request.path)}


@router.post("/exists")
async def exists(request: PathRequest) -> dict:
    return {"result": path_exists(request.path)}


@router.post("/is-file")
async def is_file(request: PathRequest) -> dict:
    return {"result": path_is_file(request.path)}


@router.post("/is-dir")
async def is_dir(request: PathRequest) -> dict:
    return {"result": path_is_dir(request.path)}
