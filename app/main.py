from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.resume_match.router import router as resume_match_router
from app.modules.skill_gap.router import router as skill_gap_router
from app.modules.candidate_ranking.router import router as ranking_router
from app.modules.interview_questions.router import router as interview_router

app = FastAPI(
    title="HR Recruitment AI Service",
    version="1.0.0"
)

# ✅ ADD CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "AI service is running"}

app.include_router(resume_match_router)
app.include_router(skill_gap_router)
app.include_router(ranking_router)
app.include_router(interview_router)
