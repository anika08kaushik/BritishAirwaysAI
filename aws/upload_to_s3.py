import boto3
import os

BUCKET_NAME = "british-airways-ai-anika"

s3 = boto3.client("s3", region_name="ap-south-1")

files = [
    ("dataset/british_airways_reviews.csv", "raw/british_airways_reviews.csv"),
    ("dataset/final_reviews.csv", "processed/final_reviews.csv"),
    ("model/saved_models/csat_model.pkl", "models/csat_model.pkl"),
    ("model/saved_models/tfidf_vectorizer.pkl", "models/tfidf_vectorizer.pkl")
]

print("=" * 60)
print("Uploading Files to Amazon S3")
print("=" * 60)

for local_file, s3_key in files:

    if os.path.exists(local_file):

        print(f"Uploading {local_file}")

        s3.upload_file(
            local_file,
            BUCKET_NAME,
            s3_key
        )

        print("Uploaded Successfully\n")

    else:

        print(f"{local_file} not found\n")

print("=" * 60)
print("All uploads completed.")