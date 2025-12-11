import pickle
import numpy as np
import streamlit as st

@st.cache_resource
def load_model():
    with open("model/my_model_2.pkl", "rb") as f:
        model = pickle.load(f)
    return model


def one_hot(value, categories):
    """Convert a single categorical value to a one-hot list."""
    return [1 if value == cat else 0 for cat in categories]


def predict_risk(model, num_lanes, curvature, speed_limit, num_reported_accidents,
                 road_type, lighting, weather, time_of_day):
    # Define categories exactly as used in training
    road_types = ["highway", "rural", "urban"]
    lightings = ["daylight", "dim", "night"]
    weathers = ["clear", "foggy", "rainy"]
    times_of_day = ["morning", "afternoon", "evening"]

    # Build feature vector
    features = (
            [num_lanes, curvature, speed_limit, num_reported_accidents] +
            one_hot(road_type, road_types) +
            one_hot(lighting, lightings) +
            one_hot(weather, weathers) +
            one_hot(time_of_day, times_of_day)
    )

    features = np.array([features])
    risk_score = model.predict(features)[0]
    return risk_score
