import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ----------------------------
# Load Dataset
# ----------------------------

def load_dataset():

    df = pd.read_csv("dataset/final_reviews.csv")

    return df


# ----------------------------
# Sentiment Pie Chart
# ----------------------------

def sentiment_chart(df):

    counts = df["sentiment"].value_counts().reset_index()

    counts.columns = ["Sentiment", "Count"]

    fig = px.pie(
        counts,
        values="Count",
        names="Sentiment",
        hole=0.45,
        title="Customer Sentiment Distribution"
    )

    fig.update_traces(textinfo="percent+label")

    fig.update_layout(
        height=420
    )

    return fig


# ----------------------------
# Review Quality Histogram
# ----------------------------

def quality_chart(df):

    mapping = {

        "Very Positive":95,
        "Positive":80,
        "Neutral":60,
        "Negative":35,
        "Very Negative":15

    }

    df = df.copy()

    df["quality"] = df["sentiment"].map(mapping)

    fig = px.histogram(

        df,

        x="quality",

        nbins=12,

        title="Review Quality Score Distribution"

    )

    fig.update_layout(height=420)

    return fig


# ----------------------------
# Top Issues
# ----------------------------

def top_issue_chart(df):

    keywords = {

        "Delay":0,
        "Food":0,
        "Staff":0,
        "Seat":0,
        "Baggage":0,
        "Boarding":0,
        "Cleanliness":0

    }

    if "clean_review" in df.columns:

        reviews = df["clean_review"]

    else:

        reviews = df["reviews"]

    for review in reviews:

        review = str(review).lower()

        if "delay" in review:
            keywords["Delay"] += 1

        if "food" in review:
            keywords["Food"] += 1

        if "staff" in review:
            keywords["Staff"] += 1

        if "seat" in review:
            keywords["Seat"] += 1

        if "bag" in review:
            keywords["Baggage"] += 1

        if "boarding" in review:
            keywords["Boarding"] += 1

        if "clean" in review:
            keywords["Cleanliness"] += 1

    chart = pd.DataFrame({

        "Issue": keywords.keys(),

        "Count": keywords.values()

    })

    chart = chart.sort_values(

        by="Count",

        ascending=False

    )

    fig = px.bar(

        chart,

        x="Issue",

        y="Count",

        text="Count",

        title="Most Frequently Reported Issues"

    )

    fig.update_layout(height=420)

    return fig


# ----------------------------
# Average Quality Score
# ----------------------------

def average_quality(df):

    mapping = {

        "Very Positive":95,
        "Positive":80,
        "Neutral":60,
        "Negative":35,
        "Very Negative":15

    }

    quality = df["sentiment"].map(mapping)

    return round(quality.mean(),1)


# ----------------------------
# KPI Metrics
# ----------------------------

def dashboard_metrics(df):

    total = len(df)

    positive = len(

        df[

            df["sentiment"].isin(

                [

                    "Positive",

                    "Very Positive"

                ]

            )

        ]

    )

    negative = len(

        df[

            df["sentiment"].isin(

                [

                    "Negative",

                    "Very Negative"

                ]

            )

        ]

    )

    neutral = len(

        df[

            df["sentiment"]=="Neutral"

        ]

    )

    return {

        "total": total,

        "positive": positive,

        "negative": negative,

        "neutral": neutral,

        "quality": average_quality(df)

    }


# ----------------------------
# Recent Reviews
# ----------------------------

def recent_reviews(df):

    columns = [

        "title",

        "sentiment"

    ]

    available = [

        c for c in columns

        if c in df.columns

    ]

    return df[available].head(10)