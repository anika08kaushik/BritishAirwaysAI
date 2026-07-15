import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

INPUT_FILE = "dataset/final_reviews.csv"

NUM_TOPICS = 5
NUM_WORDS = 10

print("=" * 60)
print("Topic Modelling")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

# Only use negative reviews
negative_reviews = df[
    df["sentiment"].isin(["Negative", "Very Negative"])
]["clean_review"]

print("\nNegative Reviews :", len(negative_reviews))

vectorizer = CountVectorizer(
    stop_words="english",
    max_features=1000
)

X = vectorizer.fit_transform(negative_reviews)

lda = LatentDirichletAllocation(
    n_components=NUM_TOPICS,
    random_state=42
)

lda.fit(X)

feature_names = vectorizer.get_feature_names_out()

print("\nDetected Topics\n")

for idx, topic in enumerate(lda.components_):

    print("=" * 40)

    print(f"Topic {idx+1}")

    print("=" * 40)

    words = [
        feature_names[i]
        for i in topic.argsort()[-NUM_WORDS:]
    ]

    print(", ".join(words))