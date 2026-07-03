from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load once
model = SentenceTransformer("models/all-MiniLM-L6-v2")


def semantic_skill_match(
    jd_skills,
    candidate_skills,
    threshold=0.70
):
    """
    Returns:
        matched_skills
        match_percentage
    """

    if not jd_skills:
        return [], 100

    if not candidate_skills:
        return [], 0

    matched = []

    candidate_embeddings = model.encode(
        candidate_skills,
        convert_to_numpy=True
    )

    for jd_skill in jd_skills:

        jd_embedding = model.encode(
            [jd_skill],
            convert_to_numpy=True
        )

        similarities = cosine_similarity(
            jd_embedding,
            candidate_embeddings
        )[0]

        best_score = similarities.max()

        if best_score >= threshold:

            idx = similarities.argmax()

            matched.append(
                candidate_skills[idx]
            )

    percentage = (
        len(matched) /
        len(jd_skills)
    ) * 100

    return matched, round(percentage, 2)