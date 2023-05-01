import json
import os
from datetime import datetime

import requests

API_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
NLP_ENDPOINT = f'https://trackapi.nutritionix.com/v2/natural/exercise'
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

NLP_header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,

}
parameters = {
    "query": input("Tell me your exercises?"),
    "gender": "male",
    "weight_kg": 64,
    "height_cm": 171.9,
    "age": 17
}
r = requests.post(url=NLP_ENDPOINT, headers=NLP_header, json=parameters)
data = r.json()
with open("exercise.json", mode="w") as file:
    json.dump(data, file, indent=6)

workout_post_endpoint = 'https://api.sheety.co/cafbb767c733f083a83e1e17b207d123/myWorkouts/workouts'

# Get user input for name
name = input("What's your name? ")

for exc in data['exercises']:
    header = {
        "Authorization": "Bearer hajhsjsbssauhj"
    }

    param = {
        "workout": {
            'name': name,
            'date': date,
            "time": time,
            "exercise": exc['name'].title(),
            "duration": exc['duration_min'],
            "calories": exc["nf_calories"]
        }
    }
    response = requests.post(url=workout_post_endpoint,headers=header, json=param)
    response.raise_for_status()
    print(response.text)

