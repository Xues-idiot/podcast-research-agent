"""正则表达式API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.regex_utils import regex_match, regex_search, regex_find_all, regex_replace, regex_split, extract_numbers, extract_emails, is_valid_email, is_valid_phone, is_valid_url


class RegexRequest(BaseModel):
    pattern: str
    text: str


class ReplaceRequest(BaseModel):
    pattern: str
    text: str
    replacement: str


router = APIRouter(prefix="/api/regex", tags=["regex"])


@router.post("/match")
async def match(request: RegexRequest) -> dict:
    return {"result": regex_match(request.pattern, request.text)}


@router.post("/search")
async def search(request: RegexRequest) -> dict:
    return {"result": regex_search(request.pattern, request.text)}


@router.post("/find-all")
async def find_all(request: RegexRequest) -> dict:
    return {"result": regex_find_all(request.pattern, request.text)}


@router.post("/replace")
async def replace(request: ReplaceRequest) -> dict:
    return {"result": regex_replace(request.pattern, request.text, request.replacement)}


@router.post("/split")
async def split(request: RegexRequest) -> dict:
    return {"result": regex_split(request.pattern, request.text)}


@router.post("/extract-numbers")
async def numbers(request: RegexRequest) -> dict:
    return {"result": extract_numbers(request.text)}


@router.post("/extract-emails")
async def emails(request: RegexRequest) -> dict:
    return {"result": extract_emails(request.text)}
