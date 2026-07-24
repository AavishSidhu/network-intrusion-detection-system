from src.data.loader import load_dataset
from src.features.encoding import encode_categorical_features

train_df, _ = load_dataset()

encoded_df, encoder = encode_categorical_features(train_df)

print(encoded_df.shape)

print()

print(encoded_df.head())