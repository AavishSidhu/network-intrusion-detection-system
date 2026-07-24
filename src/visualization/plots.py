import matplotlib.pyplot as plt
import pandas as pd


def plot_attack_distribution(df: pd.DataFrame):
    attack_counts = df["label"].value_counts()

    plt.figure(figsize=(14, 6))

    attack_counts.plot(kind="bar")

    plt.title("Attack Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Number of Samples")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()