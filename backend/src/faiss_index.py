import faiss
import numpy as np


embeddings = np.load(
    "data/candidate_embeddings.npy"
)

embeddings = embeddings.astype("float32")

dimension = embeddings.shape[1]

faiss.normalize_L2(embeddings)

index = faiss.IndexFlatIP(
    dimension
)

index.add(embeddings)

faiss.write_index(
    index,
    "data/candidates.index"
)

print(
    f"Indexed {index.ntotal} candidates"
)