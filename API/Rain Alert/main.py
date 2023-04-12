import json
import requests
import pandas as pd
from twilio.rest import Client

# Download the helper library from https://www.twilio.com/docs/python/instal
# Set environment variables for your credentials
# Read more at http://twil.io/secure
API_KEY = '0b042412XX2XXXXXXXX231204'
account_sid = "AC44fcXXXXXXXXXXXX9508"
auth_token = "9150a47XXXXXXXXXX0b71890"

parameter = {
    "key": API_KEY,
    "q": "Bern",
    "days": 15,
    "exclude": "hourly"
}
response = requests.get(
    "https://api.weatherapi.com/v1/forecast.json", params=parameter)
response.raise_for_status()
data = response.json()
will_rain = False
forecast_slice = data["forecast"]["forecastday"][0]["hour"][:12]
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
