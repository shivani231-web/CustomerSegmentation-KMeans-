import pandas as pd
import os

RAW = "data/raw/Mall_Customers.csv"
PROCESSED = "data/processed/cleaned_data.csv"

def main():
    # Load dataset
    df = pd.read_csv(RAW)
    print("✅ Raw data shape:", df.shape)
    print("📊 Columns:", df.columns.tolist())

    # Rename columns: remove spaces, replace with underscore
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Encode Genre column (Male=0, Female=1)
    df["Gender_encoded"] = df["Genre"].map({"Male": 0, "Female": 1})

    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED, index=False)
    print("💾 Saved cleaned data to:", PROCESSED)
    print("🔍 Preview:\n", df.head())

if __name__ == "__main__":
    main()
