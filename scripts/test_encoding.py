from src.data.loader import load_dataset
from src.features.encoding import encode_target

train_df, _ = load_dataset()

encoded_df, encoder = encode_target(train_df)

print(encoded_df[["label", "target"]].head())

print("\nClasses:")
print(encoder.classes_)