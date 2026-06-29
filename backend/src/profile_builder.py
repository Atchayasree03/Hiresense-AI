def build_candidate_text(candidate):

    text_parts = []

    profile = candidate.get("profile", {})

    text_parts.append(profile.get("headline", ""))
    text_parts.append(profile.get("summary", ""))
    text_parts.append(profile.get("current_title", ""))
    text_parts.append(profile.get("current_industry", ""))

    # Career History
    for job in candidate.get("career_history", []):
        text_parts.append(job.get("title", ""))
        text_parts.append(job.get("description", ""))

    # Skills
    for skill in candidate.get("skills", []):
        text_parts.append(skill.get("name", ""))

    # Education
    for edu in candidate.get("education", []):
        text_parts.append(edu.get("degree", ""))
        text_parts.append(edu.get("field_of_study", ""))

    return " ".join(text_parts)

from loader import load_candidates

if __name__ == "__main__":

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    text = build_candidate_text(
        candidates[0]
    )

    print(text[:3000])