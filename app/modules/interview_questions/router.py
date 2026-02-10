from fastapi import APIRouter
from .schema import InterviewQuestionRequest, InterviewQuestionResponse
from .service import generate_questions

router = APIRouter(
    prefix="/api/ai",
    tags=["Interview Question Generator"]
)

@router.post("/generate-questions", response_model=InterviewQuestionResponse)
def questions(request: InterviewQuestionRequest):
    return generate_questions(request)
