import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_company_history(candidate):

    history = []

    for job in candidate.get("career_history", []):

        history.append({
            "company": job.get("company", ""),
            "industry": job.get("industry", ""),
            "title": job.get("title", ""),
            "description": job.get("description", "")
        })

    prompt = f"""
You are an expert technical recruiter.

Analyze this candidate's career history.

Career History:

{json.dumps(history, indent=2)}

Answer ONLY in JSON.

Return:

{{
    "company_type":"Product | Consulting | Mixed",

    "reason":"",

    "score":-5 to 5
}}

Rules:

- Look at the ENTIRE career.

- Do NOT classify only by company names.

- If the candidate mainly built products,
  classify as Product.

- If the candidate mainly delivered consulting/client projects,
  classify as Consulting.

- If both,
  classify as Mixed.

Return JSON only.
"""

    response = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    return json.loads(
        response.choices[0].message.content
    )