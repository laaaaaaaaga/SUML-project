"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from kedro.extras.datasets.pandas import CSVDataSet

def remove_index(data: pd.DataFrame) -> pd.DataFrame:
    data = data.reset_index(drop=True)
    data = data.iloc[:, 1:]
    return data

def onehot(data: pd.DataFrame) -> pd.DataFrame:
    cat_col_names = data.select_dtypes(include=['object']).columns.tolist()
    hot = OneHotEncoder()
    hot = hot.fit(data[cat_col_names].copy())
    encoded = hot.transform(data[cat_col_names].copy())
    column_names = hot.get_feature_names_out()
    hot_pd = pd.DataFrame(encoded.toarray(), columns=column_names)
    data = data.reset_index(drop=True)
    data = data.drop(cat_col_names, axis=1)
    data_con = pd.concat([data, hot_pd], axis=1)
    return data_con

def split_data():   
    pass
def standardize_train():
    pass
def standardize_test():
    pass
