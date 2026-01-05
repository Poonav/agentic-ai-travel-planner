import streamlit as st
from agent import run_travel_agent

st.title("🧳 Agentic AI Travel Planner")

source = st.text_input("Source City", "Mumbai")
destination = st.text_input("Destination City", "Goa")
days = st.slider("Trip Duration (days)", 3, 7, 5)
budget = st.number_input("Budget (INR)", min_value=10000, value=50000)
interests = st.multiselect("Interests", ["Nature", "Adventure", "Historical", "Food", "Shopping"], default=["Nature", "Food"])

if st.button("Generate Itinerary"):
    user_input = {
        "source": source,
        "destination": destination,
        "days": days,
        "budget": budget,
        "interests": interests
    }

    result = run_travel_agent(user_input)
    st.json(result)
