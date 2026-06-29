import json
from tqdm import tqdm


def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in tqdm(f, desc="Loading Candidates"):
            if line.strip():
                candidates.append(json.loads(line))

    return candidates


if __name__ == "__main__":
    candidates = load_candidates("data/candidates.jsonl")

    print(f"\nLoaded {len(candidates)} candidates")

    print("\nFirst Candidate ID:")
    print(candidates[0]["candidate_id"])
    print(candidates[0].keys())