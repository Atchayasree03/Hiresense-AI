from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from loader import load_candidates
from profile_builder import build_candidate_text
from embeddings import generate_embedding


def retrieve_top_candidates(jd_text, candidates, top_k=10):

    jd_embedding = generate_embedding(jd_text)

    scores = []

    for candidate in candidates:

        candidate_text = build_candidate_text(candidate)

        candidate_embedding = generate_embedding(
            candidate_text
        )

        similarity = cosine_similarity(
            [jd_embedding],
            [candidate_embedding]
        )[0][0]

        scores.append(
            (
                candidate["candidate_id"],
                similarity
            )
        )

    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scores[:top_k]


if __name__ == "__main__":

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    # VERY IMPORTANT
    candidates = candidates[:100]

    jd = """
    Senior AI Engineer

    Embeddings
    Retrieval
    Ranking
    Vector Databases
    Python
    """

    results = retrieve_top_candidates(
        jd,
        candidates,
        top_k=10
    )

    print("\nTop Matches:\n")

    for rank, result in enumerate(results, start=1):

        print(
            rank,
            result[0],
            round(result[1], 4)
        )