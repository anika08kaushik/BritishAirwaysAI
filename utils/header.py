import streamlit as st


def show_header():

    st.markdown(
        """
        <style>

        .main-title{
            font-size:42px;
            font-weight:bold;
            color:#0E6FFF;
        }

        .sub-title{
            font-size:18px;
            color:gray;
            margin-bottom:20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------
    # Title
    # -----------------------------

    st.markdown(
        """
        <div class='main-title'>
            ✈ British Airways AI Analytics Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------
    # Subtitle
    # -----------------------------

    st.markdown(
        """
        <div class='sub-title'>
            AI-powered customer review analysis using Machine Learning,
            Amazon Bedrock and AWS Serverless Services.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------
    # Project Info Cards
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🤖 AI Model",
            "Logistic Regression"
        )

    with col2:
        st.metric(
            "🧠 LLM",
            "Amazon Nova"
        )

    with col3:
        st.metric(
            "☁ Cloud",
            "AWS"
        )

    st.divider()