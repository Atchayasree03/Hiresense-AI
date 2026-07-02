def extract_intent(parsed_jd):

    required = parsed_jd.get(
        "required_skills",
        []
    )

    preferred = parsed_jd.get(
        "preferred_skills",
        []
    )

    role = parsed_jd.get(
        "role",
        ""
    )

    responsibilities = parsed_jd.get(
        "responsibilities",
        []
    )

    intent = {

        "role": role,

        "required_skills": required,

        "preferred_skills": preferred,

        "experience_years":
        parsed_jd.get(
            "experience_years",
            0
        ),

        "responsibilities":
        responsibilities,

        "core_competencies": [],

        "domain": "",

        "seniority": ""
    }

    text = (
        role
        + " "
        + " ".join(required)
        + " "
        + " ".join(responsibilities)
    ).lower()

    if any(
        x in text
        for x in [
            "retrieval",
            "search",
            "ranking",
            "recommendation"
        ]
    ):

        intent["core_competencies"].append(
            "Search Systems"
        )

    if any(
        x in text
        for x in [
            "llm",
            "rag",
            "langchain",
            "vector",
            "embedding"
        ]
    ):

        intent["core_competencies"].append(
            "Generative AI"
        )

    if any(
        x in text
        for x in [
            "tensorflow",
            "pytorch",
            "machine learning",
            "deep learning"
        ]
    ):

        intent["core_competencies"].append(
            "Machine Learning"
        )

    if any(
        x in text
        for x in [
            "backend",
            "fastapi",
            "django",
            "flask"
        ]
    ):

        intent["domain"] = "Backend"

    elif any(
        x in text
        for x in [
            "frontend",
            "react",
            "angular"
        ]
    ):

        intent["domain"] = "Frontend"

    elif any(
        x in text
        for x in [
            "data scientist",
            "machine learning",
            "ai engineer"
        ]
    ):

        intent["domain"] = "AI"

    if any(
        x in role.lower()
        for x in [
            "senior",
            "lead",
            "principal"
        ]
    ):

        intent["seniority"] = "Senior"

    else:

        intent["seniority"] = "Mid"

    return intent