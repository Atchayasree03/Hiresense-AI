import os
import json
from src.jd_validator import validate_skills
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("GEMINI_API_KEY")
)

def parse_jd(jd_text):

    prompt = f"""
        You are an expert technical recruiter.

        Analyze the following Job Description.

        Return ONLY valid JSON.

        Do NOT copy text blindly.

        Infer the recruiter's intent.

        Return this exact format:

        {{
        "role":"",
        "required_skills":[],
        "preferred_skills":[],
        "experience_years":0,
        "responsibilities":[],
        "core_competencies":[],
        "engineering_focus":[],
        "company_preference":"",
        "behavioral_preferences":[]
        }}

        Rules:

        - Separate required and preferred skills.
        - Infer hidden competencies.
        - Group similar technologies.
        - If Pinecone, FAISS, Weaviate appear → Retrieval Systems.
        - If TensorFlow, PyTorch appear → Machine Learning.
        - If NDCG, MRR appear → Ranking Evaluation.
        - Infer engineering focus.
        - Infer preferred company type.
        - Infer behavioral expectations.
        - Return JSON only.

        JD:

        {jd_text}
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

    # Find JSON boundaries
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError(f"No JSON found.\nResponse:\n{text}")

    json_text = text[start:end + 1]

    parsed = json.loads(json_text)

    parsed = validate_skills(
        parsed,
        jd_text
    )

    return parsed


jd_text = """
Data Scientist

Requirements:
Python
SQL
TensorFlow
PyTorch
Scikit-learn

3+ years experience
"""

parsed_jd = parse_jd(jd_text)

print(parsed_jd)