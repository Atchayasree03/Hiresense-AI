import faiss
import numpy as np

from src.embeddings import generate_embedding


def search_candidates(jd_text, top_k=10):

    index = faiss.read_index(
        "data/candidates.index"
    )

    jd_embedding = generate_embedding(
        jd_text
    )

    jd_embedding = np.array(
        [jd_embedding],
        dtype="float32"
    )

    # cosine similarity
    faiss.normalize_L2(
        jd_embedding
    )

    scores, indices = index.search(
        jd_embedding,
        top_k
    )

    return scores, indices


if __name__ == "__main__":

    jd = """
    Role OverviewWe are seeking a Data Scientist to transform raw data into actionable insights. You will build predictive models and analyze complex datasets to solve business problems.Key ResponsibilitiesClean Data: Collect and prepare data from various sources.Build Models: Design and deploy machine learning algorithms.Find Trends: Conduct statistical analysis to uncover patterns.Visualize Insights: Create dashboards using Tableau or Power BI.Share Findings: Present data-driven solutions to business stakeholders.Technical RequirementsCode: Advanced Python, R, and SQL.ML Libraries: Experience with Scikit-learn, TensorFlow, or PyTorch.Math: Strong skills in statistics and probability.Education: Degree in Computer Science, Data Science, or Math.
    """

    scores, indices = search_candidates(
        jd,
        top_k=10
    )

    print("\nTop Matches:\n")

    for i in range(len(indices[0])):

        print(
            f"Candidate Index: {indices[0][i]}"
        )

        print(
            f"Similarity Score: {scores[0][i]:.4f}"
        )

        print("-" * 30)