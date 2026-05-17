import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")

area = st.number_input("Enter Area")
bedrooms = st.number_input("Enter Bedrooms")

if st.button("Predict Price"):

    features = np.array([[area, bedrooms]])

    prediction = model.predict(features)

    st.success(f"Predicted Price: {prediction[0]}")