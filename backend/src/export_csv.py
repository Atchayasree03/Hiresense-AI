import pandas as pd

from src.rank_candidates import rank_candidates


def export_csv(jd_text):

    candidates = rank_candidates(
        jd_text,
        top_k=100
    )

    rows = []

    for rank, candidate in enumerate(candidates, start=1):

        reasoning = (
            f"{candidate['headline']} with "
            f"{candidate['years_of_experience']} years experience. "
            f"Matched skills: "
            f"{', '.join(candidate['matched_skills'][:5])}. "
            f"Overall match score "
            f"{candidate['match_score']}."
        )

        rows.append({

            "candidate_id": candidate["candidate_id"],

            "rank": rank,

            "score": round(candidate["match_score"] / 100, 3),

            "reasoning": reasoning

        })

    df = pd.DataFrame(rows)

    df.to_csv(
        "submission.csv",
        index=False
    )

    print("submission.csv generated successfully.")


if __name__ == "__main__":

    jd = open(
        "sample_jd.txt",
        encoding="utf-8"
    ).read()

    export_csv(jd)