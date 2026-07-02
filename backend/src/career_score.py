from difflib import SequenceMatcher
from src.candidate_evidence import extract_candidate_evidence

def normalize(text):
    return str(text).lower().strip()


def similarity(a, b):
    return SequenceMatcher(
        None,
        normalize(a),
        normalize(b)
    ).ratio()


def extract_candidate_profile(candidate):

    profile = {}

    profile["headline"] = candidate["profile"].get(
        "headline",
        ""
    )

    profile["summary"] = candidate["profile"].get(
        "summary",
        ""
    )

    profile["experience"] = candidate["profile"].get(
        "years_of_experience",
        0
    )

    profile["skills"] = [
        skill["name"]
        for skill in candidate.get(
            "skills",
            []
        )
    ]

    profile["projects"] = ""

    for job in candidate.get(
        "career_history",
        []
    ):

        profile["projects"] += (
            job.get(
                "title",
                ""
            )
            + " "
        )

        profile["projects"] += (
            job.get(
                "description",
                ""
            )
            + " "
        )

    profile["education"] = ""

    for edu in candidate.get(
        "education",
        []
    ):

        profile["education"] += (
            edu.get(
                "degree",
                ""
            )
            + " "
        )

        profile["education"] += (
            edu.get(
                "field_of_study",
                ""
            )
            + " "
        )

    return profile


def score_required_skills(
    candidate_profile,
    required_skills
):

    matched = []

    score = 0

    if len(required_skills) == 0:
        return 40, []

    per_skill = 40 / len(required_skills)

    searchable = " ".join([
        candidate_profile["headline"],
        candidate_profile["summary"],
        " ".join(candidate_profile["projects"]),
        " ".join(candidate_profile["skills"])
    ]).lower()

    for skill in required_skills:

        if normalize(skill) in searchable:

            matched.append(skill)

            score += per_skill

    return round(score, 2), matched


def score_preferred_skills(
    candidate_profile,
    preferred_skills
):

    matched = []

    score = 0

    if len(preferred_skills) == 0:
        return 15, []

    per_skill = 15 / len(preferred_skills)

    searchable = " ".join([
        candidate_profile["headline"],
        candidate_profile["summary"],
        " ".join(candidate_profile["projects"]),
        " ".join(candidate_profile["skills"])
    ]).lower()

    for skill in preferred_skills:

        if normalize(skill) in searchable:

            matched.append(skill)

            score += per_skill

    return round(score, 2), matched


def score_experience(
    candidate_profile,
    required_exp
):

    years = candidate_profile["experience"]

    if required_exp == 0:

        return 20

    if years >= required_exp:

        return 20

    return round(
        (years / required_exp) * 20,
        2
    )


def score_role(
    candidate_profile,
    role
):

    if similarity(
        candidate_profile["headline"],
        role
    ) > 0.55:

        return 10

    return 0


def score_projects(
    candidate_profile,
    required_skills
):

    project = normalize(
        candidate_profile["projects"]
    )

    matched = 0

    for skill in required_skills:

        if normalize(skill) in project:

            matched += 1

    if len(required_skills) == 0:

        return 10

    return round(
        (matched / len(required_skills)) * 10,
        2
    )


def score_education(
    candidate_profile
):

    edu = normalize(
        candidate_profile["education"]
    )

    keywords = [
        "computer science",
        "data science",
        "artificial intelligence",
        "machine learning",
        "statistics",
        "mathematics"
    ]

    for k in keywords:

        if k in edu:

            return 5

    return 0

def score_core_competencies(
    evidence,
    intent
):

    score = 0

    competencies = intent.get(
        "core_competencies",
        []
    )

    if "Search Systems" in competencies:

        if evidence["retrieval"]:

            score += 5

    if "Machine Learning" in competencies:

        if evidence["production_ml"]:

            score += 5

    if "Generative AI" in competencies:

        if (
            evidence["retrieval"]
            or
            evidence["production_ml"]
        ):

            score += 5

    return score


def calculate_career_score(
    candidate,
    parsed_jd
):

    profile = extract_candidate_profile(
        candidate
    )

    evidence = extract_candidate_evidence(
    candidate
)

    required_score, matched_required = (
        score_required_skills(
            profile,
            parsed_jd["required_skills"]
        )
    )

    preferred_score, matched_preferred = (
        score_preferred_skills(
            profile,
            parsed_jd["preferred_skills"]
        )
    )

    experience_score = score_experience(
        profile,
        parsed_jd["experience_years"]
    )

    role_score = score_role(
        profile,
        parsed_jd["role"]
    )

    project_score = score_projects(
        profile,
        parsed_jd["required_skills"]
    )

    education_score = score_education(
        profile
    )

    competency_score = score_core_competencies(
        evidence,
        parsed_jd
    )

    total = (
    required_score +
    preferred_score +
    experience_score +
    role_score +
    project_score +
    education_score +
    competency_score
)

    return {
        "career_score": round(total, 2),

        "matched_required_skills":
        matched_required,

        "matched_preferred_skills":
        matched_preferred
    }