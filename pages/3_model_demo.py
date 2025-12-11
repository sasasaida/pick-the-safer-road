import streamlit as st
import numpy as np
import pickle
from utils.ml_utils import predict_risk, load_model

# Load model once
model = load_model()

st.title("Safer Roads Model Demo")
st.header("Predict Accident Risk for a Road Segment")
st.write("Select the road conditions below:")

# ---------------------------
# Streamlit inputs
# ---------------------------

num_lanes = st.number_input("Number of Lanes", min_value=1, max_value=10, value=2)
curvature = st.number_input("Road Curvature (degrees)", min_value=0, max_value=90, value=5)
speed_limit = st.number_input("Speed Limit (km/h)", min_value=20, max_value=150, value=80)
num_reported_accidents = st.number_input("Number of Reported Accidents", min_value=0, value=0)

road_type = st.selectbox("Road Type", ["highway", "rural", "urban"])
lighting = st.selectbox("Lighting Condition", ["daylight", "dim", "night"])
weather = st.selectbox("Weather Condition", ["clear", "foggy", "rainy"])
time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "evening"])

# ---------------------------
# Predict button
# ---------------------------

if st.button("Predict Risk"):
    risk_score = predict_risk(
        model,
        num_lanes, curvature, speed_limit, num_reported_accidents,
        road_type, lighting, weather, time_of_day
    )

    st.subheader("Predicted Accident Risk")
    st.write(f"**{risk_score:.2f}**")  # Display risk score rounded to 2 decimals
