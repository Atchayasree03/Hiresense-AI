from src.loader import load_candidates
candidates = load_candidates(
    "data/candidates.jsonl"
)

def get_candidate(index):
    return candidates[index]

