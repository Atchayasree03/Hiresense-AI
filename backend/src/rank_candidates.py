

from src.faiss_search import search_candidates
from src.candidate_mapper import get_candidate
from src.career_score import calculate_career_score
from src.behavior_score import calculate_behavior_score
from src.jd_parser import parse_jd
from src.explanation_engine import generate_explanation
from src.local_reasoner import generate_ai_reason
from src.jd_intent_engine import extract_intent

def rank_candidates(jd_text, top_k=100):

    parsed_jd = parse_jd(jd_text)
    
    
    jd_intent = extract_intent(parsed_jd)

    jd_skills = (
        parsed_jd["required_skills"]
        +
        parsed_jd["preferred_skills"]
    )

    jd_experience = (
        parsed_jd["experience_years"]
    )

    scores, indices = search_candidates(
        jd_text,
        top_k=300
    )

    ranked_candidates = []

    for semantic_score, idx in zip(
        scores[0],
        indices[0]
    ):

        candidate = get_candidate(idx)

        semantic_score = round(
            float(semantic_score) * 100,
            2
        )

        career = calculate_career_score(
            candidate,
            parsed_jd
        )

        career = calculate_career_score(
        candidate,
        jd_intent
    )

        career_score = career["career_score"]

        matched_skills = (
            career["matched_required_skills"] +
            career["matched_preferred_skills"]
        )

        behavior_score = (
            calculate_behavior_score(
                candidate
            )
        )

        match_score = (
            0.50 * semantic_score
            +
            0.40 * career_score
            +
            0.10 * behavior_score
        )

        if len(matched_skills) == 0:
            match_score *= 0.8

        match_score = round(
            match_score,
            2
        )

        # # Normalize score to 65-100
        # match_score = 65 + ((match_score - 60) / 15) * 35

        # match_score = max(0, min(match_score, 100))

        # match_score = round(match_score, 2)

        # reasons = generate_explanation(
        #     candidate,
        #     matched_skills,
        #     jd_experience
        # )

        ai_summary = generate_ai_reason(
            candidate,
            matched_skills,
            jd_text,
        )

        reasons = generate_explanation(
        candidate,
        matched_skills,
        jd_experience
)

        ranked_candidates.append({

    "candidate_id": candidate["candidate_id"],

    "headline": candidate["profile"].get("headline", ""),

    "years_of_experience": candidate["profile"].get(
        "years_of_experience",
        0
    ),

    "match_score": match_score,

    "semantic_score": semantic_score,

    "career_score": career_score,

    "behavior_score": behavior_score,

    "matched_skills": matched_skills,

    "reasons": reasons,

    "ai_summary": ai_summary

})
    ranked_candidates.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

   

    return ranked_candidates[:top_k]


if __name__ == "__main__":

    jd = """
Role Overview

We are seeking a Data Scientist to transform raw data into actionable insights.

Key Responsibilities

Clean Data:
Collect and prepare data from various sources.

Build Models:
Design and deploy machine learning algorithms.

Find Trends:
Conduct statistical analysis to uncover patterns.

Visualize Insights:
Create dashboards using Tableau or Power BI.

Share Findings:
Present data-driven solutions to business stakeholders.

Technical Requirements

Advanced Python
SQL
TensorFlow
PyTorch
Scikit-learn

Education:
Computer Science
Data Science
Mathematics

3+ years experience
"""

    candidates = rank_candidates(
        jd,
        top_k=10
    )

    print("\nTOP CANDIDATES\n")

    for rank, candidate in enumerate(
        candidates,
        start=1
    ):

        print(
            f"Rank #{rank}"
        )

        print(
            f"Candidate: {candidate['candidate_id']}"
        )

        print(
            f"Headline: {candidate['headline']}"
        )

        print(
            f"Experience: {candidate['years_of_experience']} years"
        )

        print(
            f"Semantic Score: {candidate['semantic_score']}"
        )

        print(
            f"Career Score: {candidate['career_score']}"
        )

        print(
            f"Behavior Score: {candidate['behavior_score']}"
        )

        print(
            f"Match Score: {candidate['match_score']}"
        )

        print("Reasons:")

        for reason in candidate["reasons"]:
            print(f"- {reason}")

        print(
            "\nMatched Skills:"
        )

        print(
            candidate["matched_skills"]
        )

        print(
            "\nAI Summary:"
        )

        print(
            candidate["ai_summary"]
        )

        print("-" * 80)