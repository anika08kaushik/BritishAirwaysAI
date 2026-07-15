import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from model.predict import predict_sentiment
import boto3

# ----------------------------
# AWS Bedrock Client
# ----------------------------
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"      # Keep this if Nova Micro works in us-east-1
)


def generate_report(review):
    """
    Generate complete AI report using:
    1. ML Sentiment Model
    2. Amazon Bedrock
    """

    # ----------------------------
    # Step 1 : Predict Sentiment
    # ----------------------------
    sentiment = predict_sentiment(review)

    # ----------------------------
    # Step 2 : Prompt
    # ----------------------------
    prompt = f"""
You are an airline customer experience expert.

Customer Review:
{review}

Predicted Sentiment:
{sentiment}

Analyze the review and provide:

1. Overall Analysis

2. Key Issues

3. Three Recommendations

Keep the response concise and professional.
"""

    # ----------------------------
    # Step 3 : Bedrock
    # ----------------------------
    response = client.converse(
        modelId="us.amazon.nova-micro-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    )

    # ----------------------------
    # Step 4 : Extract Response
    # ----------------------------
    ai_response = response["output"]["message"]["content"][0]["text"]

    # ----------------------------
    # Step 5 : Return Everything
    # ----------------------------
    return {
        "sentiment": sentiment,
        "recommendations": ai_response
    }


# ---------------------------------------------------
# Testing
# ---------------------------------------------------
if __name__ == "__main__":

    review = """
Flight delayed by four hours.
Food was terrible.
Staff were rude.
"""

    result = generate_report(review)

    print("=" * 60)
    print("PREDICTED SENTIMENT")
    print("=" * 60)

    print(result["sentiment"])

    print("\n")

    print("=" * 60)
    print("AI RECOMMENDATIONS")
    print("=" * 60)

    print(result["recommendations"])