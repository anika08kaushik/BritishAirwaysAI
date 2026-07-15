import json
import boto3
from datetime import datetime
import uuid

# -----------------------------
# DynamoDB Configuration
# -----------------------------
dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-south-1"
)

table = dynamodb.Table("BritishAirwaysPredictions")


def lambda_handler(event, context):
    try:

        # -----------------------------
        # Read Request Body
        # -----------------------------
        body = json.loads(event["body"])

        review = body.get("review", "")
        sentiment = body.get("sentiment", "")
        recommendations = body.get("recommendations", "")
        csat = body.get("csat", "")

        # -----------------------------
        # Create Item
        # -----------------------------
        item = {
            "review_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "review": review,
            "sentiment": sentiment,
            "csat": str(csat),
            "recommendations": recommendations
        }

        # -----------------------------
        # Save to DynamoDB
        # -----------------------------
        table.put_item(Item=item)

        # -----------------------------
        # Success Response
        # -----------------------------
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Review stored successfully.",
                "review_id": item["review_id"]
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }