from pydantic import BaseModel
from typing import List


class InterviewQuestionRequest(BaseModel):
    resume_text: str
    job_description: str


class InterviewQuestionResponse(BaseModel):
    technical_questions: List[str]
    practical_tasks: List[str]
    behavioral_questions: List[str]
