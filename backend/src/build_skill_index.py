import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("models/all-MiniLM-L6-v2")

with open(
    "data/skills.json",
    "r",
    encoding="utf-8"
) as f:

    skills = json.load(f)

embeddings = model.encode(
    skills,
    normalize_embeddings=True
)

embeddings = np.array(
    embeddings,
    dtype=np.float32
)

index = faiss.IndexFlatIP(
    embeddings.shape[1]
)

index.add(
    embeddings
)

faiss.write_index(
    index,
    "data/skills.index"
)

print("Done")
print(len(skills))