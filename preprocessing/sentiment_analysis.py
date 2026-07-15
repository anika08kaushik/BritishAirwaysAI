import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

INPUT_FILE = "dataset/cleaned_reviews.csv"
OUTPUT_FILE = "dataset/sentiment_reviews.csv"

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(review):

    scores = analyzer.polarity_scores(str(review))

    compound = scores["compound"]

    if compound >= 0.5:
        sentiment = "Very Positive"
        csat = 5

    elif compound >= 0.1:
        sentiment = "Positive"
        csat = 4

    elif compound > -0.1:
        sentiment = "Neutral"
        csat = 3

    elif compound > -0.5:
        sentiment = "Negative"
        csat = 2

    else:
        sentiment = "Very Negative"
        csat = 1

    return pd.Series(
        [
            scores["neg"],
            scores["neu"],
            scores["pos"],
            compound,
            sentiment,
            csat,
        ]
    )


def main():

    print("=" * 60)
    print("Running Sentiment Analysis...")
    print("=" * 60)

    df = pd.read_csv(INPUT_FILE)

    df[
        [
            "negative_score",
            "neutral_score",
            "positive_score",
            "compound_score",
            "sentiment",
            "csat",
        ]
    ] = df["reviews"].apply(analyze_sentiment)

    print(df[["sentiment", "csat"]].head())

    print("\nSentiment Distribution\n")

    print(df["sentiment"].value_counts())

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nSaved :", OUTPUT_FILE)


if __name__ == "__main__":
    main()