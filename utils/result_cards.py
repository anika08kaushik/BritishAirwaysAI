import streamlit as st


def show_result_cards(sentiment, quality):

    st.subheader("📊 Analysis Results")

    col1, col2 = st.columns(2)

    # ---------------------------
    # Sentiment Card
    # ---------------------------

    with col1:

        if sentiment == "Very Positive":

            color = "🟢"

        elif sentiment == "Positive":

            color = "🟩"

        elif sentiment == "Neutral":

            color = "🟨"

        elif sentiment == "Negative":

            color = "🟧"

        else:

            color = "🔴"

        st.metric(

            label="Predicted Sentiment",

            value=f"{color} {sentiment}"

        )

    # ---------------------------
    # Quality Score Card
    # ---------------------------

    with col2:

        st.metric(

            label="Review Quality Score",

            value=f"{quality}/100"

        )

        st.progress(quality)

    st.divider()


# ---------------------------------------
# AI Recommendation Card
# ---------------------------------------

def show_ai_analysis(recommendation):

    st.subheader("🤖 AI Recommendation")

    st.info(recommendation)

    st.divider()