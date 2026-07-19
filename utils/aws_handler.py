import requests
import streamlit as st

# -----------------------------
# API Gateway Endpoint
# -----------------------------

API_URL = "https://8fmm7c7ioe.execute-api.ap-south-1.amazonaws.com/predict"


def save_to_aws(review, result, quality):

    payload = {

        "review": review,

        "sentiment": result["sentiment"],

        "csat": quality,

        "recommendations": result["recommendations"]

    }

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=10
        )

        if response.status_code == 200:

            st.success("✅ Analysis saved to AWS successfully!")

            return True

        else:

            st.warning(
                f"⚠️ AWS returned Status Code {response.status_code}"
            )

            return False

    except requests.exceptions.Timeout:

        st.error("❌ AWS request timed out.")

        return False

    except requests.exceptions.ConnectionError:

        st.error("❌ Unable to connect to AWS API Gateway.")

        return False

    except Exception as e:

        st.error(f"❌ AWS Error: {e}")

        return False