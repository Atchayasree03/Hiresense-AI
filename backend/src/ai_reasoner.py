import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_reason(
    candidate,
    matched_skills,
    jd_text,
    company_analysis=None
):

    headline = (
        candidate["profile"]
        .get(
            "headline",
            ""
        )
    )

    summary = (
        candidate["profile"]
        .get(
            "summary",
            ""
        )
    )

    candidate_skills = []

    for skill in candidate.get(
        "skills",
        []
    ):
        candidate_skills.append(
            skill.get(
                "name",
                ""
            )
        )

    experience = (
        candidate["profile"]
        .get(
            "years_of_experience",
            0
        )
    )

    career_history = ""

    for job in candidate.get(
        "career_history",
        []
    ):

        career_history += (
            f"Title: {job.get('title', '')}\n"
        )

        career_history += (
            f"Description: {job.get('description', '')}\n\n"
        )

    prompt = f"""
You are an expert recruiter.

Analyze the candidate against the Job Description.

Generate a professional hiring summary.

JOB DESCRIPTION:
{jd_text}

CANDIDATE HEADLINE:
{headline}

YEARS OF EXPERIENCE:
{experience}

MATCHED SKILLS:
{', '.join(matched_skills)}

CANDIDATE SKILLS:
{', '.join(candidate_skills)}

PROFESSIONAL SUMMARY:
{summary}

CAREER HISTORY:
{career_history}


Write a concise recruiter-style assessment.

Requirements:
- Maximum 4 sentences
- Mention matched skills
- Mention experience
- Mention career relevance
- Explain why candidate is suitable
- Professional HR tone
- No bullet points

Mention:
- Why the candidate matches this role.
- Skills relevant to the JD.
- Career progression.
- Company background.
- Whether the candidate has product, consulting, or mixed experience.
- Production or engineering experience if available.

Do not mention scores.

"""
    

    try:

        response = (
            client.chat.completions.create(
                model="meta/llama-3.1-8b-instruct",
                messages=[
                    {
                        "role": "system",
                        "content":
                        (
                            "You are an expert recruiter "
                            "who evaluates candidates "
                            "against job descriptions."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=200
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

    except Exception as e:

        return (
            f"AI Summary unavailable: {str(e)}"
        )


if __name__ == "__main__":

    from candidate_mapper import get_candidate

    candidate = get_candidate(
        790
    )

    matched_skills = [
        "Python",
        "SQL",
        "TensorFlow"
    ]

    jd_text = """
    Data Scientist

    Responsibilities:
    Build predictive models.
    Analyze large datasets.

    Required Skills:
    Python
    SQL
    TensorFlow
    PyTorch

    Experience:
    3+ years
    """

    summary = generate_ai_reason(
        candidate,
        matched_skills,
        jd_text
    )

    print("\nAI SUMMARY:\n")
    print(summary)