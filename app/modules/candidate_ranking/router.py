from fastapi import APIRouter
from .schema import RankingRequest, RankingResponse
from .service import rank_candidates

router = APIRouter(
    prefix="/api/ai",
    tags=["Candidate Ranking"]
)

@router.post("/rank-candidates", response_model=RankingResponse)
def rank(request: RankingRequest):
    return rank_candidates(request)
