"""IP地址API"""

from fastapi import APIRouter

from echo.research.ip_tool import get_ip_tool


router = APIRouter(prefix="/api/ip", tags=["ip"])


@router.post("/validate_v4")
async def validate_ipv4(ip: str):
    return {"valid": get_ip_tool().is_valid_ipv4(ip)}


@router.post("/validate_v6")
async def validate_ipv6(ip: str):
    return {"valid": get_ip_tool().is_valid_ipv6(ip)}


@router.post("/to_int")
async def ip_to_int(ip: str):
    return {"result": get_ip_tool().ip_to_int(ip)}