import pandas as pd

# ----------------------------------------
# Airline Service Aspects
# ----------------------------------------

ASPECT_KEYWORDS = {

    "Cabin Crew": [
        "crew",
        "staff",
        "attendant",
        "hostess",
        "service"
    ],

    "Food": [
        "food",
        "meal",
        "breakfast",
        "lunch",
        "dinner",
        "snack",
        "drink"
    ],

    "Seat Comfort": [
        "seat",
        "comfort",
        "legroom",
        "space"
    ],

    "Boarding": [
        "boarding",
        "check-in",
        "queue",
        "gate"
    ],

    "Punctuality": [
        "delay",
        "late",
        "time",
        "cancelled",
        "cancel"
    ],

    "Cleanliness": [
        "clean",
        "dirty",
        "washroom",
        "toilet",
        "cabin"
    ],

    "Baggage": [
        "bag",
        "baggage",
        "luggage",
        "suitcase"
    ]

}

# ----------------------------------------
# Positive Words
# ----------------------------------------

POSITIVE = [

    "good",
    "great",
    "excellent",
    "friendly",
    "helpful",
    "comfortable",
    "clean",
    "quick",
    "smooth",
    "professional",
    "perfect",
    "amazing",
    "best",
    "love"

]

# ----------------------------------------
# Negative Words
# ----------------------------------------

NEGATIVE = [

    "bad",
    "worst",
    "delay",
    "late",
    "terrible",
    "dirty",
    "rude",
    "poor",
    "cancelled",
    "awful",
    "slow",
    "broken",
    "problem",
    "horrible",
    "uncomfortable"

]


def calculate_rating(review, keywords):

    review = review.lower()

    score = 3

    found = False

    for keyword in keywords:

        if keyword in review:

            found = True

            window = review

            for word in POSITIVE:

                if word in window:

                    score += 1

            for word in NEGATIVE:

                if word in window:

                    score -= 1

    if not found:

        return 3

    score = max(1, min(5, score))

    return score


def analyze_aspects(review):

    aspects = []

    ratings = []

    status = []

    emojis = []

    for aspect, keywords in ASPECT_KEYWORDS.items():

        rating = calculate_rating(review, keywords)

        aspects.append(aspect)

        ratings.append(rating)

        if rating >= 4:

            status.append("Excellent")

            emojis.append("🟢")

        elif rating == 3:

            status.append("Average")

            emojis.append("🟡")

        else:

            status.append("Needs Improvement")

            emojis.append("🔴")

    df = pd.DataFrame({

        "Aspect": aspects,

        "Rating": ratings,

        "Status": status,

        "Health": emojis

    })

    return df