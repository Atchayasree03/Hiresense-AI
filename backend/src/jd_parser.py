import json
import re
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from src.jd_validator import validate_skills

# Load model once
model = SentenceTransformer("models/all-MiniLM-L6-v2")

# Load skills extracted from candidates.jsonl
with open("data/skills.json", "r", encoding="utf-8") as f:
    SKILLS = json.load(f)

# Load precomputed embeddings
skill_embeddings = np.load("data/skill_embeddings.npy")


def split_jd(jd_text):
    lines = re.split(r'[\n•,-]+', jd_text)

    cleaned = []

    for line in lines:
        line = line.strip()

        if len(line) > 3:
            cleaned.append(line)

    return cleaned


def extract_exact_skills(jd):

    jd_lower = jd.lower()

    skills = []

    for skill in SKILLS:

        if skill.lower() in jd_lower:

            skills.append(skill)

    return skills


def search_skills(sentence):

    embedding = model.encode(
        sentence,
        normalize_embeddings=True
    )

    similarities = cosine_similarity(
        [embedding],
        skill_embeddings
    )[0]

    matches = []

    for skill, score in zip(SKILLS, similarities):

        if score >= 0.70:

            matches.append(skill)

    return matches


def extract_semantic_skills(jd):

    sentences = split_jd(jd)

    semantic = []

    for sentence in sentences:

        semantic.extend(
            search_skills(sentence)
        )

    return list(set(semantic))


def extract_required_skills(jd):

    exact = extract_exact_skills(jd)

    semantic = extract_semantic_skills(jd)

    final = exact.copy()

    for skill in semantic:

        if skill not in final:

            final.append(skill)

    return final


def extract_experience(jd):

    match = re.search(
        r'(\d+)\+?\s*(years?|yrs?)',
        jd.lower()
    )

    if match:
        return int(match.group(1))

    return 0


def extract_role(jd):

    lines = split_jd(jd)

    if len(lines) > 0:
        return lines[0]

    return "Software Engineer"


def parse_jd(jd_text):

    parsed = {

        "role": extract_role(jd_text),

        "required_skills": extract_required_skills(jd_text),

        "preferred_skills": [],

        "experience_years": extract_experience(jd_text),

        "responsibilities": [],

        "core_competencies": [],

        "engineering_focus": [],

        "company_preference": "",

        "behavioral_preferences": []

    }

    parsed = validate_skills(
        parsed,
        jd_text
    )

    return parsed