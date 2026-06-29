import csv


def export_candidates_to_csv(
    candidates,
    output_file="ranked_candidates.csv"
):

    with open(
        output_file,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Rank",
                "Candidate ID",
                "Headline",
                "Experience",
                "Semantic Score",
                "Career Score",
                "Behavior Score",
                "Final Score",
                "Matched Skills",
                "AI Summary"
            ]
        )

        for rank, candidate in enumerate(
            candidates,
            start=1
        ):

            writer.writerow(
                [
                    rank,

                    candidate[
                        "candidate_id"
                    ],

                    candidate[
                        "headline"
                    ],

                    candidate[
                        "years_of_experience"
                    ],

                    candidate[
                        "semantic_score"
                    ],

                    candidate[
                        "career_score"
                    ],

                    candidate[
                        "behavior_score"
                    ],

                    candidate[
                        "final_score"
                    ],

                    ", ".join(
                        candidate[
                            "matched_skills"
                        ]
                    ),

                    candidate[
                        "ai_summary"
                    ]
                ]
            )

    print(
        f"\nCSV exported successfully: "
        f"{output_file}"
    )


if __name__ == "__main__":

    from rank_candidates import (
        rank_candidates
    )

    jd = """
    Data Scientist

    Required Skills:
    Python
    SQL
    TensorFlow
    PyTorch
    Scikit-learn

    Experience:
    3+ years
    """

    candidates = rank_candidates(
        jd,
        top_k=10
    )

    export_candidates_to_csv(
        candidates
    )