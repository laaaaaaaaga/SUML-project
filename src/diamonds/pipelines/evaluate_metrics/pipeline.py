"""
This is a boilerplate pipeline 'evaluate_metrics'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import evaluate_autogluon, plot_metrics_autogluon


def create_pipeline(**kwargs) -> Pipeline:
    """
    Creates model evaluation pipeline
    Args:
        **kwargs:

    Returns:

    """
    return pipeline(
        [
            node(
                func=evaluate_autogluon,
                inputs=[
                    "X_train_scaled",
                    "X_test_scaled",
                    "y_train",
                    "y_test",
                    "autogluon",
                ],
                outputs="metrics_autogluon",
                name="evaluate_autogluon_node",
            ),
            node(
                func=plot_metrics_autogluon,
                inputs="metrics_autogluon",
                outputs="metrics_plot_autogluon",
                name="plot_metrics_autogluon_node",
            ),
        ]
    )
