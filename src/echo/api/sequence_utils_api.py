"""序列工具API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List, Optional
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.sequence_utils import (
    generate_arithmetic_sequence,
    generate_geometric_sequence,
    generate_fibonacci_sequence,
    generate_prime_sequence,
    sequence_slice,
    sequence_index,
    sequence_count,
    sequence_reverse,
    sequence_find_all
)


class ArithmeticSequenceRequest(BaseModel):
    start: float = 0
    step: float = 1
    length: int = 10


class GeometricSequenceRequest(BaseModel):
    start: float = 1
    ratio: float = 2
    length: int = 10


class FibonacciRequest(BaseModel):
    length: int = 15


class PrimeSequenceRequest(BaseModel):
    length: int = 20


class SliceRequest(BaseModel):
    seq: List[Any]
    start: int = 0
    end: Optional[int] = None
    step: int = 1


class IndexRequest(BaseModel):
    seq: List[Any]
    value: Any
    start: int = 0


class CountRequest(BaseModel):
    seq: List[Any]
    value: Any


class ReverseRequest(BaseModel):
    seq: List[Any]


class FindAllRequest(BaseModel):
    seq: List[Any]
    value: Any


router = APIRouter(prefix="/api/sequence", tags=["sequence"])


@router.post("/arithmetic")
async def arithmetic_sequence(request: ArithmeticSequenceRequest) -> dict:
    return {"result": generate_arithmetic_sequence(request.start, request.step, request.length)}


@router.post("/geometric")
async def geometric_sequence(request: GeometricSequenceRequest) -> dict:
    return {"result": generate_geometric_sequence(request.start, request.ratio, request.length)}


@router.post("/fibonacci")
async def fibonacci_sequence(request: FibonacciRequest) -> dict:
    return {"result": generate_fibonacci_sequence(request.length)}


@router.post("/primes")
async def prime_sequence(request: PrimeSequenceRequest) -> dict:
    return {"result": generate_prime_sequence(request.length)}


@router.post("/slice")
async def seq_slice(request: SliceRequest) -> dict:
    return {"result": sequence_slice(request.seq, request.start, request.end, request.step)}


@router.post("/index")
async def seq_index(request: IndexRequest) -> dict:
    return {"result": sequence_index(request.seq, request.value, request.start)}


@router.post("/count")
async def seq_count(request: CountRequest) -> dict:
    return {"result": sequence_count(request.seq, request.value)}


@router.post("/reverse")
async def seq_reverse(request: ReverseRequest) -> dict:
    return {"result": sequence_reverse(request.seq)}


@router.post("/find-all")
async def seq_find_all(request: FindAllRequest) -> dict:
    return {"result": sequence_find_all(request.seq, request.value)}