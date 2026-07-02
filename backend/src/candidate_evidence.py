import re


def normalize(text):
    return str(text).lower().strip()


def extract_candidate_evidence(candidate):

    evidence = {}

    profile = candidate.get("profile", {})

    evidence["headline"] = profile.get(
        "headline",
        ""
    )

    evidence["summary"] = profile.get(
        "summary",
        ""
    )

    evidence["experience"] = profile.get(
        "years_of_experience",
        0
    )

    evidence["skills"] = [
        skill["name"]
        for skill in candidate.get(
            "skills",
            []
        )
    ]

    evidence["projects"] = []

    evidence["role_history"] = []

    evidence["industries"] = []

    evidence["companies"] = []

    project_text = ""

    for job in candidate.get(
        "career_history",
        []
    ):

        title = job.get(
            "title",
            ""
        )

        description = job.get(
            "description",
            ""
        )

        evidence["role_history"].append(
            title
        )

        evidence["projects"].append(
            description
        )

        evidence["industries"].append(
            job.get(
                "industry",
                ""
            )
        )

        evidence["companies"].append(
            job.get(
                "company",
                ""
            )
        )

        project_text += (
            title
            + " "
            + description
            + " "
        )

    text = normalize(
        project_text
        + evidence["summary"]
        + " "
        + " ".join(
            evidence["skills"]
        )
    )

    evidence["production_ml"] = any(
        word in text
        for word in [
            "production",
            "deployment",
            "serving",
            "mlops",
            "pipeline"
        ]
    )

    evidence["retrieval"] = any(
        word in text
        for word in [
            "retrieval",
            "search",
            "faiss",
            "elasticsearch",
            "opensearch",
            "vector",
            "embedding"
        ]
    )

    evidence["recommendation"] = any(
        word in text
        for word in [
            "recommendation",
            "ranking",
            "recommender",
            "matching"
        ]
    )

    evidence["evaluation"] = any(
        word in text
        for word in [
            "ndcg",
            "mrr",
            "map",
            "evaluation",
            "ab testing"
        ]
    )

    evidence["leadership"] = any(
        word in normalize(
            " ".join(
                evidence["role_history"]
            )
        )
        for word in [
            "lead",
            "principal",
            "architect",
            "manager"
        ]
    )

    education = ""

    for edu in candidate.get("education", []):

        education += (
            edu.get("degree", "")
            + " "
            + edu.get("field_of_study", "")
            + " "
        )

    evidence["education"] = education


    return evidence