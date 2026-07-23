import pandas as pd


def validate_dataset(df: pd.DataFrame, dataset_name: str) -> None:
    print("=" * 60)
    print(f"{dataset_name} Dataset Report")
    print("=" * 60)

    print(f"\nShape: {df.shape}")

    print("\nMissing Values")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nColumn Types")
    print(df.dtypes)

    print("\nLabel Distribution")
    print(df["label"].value_counts())

    print("\nMemory Usage")
    memory = df.memory_usage(deep=True).sum() / (1024 ** 2)
    print(f"{memory:.2f} MB")

    print("\n" + "=" * 60)