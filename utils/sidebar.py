import streamlit as st
import pandas as pd
from utils.trend_analysis import dashboard_metrics


def show_sidebar():

    st.sidebar.title("✈ British Airways AI")

    st.sidebar.markdown("---")

    st.sidebar.subheader("📊 Project Statistics")

    try:

        df = pd.read_csv("dataset/final_reviews.csv")

        metrics = dashboard_metrics(df)

        st.sidebar.metric(
            "Reviews",
            metrics["total"]
        )

        st.sidebar.metric(
            "Positive",
            metrics["positive"]
        )

        st.sidebar.metric(
            "Negative",
            metrics["negative"]
        )

        st.sidebar.metric(
            "Neutral",
            metrics["neutral"]
        )

        st.sidebar.metric(
            "Average Quality",
            f'{metrics["quality"]}/100'
        )

    except:

        st.sidebar.warning(
            "Dataset not found."
        )

    st.sidebar.markdown("---")

    st.sidebar.subheader("🤖 AI Models")

    st.sidebar.success("Logistic Regression")

    st.sidebar.success("Amazon Bedrock")

    st.sidebar.success("Aspect Analyzer")

    st.sidebar.success("Quality Scoring")

    st.sidebar.markdown("---")

    st.sidebar.subheader("☁ AWS Services")

    st.sidebar.info("Amazon S3")

    st.sidebar.info("AWS Lambda")

    st.sidebar.info("Amazon API Gateway")

    st.sidebar.info("Amazon DynamoDB")

    st.sidebar.markdown("---")

    st.sidebar.subheader("🛠 Tech Stack")

    st.sidebar.write("🐍 Python")

    st.sidebar.write("📊 Streamlit")

    st.sidebar.write("📈 Plotly")

    st.sidebar.write("🤖 Scikit-learn")

    st.sidebar.write("☁ AWS Cloud")

    st.sidebar.markdown("---")

    st.sidebar.caption("Developed using AWS AI Services")
    