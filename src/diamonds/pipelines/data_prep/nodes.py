"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Tuple
from sklearn.model_selection import  train_test_split
def remove_index(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Removes index column from raw .csv datasets
    Args:
        data: raw dataset

    Returns: dataset without an index column

    '''
    data = data.reset_index(drop=True)
    data = data.iloc[:, 1:]
    return data

def remove_outliers(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Removes outlier records for selected numerical columns
    Args:
        data: input dataset

    Returns: dataset without outliers

    '''
    num_cols = ['x','y','z','depth','carat']
    for col_name in num_cols:
        q1 = data[col_name].quantile(0.25)
        q3 = data[col_name].quantile(0.75)
        iqr = q3 - q1
        cond = (data[col_name] <= q3 + 1.5 * iqr) & (data[col_name] >= q1 - 1.5 * iqr)
        data = data[cond]

    return data


def encode_labels(data: pd.DataFrame) -> Tuple[pd.DataFrame, LabelEncoder]:
    '''
    Encodes categorical features with LabelEncoder
    Args:
        data: input dataframe

    Returns: encoded dataset, encoder

    '''
    cat_col_names = data.select_dtypes(include=['object']).columns.tolist()
    encoder = LabelEncoder()
    for col in cat_col_names:
        data[col] = encoder.fit_transform(data[col])
    return data, encoder

def split_data(data: pd.DataFrame) -> Tuple:
    '''
    Loads enocded data and split it using train_test_split
    Args:
        data: input data

    Returns: X_train, X_test, y_train, y_test - standard convetion
    '''
    price = data.price
    data = data.drop(['price'],axis=1)
    X_train, X_test, y_train, y_test = train_test_split(data, price, test_size=0.2, random_state=1)

    return X_train, X_test, y_train, y_test
def standardize_train():
    pass
def standardize_test():
    pass
