import pandas as pd

INPUT_FILE = "dataset/british_airways_reviews.csv"
OUTPUT_FILE = "dataset/cleaned_reviews.csv"


def clean_dataset():

    print("=" * 60)
    print("Loading British Airways Dataset...")
    print("=" * 60)

    df = pd.read_csv(INPUT_FILE)

    print("\nInitial Shape :", df.shape)

    # Remove unwanted index column
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    # Remove missing values
    df.dropna(inplace=True)

    # Remove duplicate reviews
    df.drop_duplicates(subset=["reviews"], inplace=True)

    # Remove empty reviews
    df = df[df["reviews"].str.strip() != ""]

    # Remove extra spaces
    df["reviews"] = (
        df["reviews"]
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    df["title"] = (
        df["title"]
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    df.reset_index(drop=True, inplace=True)

    print("\nDataset Information")
    print(df.info())

    print("\nFinal Shape :", df.shape)

    print("\nFirst Five Records")
    print(df.head())

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nClean dataset saved successfully.")
    print("Location :", OUTPUT_FILE)


if __name__ == "__main__":
    clean_dataset()