import random
import streamlit as st
import pandas as pd
from utils.ml_utils import load_model, predict_risk

model = load_model()

# Load dataset once (still runs each script run, but reading is cheap if small)
df = pd.read_csv("data/train.csv")

# --- helpers ---

def generate_random_road():
    """Generate a random road sample for the game."""
    # For demo, pick numeric and categorical features randomly
    road = {
        "num_lanes": random.choice([1, 2, 3, 4]),
        "curvature": random.randint(0, 15),
        "speed_limit": random.choice([40, 60, 80, 100, 120]),
        "num_reported_accidents": random.randint(0, 5),
        "road_type": random.choice(["highway", "rural", "urban"]),
        "lighting": random.choice(["daylight", "dim", "night"]),
        "weather": random.choice(["clear", "foggy", "rainy"]),
        "time_of_day": random.choice(["morning", "afternoon", "evening"]),
    }
    # Compute predicted risk using your ML model
    road["accident_risk"] = predict_risk(
        model,
        road["num_lanes"], road["curvature"], road["speed_limit"], road["num_reported_accidents"],
        road["road_type"], road["lighting"], road["weather"], road["time_of_day"]
    )
    return road

def new_round():
    st.session_state.road_a = generate_random_road()
    st.session_state.road_b = generate_random_road()

def submit_guess():
    # compute safer using the roads currently stored
    road_a = st.session_state.road_a
    road_b = st.session_state.road_b
    safer = "Road A" if road_a["accident_risk"] < road_b["accident_risk"] else "Road B"
    if st.session_state.user_choice == safer:
        st.success("Correct! ✅")
        st.session_state.score += 1
    else:
        st.error("Incorrect ❌")

# --- session defaults ---
st.session_state.setdefault("score", 0)
if "road_a" not in st.session_state or "road_b" not in st.session_state:
    new_round()
# ensure a default for the radio selection so submit can use it
st.session_state.setdefault("user_choice", "Road A")

# --- UI ---
st.title("Pick the Safer Road!")
st.write("Choose which road you think is safer based on the given attributes.")
st.write(f"Score: {st.session_state.score}")

col1, col2 = st.columns(2)
with col1:
    st.header("Road A")
    st.text(f"Speed limit: {st.session_state.road_a['speed_limit']}")
    st.text(f"Lanes: {st.session_state.road_a['num_lanes']}")
    st.text(f"Curvature: {st.session_state.road_a['curvature']}")
with col2:
    st.header("Road B")
    st.text(f"Speed limit: {st.session_state.road_b['speed_limit']}")
    st.text(f"Lanes: {st.session_state.road_b['num_lanes']}")
    st.text(f"Curvature: {st.session_state.road_b['curvature']}")

# Radio is linked to st.session_state.user_choice so its value persists
st.radio("Which road is safer?", ("Road A", "Road B"), key="user_choice")

# Buttons use callbacks to mutate session_state without risk of accidental resampling
col3, col4 = st.columns(2)
with col3:
    st.button("Submit Guess", on_click=submit_guess)
with col4:
    st.button("Next Round", on_click=new_round)
