"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""
# ag test
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import (
    remove_index,
    change_cut,
    remove_outliers,
    encode_labels,
    split_data,
    standardize_train,
    standardize_test,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=remove_index,
                inputs="diamonds",
                outputs="index_removed",
                name="remove_index_node",
            ),
            node(
                func=change_cut,
                inputs="index_removed",
                outputs="cut_changed",
                name="change_cut_node",
            ),
            node(
                func=remove_outliers,
                inputs="cut_changed",
                outputs=["outliers_removed", "outlier_table"],
                name="remove_outliers_node",
            ),
            node(
                func=encode_labels,
                inputs="outliers_removed",
                outputs=["labels_encoded", "ordinal_encoder"],
                name="encode_labels_node",
            ),
            node(
                func=split_data,
                inputs="labels_encoded",
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=standardize_train,
                inputs="X_train",
                outputs=["X_train_scaled", "scaler"],
                name="standardize_train_node",
            ),
            node(
                func=standardize_test,
                inputs=["X_test", "scaler"],
                outputs="X_test_scaled",
                name="standardize_test_node",
            ),
        ]
    )
