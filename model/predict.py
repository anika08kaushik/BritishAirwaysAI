import re
import joblib

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load saved model and vectorizer
MODEL_PATH = "model/saved_models/csat_model.pkl"
VECTORIZER_PATH = "model/saved_models/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    text = text.lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z ]", " ", text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


def predict_sentiment(review):
    """
    Predict estimated customer satisfaction (1-5)
    """

    cleaned = preprocess(review)

    vector = vectorizer.transform([cleaned])

    csat = int(model.predict(vector)[0])

    sentiment_map = {
        5: "Very Positive",
        4: "Positive",
        3: "Neutral",
        2: "Negative",
        1: "Very Negative"
    }

    return sentiment_map[csat]


if __name__ == "__main__":

    while True:

        review = input("\nEnter Review (type exit to quit): ")

        if review.lower() == "exit":
            break

        sentiment = predict_sentiment(review)

        print("\nPredicted Sentiment :", sentiment)