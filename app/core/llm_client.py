from dotenv import load_dotenv
import os
import google.generativeai as genai
import re

# Load environment variables
load_dotenv()


class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

        if self.api_key:
            genai.configure(api_key=self.api_key)
            # Faster model
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            print("✅ Gemini AI Enabled")
        else:
            self.model = None
            print("⚠️ Gemini API key not found — Running in fallback mode")

  # 👈 add this at the TOP of the file with other imports

    def generate(self, prompt: str) -> str:
        if not self.model:
            return """{
  "match_score": 65,
  "summary": "Moderate backend match (AI disabled mode)",
  "matched_skills": ["Python", "FastAPI", "MongoDB"],
  "missing_skills": ["Docker", "AWS"],
  "reasoning": "Fallback response because Gemini API key is not configured yet."
}"""
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "max_output_tokens": 250,
                    "temperature": 0.2
                }
            )

            # ✅ Extract only JSON from Gemini response
            text = response.text.strip()
            json_match = re.search(r"\{.*\}", text, re.DOTALL)
            return json_match.group(0) if json_match else text

        except Exception as e:
            print("⚠ Gemini timeout/error:", e)
            return """{
  "match_score": 60,
  "summary": "AI timeout fallback",
  "matched_skills": [],
  "missing_skills": [],
  "reasoning": "Gemini API call timed out or failed."
}"""
