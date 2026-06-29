import re


def normalize(text):
    return str(text).lower().strip()


def validate_skills(parsed_jd, jd_text):

    jd_lower = normalize(jd_text)

    required = []

    for skill in parsed_jd["required_skills"]:

        words = skill.split()

        # Check whether every word of the skill
        # exists somewhere in the JD.
        if all(
            normalize(word) in jd_lower
            for word in words
        ):
            required.append(skill)

    preferred = []

    for skill in parsed_jd["preferred_skills"]:

        words = skill.split()

        if all(
            normalize(word) in jd_lower
            for word in words
        ):
            preferred.append(skill)

    parsed_jd["required_skills"] = required
    parsed_jd["preferred_skills"] = preferred

    return parsed_jd