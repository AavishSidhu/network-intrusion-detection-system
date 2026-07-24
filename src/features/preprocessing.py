import pandas as pd

from src.features.encoding import (
    encode_target,
    encode_categorical_features,
)


def preprocess_dataset(df: pd.DataFrame):
    """
    Complete preprocessing pipeline.
    """

    df, target_encoder = encode_target(df)

    df, categorical_encoder = encode_categorical_features(df)

    return (
        df,
        target_encoder,
        categorical_encoder,
    )