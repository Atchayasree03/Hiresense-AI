from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer("models/all-MiniLM-L6-v2")


def generate_embedding(text):
    return model.encode(text)


if __name__ == "__main__":

    sample_text = """
    Role OverviewWe are seeking a Data Scientist to transform raw data into actionable insights. You will build predictive models and analyze complex datasets to solve business problems.Key ResponsibilitiesClean Data: Collect and prepare data from various sources.Build Models: Design and deploy machine learning algorithms.Find Trends: Conduct statistical analysis to uncover patterns.Visualize Insights: Create dashboards using Tableau or Power BI.Share Findings: Present data-driven solutions to business stakeholders.Technical RequirementsCode: Advanced Python, R, and SQL.ML Libraries: Experience with Scikit-learn, TensorFlow, or PyTorch.Math: Strong skills in statistics and probability.Education: Degree in Computer Science, Data Science, or Math.
    """

    embedding = generate_embedding(
        sample_text
    )

    print("Embedding Shape:")
    print(embedding.shape)

    print("\nFirst 10 Values:")
    print(embedding[:10])