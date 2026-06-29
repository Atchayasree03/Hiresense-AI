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
    You are an ATS Job Description Parser.

    Extract structured information from the Job Description.

    IMPORTANT RULES:

    1. Return ONLY valid JSON.
    2. Do NOT explain anything.
    3. Do NOT add markdown.
    4. Normalize every skill name.
    5. Remove adjectives like:
    - Advanced
    - Strong
    - Expert
    - Excellent
    - Good
    - Basic
    - Proficient
    6. Keep only the canonical skill name.

    Examples:

    Advanced Python -> Python
    Strong SQL -> SQL
    Expert TensorFlow -> TensorFlow
    Excellent PyTorch -> PyTorch
    Basic Java -> Java

    Do NOT invent skills.

    If a skill is not explicitly mentioned,
    DO NOT include it.

    Separate required skills and preferred skills.

    Return exactly this JSON format:

    {{
    "role": "",
    "required_skills": [],
    "preferred_skills": [],
    "experience_years": 0,
    "responsibilities": []
    }}

    Job Description:

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