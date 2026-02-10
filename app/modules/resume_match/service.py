import json
from fastapi import HTTPException
from app.core.llm_client import GeminiClient
from .schema import ResumeMatchRequest, ResumeMatchResponse
from .prompt import build_resume_match_prompt

llm = GeminiClient()


def extract_json(text: str) -> dict:
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except Exception:
        raise ValueError(f"Invalid JSON from LLM:\n{text}")


def resume_jd_match(request: ResumeMatchRequest) -> ResumeMatchResponse:
    try:
        prompt = build_resume_match_prompt(request.resume_text, request.job_description)
        raw_text = llm.generate(prompt)

        print("\n===== GEMINI RAW OUTPUT =====\n", raw_text)

        data = extract_json(raw_text)

        # Ensure correct types
        data["match_score"] = int(data.get("match_score", 0))

        return ResumeMatchResponse(**data)

    except Exception as e:
        print("🔥 Resume Match Error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
