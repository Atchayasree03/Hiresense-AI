from src.candidate_mapper import get_candidate
from src.career_score import calculate_career_score
from src.behavior_score import calculate_behavior_score
from src.faiss_search import search_candidates

jd_text = """
Role OverviewWe are seeking a Data Scientist to transform raw data into actionable insights. You will build predictive models and analyze complex datasets to solve business problems.Key ResponsibilitiesClean Data: Collect and prepare data from various sources.Build Models: Design and deploy machine learning algorithms.Find Trends: Conduct statistical analysis to uncover patterns.Visualize Insights: Create dashboards using Tableau or Power BI.Share Findings: Present data-driven solutions to business stakeholders.Technical RequirementsCode: Advanced Python, R, and SQL.ML Libraries: Experience with Scikit-learn, TensorFlow, or PyTorch.Math: Strong skills in statistics and probability.Education: Degree in Computer Science, Data Science, or Math.
"""

scores, indices = search_candidates(
    jd_text,
    top_k=1
)

score = scores[0][0]
idx = indices[0][0]

candidate = get_candidate(idx)

semantic_score = score * 100
career_score = calculate_career_score(candidate)
behavior_score = calculate_behavior_score(candidate)

final_score = (
    0.5 * semantic_score +
    0.3 * career_score +
    0.2 * behavior_score
)

print(f"Candidate: {candidate['candidate_id']}")
print(f"Headline: {candidate['profile']['headline']}")
print(f"Semantic Score: {semantic_score:.2f}")
print(f"Career Score: {career_score:.2f}")
print(f"Behavior Score: {behavior_score:.2f}")
print(f"Final Score: {final_score:.2f}")