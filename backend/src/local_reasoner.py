def generate_ai_reason(candidate, matched_skills, jd_text):

    profile = candidate["profile"]

    experience = profile.get(
        "years_of_experience",
        0
    )

    headline = profile.get(
        "headline",
        ""
    )

    company = profile.get(
        "current_company",
        "Unknown"
    )

    summary = profile.get(
        "summary",
        ""
    )

    career = candidate.get(
        "career_history",
        []
    )

    career_titles = []

    for job in career:
        title = job.get("title")
        if title:
            career_titles.append(title)

    text = (
        f"This candidate has "
        f"{experience} years of experience as "
        f"{headline}. "

        f"The candidate currently works at "
        f"{company}. "

        f"Matched skills include "
        f"{', '.join(matched_skills)}. "
    )

    if career_titles:

        text += (
            "Career progression includes "
            + ", ".join(career_titles)
            + ". "
        )

    if summary:

        text += (
            "Professional background: "
            + summary[:250]
            + "..."
        )

    return text