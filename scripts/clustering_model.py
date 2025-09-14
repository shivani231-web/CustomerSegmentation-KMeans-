import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

INPUT = "data/processed/cleaned_data.csv"
OUTPUT = "data/processed/clustered_data.csv"

def main():
    df = pd.read_csv(INPUT)
    print("✅ Processed data loaded:", df.shape)

    # Features for clustering
    features = ["Age", "Annual_Income_(k$)", "Spending_Score_(1-100)", "Gender_encoded"]
    X = df[features]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply KMeans
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # Save clustered data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print("💾 Saved clustered data to:", OUTPUT)
    print("🔍 Cluster counts:\n", df["Cluster"].value_counts())

    # Visualize Income vs Spending Score
    plt.scatter(df["Annual_Income_(k$)"], df["Spending_Score_(1-100)"], 
                c=df["Cluster"], cmap="viridis")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.title("Customer Segments")
    plt.show()

if __name__ == "__main__":
    main()
