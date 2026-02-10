import json
from app.core.llm_client import GeminiClient
from .schema import InterviewQuestionRequest, InterviewQuestionResponse
from .prompt import build_interview_prompt

llm = GeminiClient()


def extract_json(text: str) -> dict:
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except Exception:
        raise ValueError(f"Invalid JSON from LLM:\n{text}")


def generate_questions(request: InterviewQuestionRequest) -> InterviewQuestionResponse:
    prompt = build_interview_prompt(request.resume_text, request.job_description)
    raw_text = llm.generate(prompt)

    try:
        data = extract_json(raw_text)

        return InterviewQuestionResponse(**data)

    except Exception as e:
        print("⚠️ Interview Question Fallback:", str(e))
        return InterviewQuestionResponse(
            technical_questions=[
                "Explain how FastAPI handles asynchronous requests",
                "How would you design a REST API for a job portal?"
            ],
            practical_tasks=[
                "Build a simple FastAPI endpoint that connects to MongoDB",
                "Write a Dockerfile for a Python backend service"
            ],
            behavioral_questions=[
                "Describe a challenging backend bug you solved",
                "How do you ensure code quality in a team project?"
            ]
        )
