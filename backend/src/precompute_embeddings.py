import numpy as np
from tqdm import tqdm

from loader import load_candidates
from profile_builder import build_candidate_text
from embeddings import generate_embedding


def precompute():

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    embeddings = []

    # TEMPORARY
    candidates = candidates[:1000]

    for candidate in tqdm(
        candidates,
        desc="Generating Embeddings"
    ):

        text = build_candidate_text(
            candidate
        )

        embedding = generate_embedding(
            text
        )

        embeddings.append(
            embedding
        )

    embeddings = np.array(
        embeddings
    )

    np.save(
        "data/candidate_embeddings.npy",
        embeddings
    )

    print(
        f"Saved {len(embeddings)} embeddings"
    )


if __name__ == "__main__":
    precompute()