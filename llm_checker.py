import os
import json
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("OPENROUTER_API_KEY")

LLM_API_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL_NAME = "qwen/qwen3-coder:free"

TIMEOUT = 120



# ------------------------------------------------
# PROMPTING THE LLM
# ------------------------------------------------

def build_prompt(resume_text: str, jd_text: str) -> str:
    return f"""
You are an ATS-style resume screening assistant.

Your task:
- compare the resume with the job description
- Evaluate skill match, experience relevance, and role suitablility
- Be objective and concise

Return ONLY valid JSON in the following format:
{{
    "candidate_name": "",
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "experience_summary": "",
    "final_verdict": "Strong Fit | Medium Fit | Weak Fit",
    "explanation": ""
}}

Rules:
- match_score must be between 0 and 100
- explanation must clearly justify the score
- Do not add any extra keys
- Do not include markdown or text outside JSON

Job Description:
\"\"\"
{jd_text}
\"\"\"

Resume:
\"\"\"
{resume_text}
\"\"\"
""".strip()

# ------------------------------------------------
# PARSING THE RESPONSE
# ------------------------------------------------

def parse_llm_response(content: str) -> Dict[str, Any]:
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON")
    
    required_keys = {
        "candidate_name",
        "match_score",
        "matched_skills",
        "missing_skills",
        "experience_summary",
        "final_verdict",
        "explanation"
    }
    if not required_keys.issubset(data.keys()):
        raise ValueError("LLM response missing required fields")
    return data

# ------------------------------------------------
# RESUME EVALUATING
# ------------------------------------------------

def evaluate_resume(resume_text: str,jd_text: str) -> Dict[str, Any]:
   if not LLM_API_KEY:
       raise RuntimeError("LLM_API_KEY not found in venv")

   prompt = build_prompt(resume_text, jd_text)

   headers = {
       "Authorization": f"Bearer {LLM_API_KEY}",
       "Content-Type": "application/json"
    }
   
   payload =  {
       "model": MODEL_NAME,
       "messages": [
           {"role": "system", "content": "You are a professional recruitment analyst."},
           {"role": "user", "content": prompt}
       ],
       "temperature": 0.2
   }

   response = requests.post(
       LLM_API_URL,
       headers=headers,
       json=payload,
       timeout=TIMEOUT
   )

   response.raise_for_status()

   raw_content = response.json()["choices"][0]["message"]["content"]

   return parse_llm_response(raw_content)