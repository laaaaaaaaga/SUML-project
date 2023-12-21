"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from typing import Tuple
from sklearn.model_selection import train_test_split


def remove_index(data: pd.DataFrame) -> pd.DataFrame:
    """
    Removes index column from raw .csv datasets
    Args:
        data: raw dataset

    Returns: dataset without an index column

    """

    data = data.iloc[:, 1:]
    return data


def remove_outliers(data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Removes outlier records for selected numerical columns
    Args:
        data: input dataset

    Returns: dataset without outliers

    """

    num_cols = ["x", "y", "z", "depth", "carat"]
    outlier_table = pd.DataFrame(index=num_cols, columns=["low", "high"])
    for col_name in num_cols:
        q1 = data[col_name].quantile(0.25)
        q3 = data[col_name].quantile(0.75)
        iqr = q3 - q1
        high = q3 + 1.5 * iqr
        low = q1 - 1.5 * iqr
        cond = (data[col_name] <= high) & (data[col_name] >= low)
        data = data[cond]

        outlier_table.loc[col_name, "low"] = low
        outlier_table.loc[col_name, "high"] = high

    return data, outlier_table


def encode_labels(data: pd.DataFrame) -> Tuple[pd.DataFrame, OrdinalEncoder]:
    """
    Encodes categorical features with LabelEncoder
    Args:
        data: input dataframe

    Returns: encoded dataset, encoder

    """
    cat_col_names = data.select_dtypes(include=["object"]).columns.tolist()
    encoder = OrdinalEncoder()
    data[cat_col_names] = encoder.fit_transform(data[cat_col_names])
    return data, encoder


def split_data(data: pd.DataFrame) -> Tuple:
    """
    Loads encoded data and split it using train_test_split
    Args:
        data: input data

    Returns: X_train, X_test, y_train, y_test - standard convention
    """
    price = data.price
    data = data.drop(["price"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        data, price, test_size=0.2, random_state=1
    )

    return X_train, X_test, y_train, y_test


def standardize_train(X_train: pd.DataFrame) -> Tuple[pd.DataFrame, StandardScaler]:
    """
    Performs scaling on training dataset using StandardScaler
    Args:
        X_train: input dataframe

    Returns: standardized X_train and the Scaler

    """
    scaler: StandardScaler = StandardScaler()
    scaler = scaler.fit(X_train)

    X_train_scaled_array = scaler.transform(X_train)
    X_train_scaled = pd.DataFrame(X_train_scaled_array, columns=X_train.columns)

    return X_train_scaled, scaler


def standardize_test(X_test: pd.DataFrame, scaler: StandardScaler) -> pd.DataFrame:
    """
    Standardizes X_test using fitted earlier StandardScaler
    Args:
        X_test: input data
        scaler: input StandardScaler

    Returns: X_test_scaled - scaled test data

    """
    X_test_scaled_array = scaler.transform(X_test)
    X_test_scaled = pd.DataFrame(X_test_scaled_array, columns=X_test.columns)

    return X_test_scaled
