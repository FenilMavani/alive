import streamlit as st
from datetime import datetime, timedelta
import time

# Function to calculate time difference
def calculate_time_alive(birth_datetime):
    now = datetime.now()
    time_alive = now - birth_datetime
    weeks_alive = time_alive.days // 7
    days_alive = time_alive.days
    hours_alive = int(time_alive.total_seconds() // 3600)
    minutes_alive = int(time_alive.total_seconds() // 60)
    seconds_alive = int(time_alive.total_seconds())
    return weeks_alive, days_alive, hours_alive, minutes_alive, seconds_alive

# Streamlit app
st.title("Live Counter of Time You've Been Alive")

# User input for birth date and time
birth_date = st.date_input("Enter your birth date")
birth_time = st.time_input("Enter your birth time")

# Combine birth date and time into a single datetime object
birth_datetime = datetime.combine(birth_date, birth_time)

# Display the live counter
if st.button("Start Counter"):
    # Create a placeholder for the live counter
    placeholder = st.empty()

    while True:
        weeks, days, hours, minutes, seconds = calculate_time_alive(birth_datetime)
        
        with placeholder.container():
            st.markdown("<h2 style='text-align: center;'>You have been alive for:</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center;'>{weeks} weeks, {days} days, {hours % 24:02d} hours, {minutes % 60:02d} minutes, {seconds % 60:02d} seconds</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center;'>Make sure to make most of what's left</h2>", unsafe_allow_html=True)
        
        time.sleep(1)
        # Necessary to keep the loop running without blocking the app
        placeholder.empty()
