import streamlit as st

from utils.trend_analysis import (
    load_dataset,
    sentiment_chart,
    quality_chart,
    top_issue_chart,
    average_quality,
    recent_reviews
)


def show_trend_dashboard():

    st.subheader("📈 Analytics Dashboard")

    try:

        df = load_dataset()

    except Exception:

        st.warning("Dataset not found.")

        return

    # ------------------------
    # KPI Cards
    # ------------------------

    positive = len(
        df[df["sentiment"].isin(["Positive", "Very Positive"])]
    )

    negative = len(
        df[df["sentiment"].isin(["Negative", "Very Negative"])]
    )

    neutral = len(
        df[df["sentiment"] == "Neutral"]
    )

    total = len(df)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Reviews",
        total
    )

    c2.metric(
        "Positive",
        positive
    )

    c3.metric(
        "Negative",
        negative
    )

    c4.metric(
        "Avg Quality",
        f"{average_quality(df)}/100"
    )

    st.divider()

    # ------------------------
    # Charts
    # ------------------------

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            sentiment_chart(df),
            use_container_width=True
        )

    with right:

        st.plotly_chart(
            quality_chart(df),
            use_container_width=True
        )

    st.plotly_chart(
        top_issue_chart(df),
        use_container_width=True
    )

    st.divider()

    # ------------------------
    # Recent Reviews
    # ------------------------

    st.subheader("📰 Recent Reviews")

    st.dataframe(

        recent_reviews(df),

        use_container_width=True,

        hide_index=True

    )

    st.divider()