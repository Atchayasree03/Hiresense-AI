
def generate_explanation(
    candidate,
    matched_skills,
    jd_experience
):

    reasons = []

    if matched_skills:

        reasons.append(
            f"Matched skills: {', '.join(matched_skills)}"
        )

    years = candidate["profile"].get(
        "years_of_experience",
        0
    )

    if years >= jd_experience:

        reasons.append(
            f"{years} years experience exceeds required {jd_experience} years"
        )

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    if signals.get(
        "open_to_work_flag",
        False
    ):
        reasons.append(
            "Currently open to work"
        )

    if signals.get(
        "recruiter_response_rate",
        0
    ) > 0.5:

        reasons.append(
            "High recruiter response rate"
        )

    return reasons