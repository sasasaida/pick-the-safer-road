import streamlit as st
import pandas as pd

# Load dataset once (still runs each script run, but reading is cheap if small)
df = pd.read_csv("data/train.csv")

# --- helpers ---
def new_round():
    roads = df.sample(n=2, random_state=None)
    st.session_state.road_a = roads.iloc[0]
    st.session_state.road_b = roads.iloc[1]

def submit_guess():
    # compute safer using the roads currently stored
    road_a = st.session_state.road_a
    road_b = st.session_state.road_b
    safer = "Road A" if road_a["speed_limit"] < road_b["speed_limit"] else "Road B"
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
with col2:
    st.header("Road B")
    st.text(f"Speed limit: {st.session_state.road_b['speed_limit']}")

# Radio is linked to st.session_state.user_choice so its value persists
st.radio("Which road is safer?", ("Road A", "Road B"), key="user_choice")

# Buttons use callbacks to mutate session_state without risk of accidental resampling
col3, col4 = st.columns(2)
with col3:
    st.button("Submit Guess", on_click=submit_guess)
with col4:
    st.button("Next Round", on_click=new_round)
