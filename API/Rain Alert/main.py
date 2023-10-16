import json
import requests
import pandas as pd
import os
from twilio.rest import Client

# Download the helper library from https://www.twilio.com/docs/python/instal
# Set environment variables for your credentials
# Read more at http://twil.io/secure


API_KEY = os.environ.get("OWN_API_KEY")
account_sid = "AC44fc8924d646e84c515c4e706c509508"
auth_token = os.environ.get("OWN_AUTH_TOKEN")

parameter = {
    "key": account_sid,
    "q": "London",
    "days": 15,
}
response = requests.get(
    "https://api.weatherapi.com/v1/forecast.json", params=parameter)
response.raise_for_status()
data = response.json()
will_rain = False
forecast_slice = data["forecast"]["forecastday"][0]["hour"][:12]
# print(forecast_slice)
with open("weather_data.json", mode="w") as data:
    json.dump(forecast_slice, data, indent=6)
count = 0
for hour_data in forecast_slice:
    condition_code = hour_data["condition"]["code"]
    if condition_code > 1063:
        will_rain = True
        count += 1
if will_rain:
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Hello from Twilio",
            from_="+15306257739",
            to="+9170XXXXXXX63")
    except Exception as e:
        print(e)
    else:
        print(message.status)

# ---------------------------------Reading json file ------------------------------------
# data = pd.read_csv("weather_conditions.csv")
# will_rain = False
# for (index,code) in data.iterrows():
#     if code["code"] > 1063:
#         will_rain = True
#     if will_rain:
#         print("Get Umbrella")
# ----------------------------------------------------------------------------------------
