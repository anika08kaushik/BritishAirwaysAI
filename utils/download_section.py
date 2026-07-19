import os
import streamlit as st

from utils.pdf_report import generate_pdf


def show_download_section(
    review,
    sentiment,
    quality,
    recommendation,
    aspects
):

    st.subheader("📄 Download Analysis Report")

    filename = "BritishAirways_AI_Report.pdf"

    generate_pdf(
        filename,
        review,
        sentiment,
        quality,
        recommendation,
        aspects
    )

    if os.path.exists(filename):

        with open(filename, "rb") as pdf:

            st.download_button(

                label="⬇ Download PDF Report",

                data=pdf,

                file_name=filename,

                mime="application/pdf",

                use_container_width=True

            )

    st.success("Your report is ready.")

    st.info(
        """
The PDF contains:

• Customer Review

• Sentiment Prediction

• Review Quality Score

• Aspect Analysis

• AI Recommendation

• Report Generation Time
        """
    )

    st.divider()