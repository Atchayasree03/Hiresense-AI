from src.loader import load_candidates

candidates = load_candidates("data/candidates.jsonl")


def get_candidate(index):
    return candidates[index]


def get_candidate_by_id(candidate_id):

    for candidate in candidates:

        if candidate["candidate_id"] == candidate_id:
            return candidate

    return None