from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def reason_candidate(jd_intent, candidate):

    profile = candidate["profile"]

    headline = profile.get("headline", "")

    summary = profile.get("summary", "")

    skills = " ".join([
        skill["name"]
        for skill in candidate.get("skills", [])
    ])

    experience = profile.get(
        "years_of_experience",
        0
    )

    text = f"""
    {headline}

    {summary}

    {skills}
    """

    jd_text = " ".join(
        jd_intent["required_skills"]
    )

    jd_embedding = model.encode(
        jd_text,
        normalize_embeddings=True
    )

    candidate_embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    match_score = round(
        similarity * 100,
        2
    )

    if match_score >= 75:
        decision = "Strong Match"

    elif match_score >= 60:
        decision = "Good Match"

    else:
        decision = "Weak Match"

    matched_skills = []

    searchable = text.lower()

    for skill in jd_intent["required_skills"]:

        if skill.lower() in searchable:

            matched_skills.append(skill)

    reasoning = (
        f"The candidate has {experience} years of experience. "
        f"Semantic similarity between the job description and candidate profile is "
        f"{match_score}%. "
        f"Matched skills include "
        f"{', '.join(matched_skills[:6])}."
    )

    return {

        "match_score": match_score,

        "hire_decision": decision,

        "strengths": matched_skills,

        "weaknesses": [],

        "missing_skills": [],

        "career_evidence": [],

        "reasoning": reasoning

    }