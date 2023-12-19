"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from typing import Tuple
from sklearn.model_selection import  train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot  as plt
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


def encode_labels(data: pd.DataFrame) -> Tuple[pd.DataFrame, OrdinalEncoder]:
    '''
    Encodes categorical features with LabelEncoder
    Args:
        data: input dataframe

    Returns: encoded dataset, encoder

    '''
    cat_col_names = data.select_dtypes(include=['object']).columns.tolist()
    encoder = OrdinalEncoder()
    data[cat_col_names] = encoder.fit_transform(data[cat_col_names])
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
def standardize_train(X_train: pd.DataFrame) -> Tuple[pd.DataFrame, StandardScaler]:
    '''
    Performs scaling on training dataset using StandardScaler
    Args:
        X_train: input dataframe

    Returns: standardized X_train and the Scaler

    '''
    scaler = StandardScaler().fit(X_train)

    X_train_scaled_array = scaler.transform(X_train)
    X_train_scaled = pd.DataFrame(X_train_scaled_array, columns=X_train.columns)

    return X_train_scaled, scaler
def standardize_test(X_test: pd.DataFrame, scaler: StandardScaler) -> pd.DataFrame:
    '''
    Standardizes X_test using fitted earlier StandardScaler
    Args:
        X_test: input data
        scaler: input StandardScaler

    Returns: X_test_scaled - scaled test data

    '''
    X_test_scaled_array= scaler.transform(X_test)
    X_test_scaled= pd.DataFrame(X_test_scaled_array, columns=X_test.columns)

    return X_test_scaled

def train_model(X_train_scaled: pd.DataFrame, y_train: pd.DataFrame) -> XGBRegressor:
    model = XGBRegressor()
    model.fit(X_train_scaled, y_train)
    return model

def evaluate_model(X_train_scaled: pd.DataFrame, X_test_scaled: pd.DataFrame,
                   y_train: pd.DataFrame, y_test: pd.DataFrame,
                   model: XGBRegressor) -> pd.DataFrame:
    '''
    Creates a summary comparision of train and test metrics
    Args:
        X_train_scaled:
        X_test_scaled:
        y_train:
        y_test:
        model:

    Returns: dataframe containing standard regression metrics for train and test datasets

    '''
    metrics = pd.DataFrame(index=['Train', 'Test'], columns=['MSE', 'R2_score', 'MAE'])
    train_pred = model.predict(X_train_scaled)
    test_pred = model.predict(X_test_scaled)

    metrics.loc['Train', 'MSE'] = mean_squared_error(y_train, train_pred)
    metrics.loc['Train', 'R2_score'] = r2_score(y_train, train_pred)
    metrics.loc['Train', 'MAE'] = mean_absolute_error(y_train, train_pred)

    metrics.loc['Test', 'MSE'] = mean_squared_error(y_test, test_pred)
    metrics.loc['Test', 'R2_score'] = r2_score(y_test, test_pred)
    metrics.loc['Test', 'MAE'] = mean_absolute_error(y_test, test_pred)

    return metrics

def plot_metrics(metrics: pd.DataFrame):
    '''
    Plots metrics from the evalution node
    Args:
        metrics:

    Returns:

    '''
    fig, ax = plt.subplots(figsize=(20, 15))
    metrics[['MSE', 'R2_score', 'MAE']].plot(kind='bar', ax=ax, subplots=True, rot=0)
    ax.set_ylabel('Values')
    ax.set_title('Comparison of Train and Test Metrics')

    plt.legend(title='Metrics')

    return fig