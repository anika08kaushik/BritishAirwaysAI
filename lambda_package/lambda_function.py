import json
import joblib
import re
from datetime import datetime

import boto3

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ---------- AWS ----------
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("BritishAirwaysPredictions")

# ---------- Load Model ----------
model = joblib.load("csat_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

recommendation_map = {
    "delay": "Improve flight scheduling.",
    "delayed": "Improve flight scheduling.",
    "food": "Improve meal quality.",
    "meal": "Improve meal quality.",
    "seat": "Provide more comfortable seating.",
    "staff": "Provide additional customer service training.",
    "crew": "Provide additional customer service training.",
    "bag": "Improve baggage handling.",
    "baggage": "Improve baggage handling.",
    "airport": "Improve airport support.",
    "service": "Improve customer service.",
    "boarding": "Improve boarding process.",
    "check": "Improve check-in process."
}


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


def lambda_handler(event, context):

    body = json.loads(event["body"])

    review = body["review"]

    cleaned = preprocess(review)

    vector = vectorizer.transform([cleaned])

    prediction = int(model.predict(vector)[0])

    recommendations = []

    for key, value in recommendation_map.items():
        if key in review.lower():
            recommendations.append(value)

    if len(recommendations) == 0:
        recommendations.append("No major operational issue detected.")

    item = {
        "review_id": datetime.utcnow().isoformat(),
        "review": review,
        "predicted_csat": prediction,
        "recommendations": recommendations
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }