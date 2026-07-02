import os
import json
from urllib import response

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("GEMINI_API_KEY")
)

def reason_candidate(
    jd_intent,
    candidate
):
    prompt = f"""
You are a Principal Technical Recruiter with 15 years of hiring experience.

Your task is NOT to compare keywords.

Your task is to understand whether the candidate has demonstrated the capability to perform this role.

========================
JOB REQUIREMENTS
========================

{json.dumps(jd_intent, indent=2)}

========================
CANDIDATE PROFILE
========================

{json.dumps(candidate, indent=2)}

========================

Evaluate the candidate exactly like a human recruiter.

Think carefully.

Consider:

1. Career progression.

2. Types of projects built.

3. Production engineering experience.

4. Equivalent technologies.

5. Transferable skills.

6. Domain expertise.

7. Leadership experience.

8. Product vs Service company background.

9. Recruitability.

Do NOT reject candidates because they don't have exact keywords.

Infer equivalent technologies.

Infer hidden strengths.

Infer weaknesses.

If someone built Elasticsearch, FAISS or OpenSearch,
understand they have Retrieval experience.

If someone built Recommendation Systems,
understand they have Ranking experience.

If someone deployed ML models,
understand they have Production ML experience.

Your reasoning should explain WHY the candidate matches.

Return ONLY JSON.

Format:

{
    "match_score":0,

    "hire_decision":"Strong Match / Good Match / Weak Match",

    "strengths":[],

    "weaknesses":[],

    "missing_skills":[],

    "career_evidence":[],

    "reasoning":""
}
"""
        
    response = client.chat.completions.create(

            model="meta/llama-3.1-8b-instruct",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0
        )
            
    text = response.choices[0].message.content

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    start = text.find("{")
    end = text.rfind("}")

    parsed = json.loads(
            text[start:end+1]
        )

    return parsed