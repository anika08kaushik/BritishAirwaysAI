import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

INPUT_FILE = "dataset/final_reviews.csv"

MODEL_DIR = "model/saved_models"
MODEL_PATH = os.path.join(MODEL_DIR, "csat_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

print("=" * 60)
print("Loading Dataset")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

X = df["clean_review"]
y = df["csat"]

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2),
    min_df=2,
    max_df=0.95
)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training Logistic Regression...")

model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nAccuracy :", accuracy_score(y_test, predictions))

print("\nClassification Report\n")

print(classification_report(y_test, predictions))

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, predictions))

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)

print("\nModel Saved Successfully.")