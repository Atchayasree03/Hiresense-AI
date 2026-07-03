from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("models/all-MiniLM-L6-v2")


def calculate_role_score(
    jd_role,
    candidate_headline
):

    if not jd_role:
        return 0

    if not candidate_headline:
        return 0

    jd_embedding = model.encode(
        [jd_role],
        convert_to_numpy=True
    )

    candidate_embedding = model.encode(
        [candidate_headline],
        convert_to_numpy=True
    )

    similarity = float(
        cosine_similarity(
            jd_embedding,
            candidate_embedding
        )[0][0]
    )

    return round(similarity * 100, 2)
