import json

import requests
import pandas as pd

API_KEY = '0b042412201a4c2c90e34203231204'
parameter = {
    "key": API_KEY,
    "q": "London",
    "days": 15
}
response = requests.get(
    "https://api.weatherapi.com/v1/forecast.json",params=parameter)
response.raise_for_status()
data = response.json()
will_rain = False
forecast_slice = data["forecast"]["forecastday"][0]["hour"][:24]
with open("weather_data.json",mode="w") as data:
    json.dump(forecast_slice,data,indent=6)
for hour_data in forecast_slice:
    condition_code = hour_data["condition"]["code"]
    if condition_code > 1063:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
else:
    print("No rain!!")

# ---------------------------------Reading json file ------------------------------------
# data = pd.read_csv("weather_conditions.csv")
# will_rain = False
# for (index,code) in data.iterrows():
#     if code["code"] > 1063:
#         will_rain = True
#     if will_rain:
#         print("Get Umbrella")
# ----------------------------------------------------------------------------------------
