import streamlit as st

st.title("Hello!")
st.header("Welcome to Safer Roads App")
st.subheader("Explore accident data interactively")
st.write("Use the sidebar to select columns and explore stats")


def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
