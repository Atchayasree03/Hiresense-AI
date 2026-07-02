import numpy as np
from tqdm import tqdm

from src.loader import load_candidates
from src.profile_builder import build_candidate_text
from src.embeddings import model


def precompute():

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    texts = []

    for candidate in tqdm(
        candidates,
        desc="Preparing Candidate Text"
    ):

        texts.append(
            build_candidate_text(candidate)
        )

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        batch_size=128,
        show_progress_bar=True,
        convert_to_numpy=True
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