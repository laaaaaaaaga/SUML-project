"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_autogluon


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_autogluon,
                inputs=["X_train_scaled", "y_train"],
                outputs="autogluon",
                name="train_autogluon_node",
            )
        ]
    )
