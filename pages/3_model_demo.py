import streamlit as st
from utils.ml_utils import load_model, predict_risk

# Load model once
model = load_model()

st.title("Model Demo")

# Example inputs
road_type = 1
lighting = 2
weather = 3
time_of_day = 1
num_lanes = 2
curvature = 5
speed_limit = 80
num_reported_accidents = 0

risk = predict_risk(model, road_type, lighting, weather, time_of_day, num_lanes, curvature, speed_limit, num_reported_accidents)
st.write(f"Predicted Accident Risk: {risk:.2f}")
