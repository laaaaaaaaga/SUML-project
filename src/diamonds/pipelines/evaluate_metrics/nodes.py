"""
This is a boilerplate pipeline 'evaluate_metrics'
generated using Kedro 0.18.14
"""
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
from autogluon.tabular import TabularPredictor, TabularDataset
import pandas as pd


def evaluate_autogluon(
    X_train_scaled: pd.DataFrame,
    X_test_scaled: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
    predictor: TabularPredictor,
) -> pd.DataFrame:
    """

    Args:
        X_train_scaled:
        X_test_scaled:
        y_train:
        y_test:
        predictor:

    Returns:

    """
    metrics = pd.DataFrame(index=["Train", "Test"], columns=["MSE", "R2_score", "MAE"])

    train_data = TabularDataset(X_train_scaled)
    test_data = TabularDataset(X_test_scaled)

    train_pred = predictor.predict(train_data)
    test_pred = predictor.predict(test_data)

    metrics.loc["Train", "MSE"] = mean_squared_error(y_train, train_pred)
    metrics.loc["Train", "R2_score"] = r2_score(y_train, train_pred)
    metrics.loc["Train", "MAE"] = mean_absolute_error(y_train, train_pred)

    metrics.loc["Test", "MSE"] = mean_squared_error(y_test, test_pred)
    metrics.loc["Test", "R2_score"] = r2_score(y_test, test_pred)
    metrics.loc["Test", "MAE"] = mean_absolute_error(y_test, test_pred)
    return metrics


def plot_metrics_autogluon(metrics: pd.DataFrame):
    """
    Plots metrics from the evaluation node
    Args:
        metrics:

    Returns:

    """
    fig, ax = plt.subplots(figsize=(20, 15))
    metrics[["MSE", "R2_score", "MAE"]].plot(kind="bar", ax=ax, subplots=True, rot=0)
    ax.set_ylabel("Values")
    ax.set_title("Comparison of Train and Test Metrics")

    plt.legend(title="Metrics")
    plt.yticks(range(0, 300, 10))

    return fig
