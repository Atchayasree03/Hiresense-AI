def build_candidate_text(candidate):

    profile = candidate.get("profile", {})

    text = []

    # Headline
    text.append(
        profile.get("headline", "")
    )

    # Professional Summary
    text.append(
        profile.get("summary", "")
    )

    # Current Role
    text.append(
        profile.get("current_title", "")
    )

    # Current Company
    text.append(
        profile.get("current_company", "")
    )

    # Industry
    text.append(
        profile.get("current_industry", "")
    )

    # Skills
    for skill in candidate.get("skills", []):

        text.append(
            skill.get("name", "")
        )

    # Career History
    for job in candidate.get("career_history", []):

        text.append(
            job.get("title", "")
        )

        text.append(
            job.get("description", "")
        )

        text.append(
            job.get("industry", "")
        )

    # Education
    for edu in candidate.get("education", []):

        text.append(
            edu.get("degree", "")
        )

        text.append(
            edu.get("field_of_study", "")
        )

    # Certifications
    for cert in candidate.get("certifications", []):

        text.append(
            cert.get("name", "")
        )

    # Languages
    for lang in candidate.get("languages", []):

        text.append(
            lang.get("language", "")
        )

    return " ".join(text)