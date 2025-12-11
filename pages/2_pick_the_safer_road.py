import random
import streamlit as st
import pandas as pd
from utils.ml_utils import load_model, predict_risk

# ------------------ CONSTANTS ------------------
DISPLAY_COLS = [
    "speed_limit",
    "num_lanes",
    "weather",
    "lighting",
    "road_type",
    "curvature",
    "time_of_day"
]

ROAD_OPTIONS = {
    "num_lanes": [1, 2, 3, 4],
    "curvature": (0, 15),  # (min, max)
    "speed_limit": [40, 60, 80, 100, 120],
    "num_reported_accidents": (0, 5),
    "road_type": ["highway", "rural", "urban"],
    "lighting": ["daylight", "dim", "night"],
    "weather": ["clear", "foggy", "rainy"],
    "time_of_day": ["morning", "afternoon", "evening"],
}

# ------------------ LOAD MODEL/DATA ------------------
model = load_model()
df = pd.read_csv("data/train.csv")

# ------------------ HELPERS ------------------
def generate_random_road():
    """Generate a random road sample for the game."""
    road = {
        "num_lanes": random.choice(ROAD_OPTIONS["num_lanes"]),
        "curvature": random.randint(*ROAD_OPTIONS["curvature"]),
        "speed_limit": random.choice(ROAD_OPTIONS["speed_limit"]),
        "num_reported_accidents": random.randint(*ROAD_OPTIONS["num_reported_accidents"]),
        "road_type": random.choice(ROAD_OPTIONS["road_type"]),
        "lighting": random.choice(ROAD_OPTIONS["lighting"]),
        "weather": random.choice(ROAD_OPTIONS["weather"]),
        "time_of_day": random.choice(ROAD_OPTIONS["time_of_day"]),
    }

    # Compute ML risk
    road["accident_risk"] = predict_risk(model,
        road["num_lanes"], road["curvature"], road["speed_limit"],
        road["num_reported_accidents"], road["road_type"],
        road["lighting"], road["weather"], road["time_of_day"]
    )
    return road


def new_round():
    st.session_state.road_a = generate_random_road()
    st.session_state.road_b = generate_random_road()


def submit_guess():
    road_a = st.session_state.road_a
    road_b = st.session_state.road_b

    safer = "Road A" if road_a["accident_risk"] < road_b["accident_risk"] else "Road B"
    user_pick = st.session_state.user_choice

    if user_pick == safer:
        st.success("Correct! ✅")
        st.session_state.score += 1
    else:
        st.error("Incorrect ❌")

    st.write(
        f"Road A risk: {road_a['accident_risk']:.2f}, "
        f"Road B risk: {road_b['accident_risk']:.2f}"
    )


def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show_card(label, road):
    st.subheader(label)
    fields_html = "".join(
        f"<p><strong>{col.replace('_',' ').title()}:</strong> {road[col]}</p>"
        for col in DISPLAY_COLS
    )

    st.markdown(f"<div class='card'>{fields_html}</div>", unsafe_allow_html=True)


# ------------------ SESSION STATE ------------------
st.session_state.setdefault("score", 0)
st.session_state.setdefault("user_choice", "Road A")

if "road_a" not in st.session_state:
    new_round()

# ------------------ UI ------------------
load_css()

st.title("🚦 Pick the Safer Road")
st.markdown("Choose which road you think is safer.")
st.markdown(f"### ⭐ Score: **{st.session_state.score}**")

col1, col2 = st.columns(2)
with col1:
    show_card("🛣️ Road A", st.session_state.road_a)
with col2:
    show_card("🛣️ Road B", st.session_state.road_b)

st.radio("Which road is safer?", ("Road A", "Road B"), key="user_choice")

btn1, btn2 = st.columns(2)
with btn1:
    st.button("Submit Guess", on_click=submit_guess)
with btn2:
    st.button("Next Round", on_click=new_round)
