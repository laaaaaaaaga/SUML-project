"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.14
"""
# ag test
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import remove_index, remove_outliers, encode_labels, split_data, standardize_train
from .nodes import standardize_test, train_model, evaluate_model,plot_metrics, train_autogluon,evaluate_autogluon, plot_metrics_autogluon
import seaborn

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=remove_index,
             inputs='diamonds',
             outputs='index_removed',
             name="remove_index_node"),

        node(func=remove_outliers,
             inputs='index_removed',
             outputs=['outliers_removed','outlier_table'],
             name='remove_outliers_node'),

        node(func=encode_labels,
             inputs='outliers_removed',
             outputs=['labels_encoded','ordinal_encoder'],
             name='encode_labels_node'),

        node(func=split_data,
             inputs='labels_encoded',
             outputs=['X_train','X_test','y_train','y_test'],
             name='split_data_node'),

        node(func=standardize_train,
             inputs='X_train',
             outputs=['X_train_scaled', 'scaler'],
             name='standardize_train_node'),

        node(func=standardize_test,
             inputs=['X_test','scaler'],
             outputs='X_test_scaled',
             name='standardize_test_node'),

        node(func=train_model,
             inputs=['X_train_scaled', 'y_train'],
             outputs='model',
             name='train_model_node'),
        node(func=train_autogluon,
             inputs=['X_train_scaled', 'y_train'],
             outputs='autogluon',
             name='train_autogluon_node'),

        node(func=evaluate_model,
             inputs=['X_train_scaled', 'X_test_scaled','y_train','y_test','model'],
             outputs='metrics',
             name='evaluate_model_node'),
        node(func=evaluate_autogluon,
             inputs=['X_train_scaled', 'X_test_scaled', 'y_train', 'y_test', 'autogluon'],
             outputs='metrics_autogluon',
             name='evaluate_autogluon_node'),
        node(func=plot_metrics,
             inputs='metrics',
             outputs='metrics_plot',
             name='plot_metrics_node'),
        node(func=plot_metrics_autogluon,
             inputs='metrics_autogluon',
             outputs='metrics_plot_autogluon',
             name='plot_metrics_autogluon_node'),

    ])
