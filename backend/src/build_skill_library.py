import json

skills = set()

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(line)

        for skill in candidate.get("skills", []):

            skills.add(
                skill["name"].strip()
            )

skills = sorted(list(skills))

with open(
    "data/skills.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        skills,
        f,
        indent=4
    )

print("Total Skills :", len(skills))
print("Saved Successfully")