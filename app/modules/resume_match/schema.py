from pydantic import BaseModel
from typing import List


class ResumeMatchRequest(BaseModel):
    resume_text: str
    job_description: str


class ResumeMatchResponse(BaseModel):
    match_score: int
    summary: str
    matched_skills: List[str]
    missing_skills: List[str]
    reasoning: str
