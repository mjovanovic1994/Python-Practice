import streamlit as st
from rps import rps

options = ["rock", "paper", "scissors"]
chances = 10
if "results" not in st.session_state:
    st.session_state.results = []

st.title("Rock Paper Scissors")
user = st.selectbox("Choose:", options)

if st.button("Play"):
    result = rps(user)
    st.session_state.results.append(result)
    st.write(f"Result: **{result}**")

if len(st.session_state.results) >= chances:
    st.success(f"Results: {st.session_state.results}")
