import streamlit as st
import pandas as pd 
import time

st.set_page_config(page_title="Live Track Dashboard", layout="wide")

st.subheader("Live Track Data Simulation")

@st.cache_data
def load_data():
    data = pd.read_csv('track_data.csv')
    return data

data = load_data()

col1, col2 = st.columns(2)

with col1: 
    speed_text=st.empty()
    distance_text=st.empty()
    status_text=st.empty()
with col2:
    chart_placeholder=st.empty()

live_buffer=[]

# This starts the loop. 'row' represents one line of your CSV.
for index, row in data.iterrows():
    
    # 1. HERE is where you define the variables!
    # We take the value from the 'speed' column of the current row
    current_speed = row['speed'] 
    current_distance = row['distance']
    
    # 2. Update the big numbers on your dashboard
    speed_text.metric("Speed", f"{current_speed:.1f} km/h")
    distance_text.metric("Distance", f"{current_distance:.0f} m")
    
    # 3. Determine the status based on the speed we just defined
    if current_speed < 150:
        status_text.error("BRAKING ZONE")
    else:
        status_text.success("ACCELERATING")

    # 4. Add the speed to our list for the chart
    live_buffer.append(current_speed)
    
    # 5. Keep the chart from getting too crowded (show last 50 points)
    if len(live_buffer) > 50:
        live_buffer.pop(0)
    
    # 6. Draw the chart
    chart_placeholder.line_chart(live_buffer)
    
    # 7. Pause for a tiny bit so it looks "real-time"
    time.sleep(0.2)