import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

INPUT = "data/processed/clustered_data.csv"

def main():
    df = pd.read_csv(INPUT)
    print("✅ Clustered data loaded:", df.shape)

    # Compute correlation
    corr = df.corr(numeric_only=True)

    # Heatmap
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    main()
