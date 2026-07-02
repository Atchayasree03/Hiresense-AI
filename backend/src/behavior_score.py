

def calculate_behavior_score(candidate):

    signals = candidate.get(
        "redrob_signals", {}
    )

    score = 0

    if signals.get(
        "open_to_work_flag", False
    ):
        score += 20

    score += (
        signals.get(
            "recruiter_response_rate",
            0
        ) * 20
    )

    score += (
        signals.get(
            "interview_completion_rate",
            0
        ) * 20
    )

    score += min(
        signals.get(
            "profile_completeness_score",
            0
        ) / 5,
        20
    )

    score += min(
        signals.get(
            "github_activity_score",
            0
        ),
        20
    )

    return round(score, 2)


if __name__ == "__main__":

    candidate = get_candidate(30)

    score = calculate_behavior_score(
        candidate
    )

    print(
        candidate["candidate_id"]
    )

    print(
        "Behavior Score:",
        score
    )