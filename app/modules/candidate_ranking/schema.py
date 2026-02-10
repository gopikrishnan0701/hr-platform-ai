from pydantic import BaseModel
from typing import List


class CandidateInput(BaseModel):
    name: str
    match_score: int
    missing_skills: List[str]
    experience_gaps: List[str]


class RankingRequest(BaseModel):
    candidates: List[CandidateInput]


class RankedCandidate(BaseModel):
    name: str
    final_score: float
    rank: int


class RankingResponse(BaseModel):
    ranked_candidates: List[RankedCandidate]
