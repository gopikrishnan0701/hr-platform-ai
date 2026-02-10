def build_interview_prompt(resume: str, jd: str) -> str:
    return f"""
You are a senior technical interviewer.

Based on the candidate RESUME and JOB DESCRIPTION below, generate interview questions.

RESUME:
{resume}

JOB DESCRIPTION:
{jd}

Return ONLY valid JSON in this format:

{{
  "technical_questions": [string],
  "practical_tasks": [string],
  "behavioral_questions": [string]
}}
"""
