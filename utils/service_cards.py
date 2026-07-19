import streamlit as st


def stars(rating):

    return "⭐" * rating + "☆" * (5 - rating)


def status_color(status):

    if status == "Excellent":

        return "🟢"

    elif status == "Average":

        return "🟡"

    else:

        return "🔴"


def show_service_cards(aspects):

    st.subheader("✈ Airline Service Ratings")

    cols = st.columns(3)

    for index, row in aspects.iterrows():

        with cols[index % 3]:

            st.markdown(
                f"""
### {row['Aspect']}

{stars(row['Rating'])}

**Status:** {status_color(row['Status'])} {row['Status']}
                """
            )

    st.divider()


def show_aspect_table(aspects):

    st.subheader("📋 Aspect Analysis")

    styled = aspects.copy()

    styled["Rating"] = styled["Rating"].apply(stars)

    st.dataframe(

        styled,

        use_container_width=True,

        hide_index=True

    )

    st.divider()