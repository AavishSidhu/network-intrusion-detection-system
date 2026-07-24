import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


def encode_target(df: pd.DataFrame):
    """
    Encode target labels.
    """

    encoder = LabelEncoder()

    df = df.copy()

    df["target"] = encoder.fit_transform(df["label"])

    return df, encoder


def encode_categorical_features(df: pd.DataFrame):
    """
    One-hot encode categorical features.
    """

    categorical_columns = [
        "protocol_type",
        "service",
        "flag",
    ]

    encoder = OneHotEncoder(
        sparse_output=False,
        handle_unknown="ignore",
    )

    encoded = encoder.fit_transform(
        df[categorical_columns]
    )

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(
            categorical_columns
        ),
        index=df.index,
    )

    df = df.drop(columns=categorical_columns)

    df = pd.concat(
        [df, encoded_df],
        axis=1,
    )

    return df, encoder