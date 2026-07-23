from src.data.loader import load_dataset

train_df, test_df = load_dataset()

print("Training Shape:", train_df.shape)
print("Testing Shape:", test_df.shape)

print()
print(train_df.head())