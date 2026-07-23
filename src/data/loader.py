from pathlib import Path

import pandas as pd

from src.config.paths import RAW_DATA_DIR
from src.data.schema import COLUMN_NAMES


DATASET_DIR = RAW_DATA_DIR / "NSL-KDD"


def load_train_data() -> pd.DataFrame:
    train_path = DATASET_DIR / "KDDTrain+.txt"

    return pd.read_csv(
        train_path,
        names=COLUMN_NAMES,
    )


def load_test_data() -> pd.DataFrame:
    test_path = DATASET_DIR / "KDDTest+.txt"

    return pd.read_csv(
        test_path,
        names=COLUMN_NAMES,
    )


def load_dataset():
    train_df = load_train_data()
    test_df = load_test_data()

    return train_df, test_df