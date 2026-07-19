import os
import sys

import streamlit as st

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from recommendation.recommendation_engine import generate_report

from utils.header import show_header
from utils.sidebar import show_sidebar
from utils.input_section import show_input_section

from utils.quality_score import calculate_quality_score
from utils.aspect_analyzer import analyze_aspects

from utils.aws_handler import save_to_aws

from utils.result_cards import (
    show_result_cards,
    show_ai_analysis
)

from utils.service_cards import (
    show_service_cards,
    show_aspect_table
)

from utils.trend_dashboard import show_trend_dashboard

from utils.download_section import (
    show_download_section
)


# ------------------------------------
# Page Configuration
# ------------------------------------

st.set_page_config(

    page_title="British Airways AI Analytics",

    page_icon="✈️",

    layout="wide"

)

# ------------------------------------
# Sidebar
# ------------------------------------

show_sidebar()

# ------------------------------------
# Header
# ------------------------------------

show_header()

# ------------------------------------
# Input Section
# ------------------------------------

review, analyze = show_input_section()

# ------------------------------------
# Analyze Review
# ------------------------------------

if analyze:

    if review.strip() == "":

        st.warning("Please enter a review.")

        st.stop()

    with st.spinner("Analyzing Review..."):

        result = generate_report(review)

    # ------------------------------------
    # Quality Score
    # ------------------------------------

    quality = calculate_quality_score(

        review,

        result["sentiment"]

    )

    # ------------------------------------
    # Aspect Analysis
    # ------------------------------------

    aspects = analyze_aspects(review)

    # ------------------------------------
    # Save to AWS
    # ------------------------------------

    save_to_aws(

        review,

        result,

        quality

    )

    # ------------------------------------
    # Result Cards
    # ------------------------------------

    show_result_cards(

        result["sentiment"],

        quality

    )

    # ------------------------------------
    # Aspect Table
    # ------------------------------------

    show_aspect_table(

        aspects

    )

    # ------------------------------------
    # Service Cards
    # ------------------------------------

    show_service_cards(

        aspects

    )

    # ------------------------------------
    # AI Recommendation
    # ------------------------------------

    show_ai_analysis(

        result["recommendations"]

    )

    # ------------------------------------
    # Trend Dashboard
    # ------------------------------------

    show_trend_dashboard()

    # ------------------------------------
    # Download Report
    # ------------------------------------

    show_download_section(

        review,

        result["sentiment"],

        quality,

        result["recommendations"],

        aspects

    )