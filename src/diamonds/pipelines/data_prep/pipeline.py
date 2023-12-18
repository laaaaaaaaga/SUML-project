"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import remove_index, remove_outliers, encode_labels, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=remove_index,
             inputs='diamonds',
             outputs='index_removed',
             name="remove_index_node"),

        node(func=remove_outliers,
             inputs='index_removed',
             outputs='outliers_removed',
             name='remove_outliers_node'),
        node(func=encode_labels,
             inputs='outliers_removed',
             outputs=['labels_encoded','label_encoder'],
             name='encode_labels_node'),
        node(func=split_data,
             inputs='labels_encoded',
             outputs=['X_train','X_test','y_train','y_test'],
             name='split_data_node'),
    ])
