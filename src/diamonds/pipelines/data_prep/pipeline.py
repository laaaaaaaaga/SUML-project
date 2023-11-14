"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import remove_index,onehot


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=remove_index,
             inputs='data1',
             outputs='data2',
             name="remove_index_noed"),
        node(func=onehot,
             inputs='data2',
             outputs='onehot_node',
             name='onehot_node')
    ])
