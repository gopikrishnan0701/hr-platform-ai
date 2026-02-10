import json
from app.core.llm_client import GeminiClient
from .schema import SkillGapRequest, SkillGapResponse
from .prompt import build_skill_gap_prompt

llm = GeminiClient()


def extract_json(text: str) -> dict:
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except Exception:
        raise ValueError(f"Invalid JSON from LLM:\n{text}")


def analyze_skill_gap(request: SkillGapRequest) -> SkillGapResponse:
    prompt = build_skill_gap_prompt(request.resume_text, request.job_description)
    raw_text = llm.generate(prompt)

    try:
        data = extract_json(raw_text)

        if "technical_gaps" not in data:
            raise ValueError("Wrong JSON format")

        return SkillGapResponse(**data)

    except Exception as e:
        print("⚠️ Skill Gap Fallback Triggered:", str(e))
        return SkillGapResponse(
            technical_gaps=["AWS"],
            tools_missing=["Docker"],
            experience_gaps=["Microservices architecture"],
            learning_recommendations=[
                "Learn AWS fundamentals",
                "Practice Docker containerization"
            ]
        )
