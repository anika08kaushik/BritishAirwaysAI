import re
import nltk
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")

INPUT_FILE = "dataset/sentiment_reviews.csv"
OUTPUT_FILE = "dataset/final_reviews.csv"

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()


def preprocess(text):

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove HTML
    text = re.sub(r"<.*?>", "", text)

    # Remove punctuation
    text = re.sub(r"[^a-zA-Z ]", " ", text)

    # Remove digits
    text = re.sub(r"\d+", "", text)

    words = text.split()

    processed = []

    for word in words:

        if word not in stop_words:

            processed.append(
                lemmatizer.lemmatize(word)
            )

    return " ".join(processed)


def main():

    print("=" * 60)
    print("Running Text Preprocessing...")
    print("=" * 60)

    df = pd.read_csv(INPUT_FILE)

    df["clean_review"] = df["reviews"].apply(preprocess)

    print(df[["clean_review"]].head())

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nSaved :", OUTPUT_FILE)


if __name__ == "__main__":
    main()