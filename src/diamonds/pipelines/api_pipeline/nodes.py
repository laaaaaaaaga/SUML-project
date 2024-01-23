import pandas as pd


class MLPredictor:
    def __init__(self, model, ordinal_encoder, scaler):
        self.model = model
        self.ordinal_encoder = ordinal_encoder
        self.scaler = scaler

    def encode_labels(self, api_data: pd.DataFrame):
        '''
        Encodes user input into integer data
        Args:
            api_data:

        Returns:

        '''
        df_args_encoded = api_data
        df_args_encoded[["cut", "color", "clarity"]] = self.ordinal_encoder.transform(
            api_data[["cut", "color", "clarity"]]
        )
        return df_args_encoded

    def scale_data(self, api_data: pd.DataFrame):
        '''
        Standardizes the user input
        Args:
            api_data:

        Returns:

        '''
        df_args = api_data
        scaled_array = self.scaler.transform(df_args)
        scaled = pd.DataFrame(scaled_array, columns=df_args.columns)
        return scaled

    def predict(self, api_data: pd.DataFrame, context):
        '''
        Main inference method. Return a float price prediction.
        Args:
            api_data:
            context:

        Returns:

        '''
        df_args = api_data
        encoded_labels = self.encode_labels(df_args)
        scaled = self.scale_data(encoded_labels)

        prediction = int(self.model.predict(scaled).iloc[0])
        return {"prediction": prediction}


def save_predictor(model, ordinal_encoder, scaler) -> MLPredictor:
    '''
    Method that return a predictor. To be used in a pipeline
    Args:
        model:
        ordinal_encoder:
        scaler:

    Returns:

    '''
    predictor = MLPredictor(model, ordinal_encoder, scaler)
    return predictor
