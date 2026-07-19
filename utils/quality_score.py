import re


def count_positive_words(text):
    positive_words = [
        "good", "great", "excellent", "amazing", "friendly",
        "helpful", "comfortable", "clean", "smooth", "pleasant",
        "professional", "love", "best", "perfect", "awesome",
        "delicious", "happy", "quick", "easy", "fantastic"
    ]

    words = re.findall(r"\b\w+\b", text.lower())

    return sum(word in positive_words for word in words)


def count_negative_words(text):
    negative_words = [
        "bad", "worst", "delay", "late", "terrible",
        "rude", "dirty", "poor", "awful", "cancelled",
        "cancel", "broken", "horrible", "slow",
        "problem", "complaint", "disappointed",
        "uncomfortable", "angry", "lost"
    ]

    words = re.findall(r"\b\w+\b", text.lower())

    return sum(word in negative_words for word in words)


def calculate_quality_score(review, sentiment):

    score = 50

    # --------------------------
    # Sentiment Weight
    # --------------------------

    sentiment_scores = {
        "Very Positive": 35,
        "Positive": 20,
        "Neutral": 0,
        "Negative": -20,
        "Very Negative": -35
    }

    score += sentiment_scores.get(sentiment, 0)

    # --------------------------
    # Positive Words
    # --------------------------

    score += count_positive_words(review) * 2

    # --------------------------
    # Negative Words
    # --------------------------

    score -= count_negative_words(review) * 2

    # --------------------------
    # Review Length
    # --------------------------

    word_count = len(review.split())

    if word_count > 60:
        score += 10

    elif word_count > 30:
        score += 5

    # --------------------------
    # Keep between 0 and 100
    # --------------------------

    score = max(0, min(100, score))

    return score