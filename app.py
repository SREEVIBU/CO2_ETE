import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- Streamlit Page Config ---
st.set_page_config(page_title="CO₂ Emission Prediction App", page_icon="🌍", layout="centered")

st.title("🌍 CO₂ Emission Prediction App")
st.write("Enter the vehicle specifications below to predict **CO₂ Emissions (g/km)**.")

# --- Load Model ---
with open("models.pkl", "rb") as f:
    models = pickle.load(f)
model=models['KNeighborsRegressor']
# --- Input Fields ---
engine_size = st.number_input("Engine Size (L)", min_value=0.0, step=0.1)
cylinders = st.number_input("Cylinders", min_value=1, step=1)
fuel_city = st.number_input("Fuel Consumption City (L/100 km)", min_value=0.0, step=0.1)
fuel_hwy = st.number_input("Fuel Consumption Hwy (L/100 km)", min_value=0.0, step=0.1)
fuel_comb = st.number_input("Fuel Consumption Comb (L/100 km)", min_value=0.0, step=0.1)
fuel_comb_mpg = st.number_input("Fuel Consumption Comb (mpg)", min_value=0.0, step=0.1)

# --- Prediction Button ---
if st.button("🔍 Predict CO₂ Emissions"):
    try:
        features = np.array([[engine_size, cylinders, fuel_city, fuel_hwy, fuel_comb, fuel_comb_mpg]])
        prediction = model.predict(features)
        st.success(f"🚗 Estimated CO₂ Emission: **{prediction[0]:.2f} g/km**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Machine Learning.")
