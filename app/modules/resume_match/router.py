from fastapi import APIRouter
from .schema import ResumeMatchRequest, ResumeMatchResponse
from .service import resume_jd_match

router = APIRouter(
    prefix="/api/ai",
    tags=["Resume Matching"]
)

@router.post("/resume-match", response_model=ResumeMatchResponse)
def resume_match(request: ResumeMatchRequest):
    return resume_jd_match(request)
