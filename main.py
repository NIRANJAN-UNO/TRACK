import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# fake track (5000) meters
distance = np.linspace(0,5000,500)

speed = 200 + 50*np.sin(distance/400)-80*np.abs(np.sin(distance/800))

time=np.cumsum(1/(speed/3.6))

data = pd.DataFrame({'distance': distance, 'speed': speed, 'time': time}
)
print(data.head())

plt.plot(data['distance'], data['speed'])
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.title('Speed profile along track')
plt.savefig('speed_profile.png')

corner_threshold = 150
corners = data[data['speed'] < corner_threshold]
print("Detected corners")
print(corners.head())

data["Sector"] = pd.cut(data["distance"], bins=3, labels=[1,2,3])

sector_times = data.groupby("Sector", observed=False)["time"].max()

print(sector_times)
data.to_csv('track_data.csv', index=False)