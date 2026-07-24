from src.data.loader import load_dataset
from src.features.preprocessing import preprocess_dataset

train_df, _ = load_dataset()

processed_df, target_encoder, categorical_encoder = preprocess_dataset(train_df)

print(processed_df.shape)

print()

print(processed_df.head())