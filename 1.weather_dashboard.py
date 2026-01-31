import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Delhi latitude & longitude
LAT = 28.61
LON = 77.20

URL = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    f"&hourly=temperature_2m,relativehumidity_2m"
)

response = requests.get(URL)
data = response.json()

df = pd.DataFrame({
    "Time": data["hourly"]["time"],
    "Temperature (°C)": data["hourly"]["temperature_2m"],
    "Humidity (%)": data["hourly"]["relativehumidity_2m"]
})

df["Time"] = pd.to_datetime(df["Time"])

# Dashboard
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.lineplot(x=df["Time"], y=df["Temperature (°C)"])
plt.title("Temperature Trend")

plt.subplot(1, 2, 2)
sns.lineplot(x=df["Time"], y=df["Humidity (%)"])
plt.title("Humidity Trend")

plt.tight_layout()
plt.show()

