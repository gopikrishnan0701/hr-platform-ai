def build_resume_match_prompt(resume: str, jd: str) -> str:
    return f"""
You are an AI recruitment engine.

Compare the RESUME and JOB DESCRIPTION below.

RESUME:
{resume}

JOB DESCRIPTION:
{jd}

TASK:
- Score the match from 0 to 100
- Extract matching skills
- Extract missing skills
- Provide a short professional explanation

RULES:
- Respond ONLY in valid JSON
- Do NOT include markdown
- Do NOT include explanations outside JSON

JSON FORMAT:
{{
  "match_score": number,
  "summary": string,
  "matched_skills": [string],
  "missing_skills": [string],
  "reasoning": string
}}
"""
