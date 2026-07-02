import json
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

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

np.save(
    "data/skill_embeddings.npy",
    embeddings
)

print("Done")
print("Skills :", len(skills))
print("Embedding Shape :", embeddings.shape)