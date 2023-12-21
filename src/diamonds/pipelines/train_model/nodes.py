"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.14
"""
import pandas as pd
from autogluon.tabular import TabularPredictor, TabularDataset


def train_autogluon(
    X_train_scaled: pd.DataFrame, y_train: pd.DataFrame
) -> TabularPredictor:
    """
    Train a TabularPredictor
    Args:
        X_train_scaled:
        y_train:

    Returns:
    """
    train_data_df: pd.DataFrame = pd.concat(
        [X_train_scaled, y_train], axis=1
    ).reset_index(drop=True)
    train_data: TabularDataset = TabularDataset(train_data_df)
    predictor: TabularPredictor = TabularPredictor(label="price").fit(train_data)

    return predictor
