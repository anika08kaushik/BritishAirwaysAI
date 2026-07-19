import streamlit as st


def show_input_section():

    st.subheader("📝 Customer Review")

    st.markdown(
        "Enter a British Airways customer review below to analyze customer sentiment, service quality, and generate AI-powered recommendations."
    )

    review = st.text_area(
        label="",
        placeholder="""Example:

The cabin crew were very friendly and professional.
The flight departed on time and the food was excellent.
Overall, I had a wonderful experience.""",
        height=220
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        analyze = st.button(
            "🚀 Analyze Review",
            use_container_width=True
        )

    with col2:

        if st.button(
            "😊 Positive Example",
            use_container_width=True
        ):

            st.session_state["review"] = (
                "The cabin crew were excellent. "
                "Food was delicious and boarding was smooth. "
                "I would definitely fly British Airways again."
            )

            st.rerun()

    with col3:

        if st.button(
            "😡 Negative Example",
            use_container_width=True
        ):

            st.session_state["review"] = (
                "The flight was delayed by four hours. "
                "Food was terrible and the staff were rude. "
                "Very disappointing experience."
            )

            st.rerun()

    st.divider()

    words = len(review.split())

    characters = len(review)

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "📝 Word Count",
            words
        )

    with c2:

        st.metric(
            "🔤 Characters",
            characters
        )

    return review, analyze