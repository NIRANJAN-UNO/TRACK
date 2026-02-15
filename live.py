import time
import pandas as pd

data=pd.read_csv('track_data.csv')

print("Starting live data simulation...")
for index, row in data.iterrows():

    current_speed= row['speed']

    status="Flat Out" if current_speed > 150 else "Cornering"
    print(f"Distance: {row['distance']}, Speed: {current_speed}, Status: {status}")
    time.sleep(0.1)