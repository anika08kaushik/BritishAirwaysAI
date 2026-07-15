import requests
import streamlit as st
import sys
import os

# -----------------------------
# Add Project Root
# -----------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from recommendation.recommendation_engine import generate_report

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="British Airways AI Review Analyzer",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("✈️ British Airways AI Review Analyzer")
st.markdown("### AI Powered Customer Review Analysis")

st.write("---")

# -----------------------------
# API Gateway URL
# -----------------------------
API_URL = "https://8fmm7c7ioe.execute-api.ap-south-1.amazonaws.com/predict"

# -----------------------------
# User Input
# -----------------------------
review = st.text_area(
    "Enter a British Airways customer review",
    height=200,
    placeholder="Example:\nThe flight was delayed by 4 hours. Food was terrible and the staff were rude."
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze Review"):

    if review.strip() == "":
        st.warning("Please enter a review.")
        st.stop()

    # -----------------------------
    # Generate AI Report
    # -----------------------------
    with st.spinner("Analyzing review..."):
        result = generate_report(review)

    # -----------------------------
    # Send to API Gateway
    # -----------------------------
    payload = {
        "review": review,
        "sentiment": result["sentiment"],
        "csat": result.get("csat", ""),
        "recommendations": result["recommendations"]
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            st.success("✅ Analysis saved to AWS successfully!")
        else:
            st.warning(f"⚠️ AWS returned Status Code: {response.status_code}")
            st.write(response.text)

    except Exception as e:
        st.error(f"AWS Error: {e}")

    # -----------------------------
    # Display Results
    # -----------------------------
    st.success("Analysis Completed!")

    st.write("---")

    # Sentiment
    st.subheader("📊 Predicted Sentiment")
    st.info(result["sentiment"])

    # AI Analysis
    st.subheader("🤖 AI Analysis")
    st.write(result["recommendations"])