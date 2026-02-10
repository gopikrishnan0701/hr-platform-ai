from .schema import RankingRequest, RankingResponse, RankedCandidate


def calculate_final_score(match_score, missing_skills, experience_gaps):
    penalty = (len(missing_skills) * 5) + (len(experience_gaps) * 7)
    return max(match_score - penalty, 0)


def rank_candidates(request: RankingRequest) -> RankingResponse:
    scored = []

    for c in request.candidates:
        final = calculate_final_score(c.match_score, c.missing_skills, c.experience_gaps)
        scored.append((c.name, final))

    scored.sort(key=lambda x: x[1], reverse=True)

    ranked = [
        RankedCandidate(name=name, final_score=score, rank=i + 1)
        for i, (name, score) in enumerate(scored)
    ]

    return RankingResponse(ranked_candidates=ranked)
