def generate_ai_reason(candidate, matched_skills, jd_text):

    profile = candidate.get("profile", {})

    headline = profile.get("headline", "Professional")

    experience = profile.get(
        "years_of_experience",
        0
    )

    company = profile.get(
        "current_company",
        "Unknown"
    )

    summary = profile.get(
        "summary",
        ""
    )

    matched = ", ".join(matched_skills[:5])

    if not matched:
        matched = "No direct skill match identified"

    reason = (
        f"{headline} with {experience} years of experience "
        f"currently working at {company}. "
        f"Strong alignment with the job description through "
        f"{matched}. "
    )

    if summary:
        reason += (
            "Profile summary indicates relevant experience "
            "for this role."
        )

    return reason