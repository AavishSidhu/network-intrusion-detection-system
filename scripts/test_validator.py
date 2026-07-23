from src.data.loader import load_dataset
from src.data.validator import validate_dataset

train_df, test_df = load_dataset()

validate_dataset(train_df, "Training")
validate_dataset(test_df, "Testing")