import streamlit as st
from urllib.parse import urlencode
import requests


class DiamondPricePredictor:
    def __init__(self, model_endpoint):
        self.model_endpoint = model_endpoint

    def get_diamond_data(self) -> dict:
        """
        Logic for handling user input method
        Returns: dict containing user input

        """
        carat = st.slider("Carat", 0.5, 3.0, 1.0)
        cut = st.selectbox("Cut", ["Fair", "Good", "Very_Good", "Premium", "Ideal"])
        color = st.selectbox("Color", ["J", "I", "H", "G", "F", "E", "D"])
        clarity = st.selectbox(
            "Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
        )
        depth = st.slider("Total Depth Percentage", 55.0, 65.0, 60.0)
        table = st.slider("Table Width", 43.0, 95.0, 55.0)
        x = st.slider("Length (mm)", 1.0, 10.0, 5.0)
        y = st.slider("Width (mm)", 1.0, 10.0, 5.0)
        z = st.slider("Depth (mm)", 1.0, 6.0, 3.0)

        return {
            "carat": carat,
            "cut": cut,
            "color": color,
            "clarity": clarity,
            "depth": depth,
            "table": table,
            "x": x,
            "y": y,
            "z": z,
        }

    def predict_price(self, diamond_data):
        """
        Call inference endpoint
        Args:
            diamond_data: user_input

        Returns:

        """
        url_params = urlencode(diamond_data)
        response = requests.get(f"{self.model_endpoint}?{url_params}")

        if response.status_code == 200:
            prediction_result = response.json()["prediction"]
            st.success(f"### PRICE: {prediction_result}")
        else:
            st.error(
                f"Error in prediction request. Status Code: {response.status_code}."
            )


if __name__ == "__main__":
    MODEL_ENDPOINT = "https://diamonds-jcvkxdo2ba-lz.a.run.app/diamond_price"
    st.set_page_config(page_title="Diamond Price Prediction App", page_icon="💎")

    overview = st.container()
    content = st.container()
    prediction = st.container()

    with open("styles.css", "r") as css_file:
        css_code = css_file.read()

    st.markdown(
        f"""
        <style>
            {css_code}
        </style>
    """,
        unsafe_allow_html=True,
    )

    with overview:
        st.markdown(
            "<div class='diamond-info'>"
            "<h1>💎 Diamond Price Prediction 💎</h1>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<i class='fas fa-ruler' style='font-size: 48px; color: white;'></i>",
            unsafe_allow_html=True,
        )

    with content:
        st.markdown("### Enter diamond information below:")
        predictor = DiamondPricePredictor(MODEL_ENDPOINT)
        diamond_data = predictor.get_diamond_data()

    with prediction:
        if st.button("Predict Price"):
            predictor.predict_price(diamond_data)
