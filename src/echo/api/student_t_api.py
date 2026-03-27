"""学生t分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.student_t import get_student_t


router = APIRouter(prefix="/api/student-t", tags=["student-t"])


class StudentTRequest(BaseModel):
    t: float
    df: int


@router.post("/pdf")
async def pdf(request: StudentTRequest):
    return {"result": get_student_t().pdf(request.t, request.df)}
