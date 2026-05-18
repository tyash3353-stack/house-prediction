import streamlit as st
import joblib
import pandas as pd

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict"):

    input_data = pd.DataFrame({
        'Area': [area],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Price: {prediction[0]}")