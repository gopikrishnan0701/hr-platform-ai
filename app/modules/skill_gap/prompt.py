def build_skill_gap_prompt(resume: str, jd: str) -> str:
    return f"""
You are an AI career advisor.

Compare the RESUME and JOB DESCRIPTION below.

RESUME:
{resume}

JOB DESCRIPTION:
{jd}

TASK:
Identify the candidate's skill gaps.

Return ONLY valid JSON in this format:

{{
  "technical_gaps": [string],
  "tools_missing": [string],
  "experience_gaps": [string],
  "learning_recommendations": [string]
}}
"""
