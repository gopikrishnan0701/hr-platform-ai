from fastapi import APIRouter
from .schema import SkillGapRequest, SkillGapResponse
from .service import analyze_skill_gap

router = APIRouter(
    prefix="/api/ai",
    tags=["Skill Gap Analysis"]
)

@router.post("/skill-gap", response_model=SkillGapResponse)
def skill_gap_analysis(request: SkillGapRequest):
    return analyze_skill_gap(request)
