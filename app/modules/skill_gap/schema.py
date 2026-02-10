from pydantic import BaseModel
from typing import List


class SkillGapRequest(BaseModel):
    resume_text: str
    job_description: str


class SkillGapResponse(BaseModel):
    technical_gaps: List[str]
    tools_missing: List[str]
    experience_gaps: List[str]
    learning_recommendations: List[str]
